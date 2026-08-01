#!/usr/bin/env python3
"""
rag_server.py - Servidor MCP para RAG sobre Piconocimiento

Este script crea un servidor MCP que permite a Pi/OpenCode/Claude
buscar y consultar tu segundo cerebro local.

Uso:
    python3 rag_server.py                    # Iniciar servidor en puerto 8765
    python3 rag_server.py --port 9000        # Puerto personalizado
    python3 rag_server.py --docs-only        # Solo docs públicas (no brain/)
"""

import json
import os
import sys
import hashlib
from pathlib import Path
from typing import Optional
from dataclasses import dataclass, field, asdict

try:
    from fastmcp import FastMCP
except ImportError:
    print("⚠️  Instalando fastmcp...")
    os.system("pip3 install fastmcp --user")
    from fastmcp import FastMCP

# Configuración
PROJECT_ROOT = Path(__file__).parent.parent
BRAIN_DIR = PROJECT_ROOT / "brain"
DOCS_DIR = PROJECT_ROOT / "docs"
LINKEDIN_DIR = PROJECT_ROOT / "linkedin"

# Index de artículos
INDEX_FILE = PROJECT_ROOT / "rag_index.json"


@dataclass
class Article:
    path: str
    title: str
    category: str
    content: str
    metadata: dict = field(default_factory=dict)


def extract_frontmatter(content: str) -> dict:
    """Extrae frontmatter YAML del contenido."""
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            fm = {}
            for line in parts[1].strip().split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    fm[key.strip()] = value.strip()
            return fm
    return {}


def build_index():
    """Construye índice de búsqueda para todos los artículos."""
    index = {
        "articles": [],
        "categories": {},
        "total": 0,
        "last_updated": None
    }
    
    # Escanear directorios
    for dir_path in [DOCS_DIR, BRAIN_DIR]:
        if not dir_path.exists():
            continue
        
        category = "docs" if dir_path == DOCS_DIR else "brain"
        
        for md_file in sorted(dir_path.rglob('*.md')):
            try:
                content = md_file.read_text(encoding='utf-8')
                frontmatter = extract_frontmatter(content)
                
                article = {
                    "path": str(md_file.relative_to(PROJECT_ROOT)),
                    "title": frontmatter.get('title', md_file.stem.replace('-', ' ').title()),
                    "category": frontmatter.get('category', category),
                    "subcategory": frontmatter.get('subcategory', ''),
                    "content_preview": content[:500],
                    "full_content": content,
                    "metadata": frontmatter,
                    "source": category
                }
                
                index["articles"].append(article)
                
                # Actualizar categorías
                cat = article["category"]
                if cat not in index["categories"]:
                    index["categories"][cat] = 0
                index["categories"][cat] += 1
                
            except Exception as e:
                print(f"⚠️ Error leyendo {md_file}: {e}", file=sys.stderr)
    
    index["total"] = len(index["articles"])
    index["last_updated"] = str(Path.now())
    
    # Guardar índice
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    
    return index


def search_articles(query: str, limit: int = 10, source: str = "all") -> list:
    """Busca artículos por palabra clave."""
    if not INDEX_FILE.exists():
        print("🔨 Construyendo índice...")
        build_index()
    
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        index = json.load(f)
    
    query_lower = query.lower()
    results = []
    
    for art in index["articles"]:
        if source != "all" and art["source"] != source:
            continue
        
        # Buscar en título, categoría y contenido
        score = 0
        if query_lower in art["title"].lower():
            score += 10
        if query_lower in art["category"].lower():
            score += 5
        if query_lower in art["content_preview"].lower():
            score += 1
        
        if score > 0:
            results.append({
                "article": art,
                "score": score
            })
    
    # Ordenar por relevancia y limitar
    results.sort(key=lambda x: -x["score"])
    return [r["article"] for r in results[:limit]]


def get_article_by_path(path: str) -> Optional[dict]:
    """Obtiene artículo completo por ruta."""
    if not INDEX_FILE.exists():
        build_index()
    
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        index = json.load(f)
    
    for art in index["articles"]:
        if art["path"] == path:
            return art
    
    return None


