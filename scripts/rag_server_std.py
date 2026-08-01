#!/usr/bin/env python3
"""
rag_server_std.py - Servidor MCP ligero sin dependencias externas

Usa solo bibliotecas estándar de Python (http.server, json).
Compatible con Pi/OpenCode/Claude via MCP protocol.

Uso:
    python3 rag_server_std.py [puerto]
    
    Por defecto: puerto 8765
"""

import json
import os
import sys
import hashlib
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import threading
import time

# Configuración
PROJECT_ROOT = Path(__file__).parent.parent
BRAIN_DIR = PROJECT_ROOT / "brain"
DOCS_DIR = PROJECT_ROOT / "docs"
LINKEDIN_DIR = PROJECT_ROOT / "linkedin"
INDEX_FILE = PROJECT_ROOT / "rag_index.json"


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
    index["last_updated"] = str(time.time())
    
    # Guardar índice
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    
    return index


def search_articles(query: str, limit: int = 10, source: str = "all"):
    """Busca artículos por palabra clave."""
    if not INDEX_FILE.exists():
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


def get_article_by_path(path: str):
    """Obtiene artículo completo por ruta."""
    if not INDEX_FILE.exists():
        build_index()
    
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        index = json.load(f)
    
    for art in index["articles"]:
        if art["path"] == path:
            return art
    
    return None


def list_categories(source: str = "all"):
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


def get_summary(source: str = "all"):
    """Resumen del conocimiento disponible."""
    if not INDEX_FILE.exists():
        build_index()
    
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        index = json.load(f)
    
    filtered_articles = [
        art for art in index["articles"]
        if source == "all" or art["source"] == source
    ]
    
    return {
        "total_articles": len(filtered_articles),
        "categories": index["categories"],
        "last_updated": index["last_updated"]
    }


# =============================================================================
# HTTP Handler para MCP Protocol
# =============================================================================

class MCPHandler(BaseHTTPRequestHandler):
    """Handler HTTP para protocolo MCP."""
    
    def do_POST(self):
        """Procesa solicitudes POST del cliente MCP."""
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        
        try:
            request = json.loads(body.decode('utf-8'))
            
            # Determinar método llamado
            method = request.get('method', '')
            params = request.get('params', {})
            
            # Routing de métodos
            if method == 'search_knowledge':
                result = search_articles(
                    query=params.get('query', ''),
                    limit=params.get('limit', 10),
                    source=params.get('source', 'all')
                )
                response = {"result": result}
            
            elif method == 'get_article':
                article = get_article_by_path(params.get('path', ''))
                response = {"found": bool(article), "article": article}
            
            elif method == 'list_categories':
                categories = list_categories(params.get('source', 'all'))
                response = {"categories": categories}
            
            elif method == 'get_summary':
                summary = get_summary(params.get('source', 'all'))
                response = summary
            
            else:
                response = {"error": f"Método no implementado: {method}"}
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response, indent=2, ensure_ascii=False).encode('utf-8'))
        
        except Exception as e:
            response = {"error": str(e)}
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode('utf-8'))
    
    def do_GET(self):
        """Procesa solicitudes GET (health check, etc)."""
        parsed_path = urlparse(self.path)
        
        if parsed_path.path == '/health':
            response = {"status": "ok", "index_loaded": INDEX_FILE.exists()}
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode('utf-8'))
        
        elif parsed_path.path == '/stats':
            if INDEX_FILE.exists():
                with open(INDEX_FILE, 'r') as f:
                    index = json.load(f)
                response = {
                    "total_articles": index["total"],
                    "categories": len(index["categories"]),
                    "last_updated": index["last_updated"]
                }
            else:
                response = {"error": "Index not built yet"}
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode('utf-8'))
        
        else:
            self.send_response(404)
            self.end_headers()


def run_server(port=8765):
    """Inicia el servidor MCP."""
    print("🚀 Iniciando Piconocimiento RAG Server...")
    print(f"📁 Proyecto: {PROJECT_ROOT}")
    print(f"🔍 Docs: {DOCS_DIR} ({len(list(DOCS_DIR.rglob('*.md')))} artículos)")
    print(f"🧠 Brain: {BRAIN_DIR} ({len(list(BRAIN_DIR.rglob('*.md'))) if BRAIN_DIR.exists() else 0} artículos)")
    
    # Construir índice inicial
    print("🔨 Construyendo índice de búsqueda...")
    build_index()
    
    server = HTTPServer(('localhost', port), MCPHandler)
    print(f"✅ Servidor MCP iniciado en http://localhost:{port}")
    print("📋 Endpoints:")
    print(f"   POST / - Métodos: search_knowledge, get_article, list_categories, get_summary")
    print(f"   GET  /health - Health check")
    print(f"   GET  /stats - Estadísticas del índice")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Servidor detenido")
        server.shutdown()


if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    run_server(port)