def list_categories(source: str = "all") -> dict:
    """Lista categorías disponibles."""
    if not INDEX_FILE.exists():
        build_index()
    
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        index = json.load(f)
    
    categories = {}
    for art in index["articles"]:
        if source != "all" and art["source"] != source:
            continue
        
        cat = art["category"]
        subcat = art.get("subcategory", "")
        
        if cat not in categories:
            categories[cat] = {"total": 0, "subcategories": {}}
        
        categories[cat]["total"] += 1
        
        if subcat:
            if subcat not in categories[cat]["subcategories"]:
                categories[cat]["subcategories"][subcat] = 0
            categories[cat]["subcategories"][subcat] += 1
    
    return categories


# =============================================================================
# Servidor MCP
# =============================================================================

def create_mcp_server():
    """Crea el servidor MCP con herramientas de búsqueda."""
    mcp = FastMCP("Piconocimiento RAG Server")
    
    @mcp.tool()
    def search_knowledge(query: str, limit: int = 10, source: str = "all") -> dict:
        """
        Busca en tu conocimiento personal (docs + brain).
        
        Args:
            query: Término de búsqueda
            limit: Número máximo de resultados
            source: 'all', 'docs' (público), o 'brain' (privado)
        """
        results = search_articles(query, limit, source)
        return {
            "query": query,
            "total_results": len(results),
            "results": results
        }
    
    @mcp.tool()
    def get_article(path: str) -> dict:
        """
        Obtiene artículo completo por ruta.
        
        Args:
            path: Ruta del archivo (ej: 'docs/azure/arquitectura-aks.md')
        """
        article = get_article_by_path(path)
        if article:
            return {"found": True, "article": article}
        return {"found": False, "error": f"Artículo no encontrado: {path}"}
    
    @mcp.tool()
    def list_categories(source: str = "all") -> dict:
        """
        Lista categorías disponibles.
        
        Args:
            source: 'all', 'docs', o 'brain'
        """
        categories = list_categories(source)
        return {
            "source": source,
            "categories": categories
        }
    
    @mcp.tool()
    def get_summary(source: str = "all") -> dict:
        """
        Resumen del conocimiento disponible.
        
        Args:
            source: 'all', 'docs', o 'brain'
        """
        if not INDEX_FILE.exists():
            build_index()
        
        with open(INDEX_FILE, 'r', encoding='utf-8') as f:
            index = json.load(f)
        
        # Filtrar por fuente
        filtered_articles = [
            art for art in index["articles"]
            if source == "all" or art["source"] == source
        ]
        
        return {
            "total_articles": len(filtered_articles),
            "categories": index["categories"],
            "last_updated": index["last_updated"]
        }
    
    return mcp


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Servidor MCP para RAG')
    parser.add_argument('--port', type=int, default=8765, help='Puerto del servidor')
    parser.add_argument('--docs-only', action='store_true', help='Solo docs públicas')
    args = parser.parse_args()
    
    print("🚀 Iniciando Piconocimiento RAG Server...")
    print(f"📁 Proyecto: {PROJECT_ROOT}")
    print(f"🔍 Docs: {DOCS_DIR} ({len(list(DOCS_DIR.rglob('*.md')))} artículos)")
    print(f"🧠 Brain: {BRAIN_DIR} ({len(list(BRAIN_DIR.rglob('*.md'))) if BRAIN_DIR.exists() else 0} artículos)")
    
    # Construir índice inicial
    print("🔨 Construyendo índice de búsqueda...")
    build_index()
    
    # Crear y ejecutar servidor
    mcp = create_mcp_server()
    
    print(f"✅ Servidor MCP iniciado en puerto {args.port}")
    print("📋 Herramientas disponibles:")
    print("  - search_knowledge(query, limit, source)")
    print("  - get_article(path)")
    print("  - list_categories(source)")
    print("  - get_summary(source)")
    
    # Ejecutar servidor
    mcp.run(port=args.port)


if __name__ == '__main__':
    main()
