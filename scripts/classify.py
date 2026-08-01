#!/usr/bin/env python3
"""
classify.py - Clasifica artículos de Piconocimiento en:
  - publishable: Contenido técnico profesional para MkDocs/LinkedIn
  - second-brain: Contenido personal para segundo cerebro
  - review: Necesita revisión manual

Uso:
    python scripts/classify.py [docs_path]
"""

import json
import os
import sys
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional

# ==================== REGLAS DE CLASIFICACIÓN ====================

# CATEGORÍAS PUBLISHABLE (profesionales)
PUBLISHABLE_TOPICS = {
    # Azure/Cloud
    'azure', 'cloud', 'architecture', 'microservices', 'aks', 'kubernetes',
    'openai', 'ai-foundry', 'machine-learning', 'ml', 'llm', 'rag',
    'api-management', 'cosmos-db', 'blob-storage', 'event-hubs',
    'databricks', 'terraform', 'bicep', 'arm-template', 'vnet',
    'virtual-hub', 'hub-spoke', 'private-link', 'key-vault',
    'managed-identity', 'app-service', 'function-app', 'monitoring',
    'log-analytics', 'application-insights', 'dns-resolver',
    'sql-database', 'postgresql', 'mongodb', 'elastic', 'adx',
    # DevOps/Infra
    'docker', 'container', 'ci-cd', 'pipeline', 'jenkins', 'devops',
    'infrastructure-as-code', 'iac', 'ansible', 'puppet', 'chef',
    # Networking
    'networking', 'tcp-ip', 'osi', 'firewall', 'vpn', 'dns', 'dhcp',
    'switch', 'router', 'vlan', 'subnet', 'cidr', 'ip',
    # Security
    'security', 'cybersecurity', 'zero-trust', 'identity', 'aad',
    'authentication', 'authorization', 'rbac', 'privilege-escalation',
    # Programming
    'python', 'javascript', 'typescript', 'csharp', '.net', 'java',
    'powershell', 'go', 'rust', 'node-js', 'deno', 'api', 'rest',
    'graphql', 'microservices', 'architecture-patterns',
    # AI/ML
    'neural-networks', 'deep-learning', 'transformer', 'attention',
    'prompt-engineering', 'embedding', 'vector-database', 'nlp',
    'computer-vision', 'speech-recognition', 'whisper', 'ollama',
    'lm-studio', 'llama', 'gpt', 'claude', 'gemini',
    # Comparativas técnicas
    'vs', 'comparison', 'benchmark', 'performance', 'alternative',
    # Certificaciones
    'certification', 'exam', 'az-305', 'azure-expert',
}

# CATEGORÍAS SEGUNDO CEREBRO (personal)
PRIVATE_TOPICS = {
    # Personal/Family
    'hipoteca', 'euribor', 'renta', 'fiscalidad', 'impuestos',
    'inversion', 'fondos', 'bolsa', 'ahorro', 'banca',
    'hijo', 'niño', 'guardería', 'colegio', 'paternidad',
    'salud', 'medico', 'holter', 'cardiaco', 'ejercicio',
    'dieta', 'alimentación', 'peso', 'gym',
    # Home/Life
    'solar', 'paneles', 'placa', 'fotovoltaica',
    'moto', 'seguro', 'vehículo', 'coche', 'matriculación',
    'hogar', 'casa', 'piso', 'alquiler',
    # Academic/Homework
    'práctica', 'practica', 'universidad', 'examen', 'curso',
    'tarea', 'deber', 'homework', 'assignment',
    'gramática', 'grammar', 'present-continuous', 'traduccion-escolar',
    # Trivial/Hobbies
    'mate-gentil', 'colaborador', 'comic', 'elefante',
    'consola', 'emulador', 'psp', 'ps2', 'snes', 'rocknix',
    'gameboy', 'nintendo', 'retro', 'gaming',
    # Personal config
    'configurar-contrasena', 'password-a52',
}

# TÍTULOS ESPECÍFICOS A MARCAR
SPECIAL_PUBLISHABLE = {
    'mvp': 'linkedin-priority',  # MVP Azure y LinkedIn
    'arquitectura-ia': 'linkedin-priority',
    'microservicios': 'linkedin-priority',
    'migracion': 'linkedin-priority',
    'pi-coding-agent': 'linkedin-priority',
}

SPECIAL_SECOND_BRAIN = {
    'hipoteca': 'personal-finanzas',
    'euribor': 'personal-finanzas',
    'renta': 'personal-finanzas',
    'declaracion': 'personal-finanzas',
    'hijo': 'personal-familia',
    'niño': 'personal-familia',
    'guardería': 'personal-familia',
    'colegio': 'personal-familia',
    'paternidad': 'personal-familia',
    'salud': 'personal-salud',
    'holter': 'personal-salud',
    'ejercicio': 'personal-salud',
    'solar': 'personal-hogar',
    'placa': 'personal-hogar',
    'moto': 'personal-vehiculo',
    'seguro': 'personal-vehiculo',
    'práctica': 'academico',
    'practica': 'academico',
    'universidad': 'academico',
    'examen': 'academico',
    'consola': 'referencia-hobby',
    'emulador': 'referencia-hobby',
    'comic': 'referencia-trivia',
    'mate-gentil': 'referencia-trivia',
}


@dataclass
class Article:
    path: str
    title: str
    category: str
    content_preview: str = ""
    
    # Clasificación
    classification: str = "review"  # publishable | second-brain | review | linkedin-priority
    subcategory: Optional[str] = None
    confidence: float = 0.0
    notes: str = ""
    
    # Metadata
    size_bytes: int = 0
    word_count: int = 0


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


def get_content_preview(content: str, max_chars: int = 500) -> str:
    """Obtiene un preview del contenido (sin frontmatter)."""
    if content.startswith('---'):
        parts = content.split('---', 3)
        if len(parts) >= 3:
            return parts[2][:max_chars]
    return content[:max_chars]


def classify_article(article: Article) -> None:
    """Clasifica un artículo basado en título, categoría y contenido."""
    title_lower = article.title.lower()
    path_lower = article.path.lower()
    category_lower = article.category.lower()
    preview_lower = article.content_preview.lower()
    
    # Combinar todo el texto para análisis
    full_text = f"{title_lower} {category_lower} {preview_lower}"
    
    # 1. Verificar títulos especiales (LinkedIn priority)
    for keyword, target in SPECIAL_PUBLISHABLE.items():
        if keyword in title_lower or keyword in path_lower:
            article.classification = "linkedin-priority"
            article.subcategory = "azure/ia-architect"
            article.confidence = 0.95
            article.notes = f"Título especial: {keyword}"
            return
    
    # 2. Verificar categorías específicas de segundo cerebro
    for keyword, target in SPECIAL_SECOND_BRAIN.items():
        if keyword in title_lower or keyword in path_lower:
            article.classification = "second-brain"
            article.subcategory = target
            article.confidence = 0.9
            return
    
    # 3. Análisis por palabras clave en contenido
    publishable_score = 0
    private_score = 0
    
    for topic in PUBLISHABLE_TOPICS:
        if topic in full_text:
            publishable_score += 1
    
    for topic in PRIVATE_TOPICS:
        if topic in full_text:
            private_score += 1
    
    # 4. Determinar clasificación final
    if publishable_score > private_score and publishable_score >= 2:
        article.classification = "publishable"
        article.confidence = min(0.5 + publishable_score * 0.1, 0.95)
        article.subcategory = category_lower
    elif private_score > publishable_score and private_score >= 1:
        article.classification = "second-brain"
        article.confidence = min(0.5 + private_score * 0.1, 0.9)
        # Determinar subcategoría de segundo cerebro
        for keyword, target in SPECIAL_SECOND_BRAIN.items():
            if keyword in full_text:
                article.subcategory = target
                break
        if not article.subcategory:
            article.subcategory = "referencia-general"
    else:
        article.classification = "review"
        article.confidence = 0.3
        article.notes = "Requiere revisión manual"


def scan_directory(docs_path: str) -> list:
    """Escanea el directorio docs y retorna lista de artículos."""
    articles = []
    docs_dir = Path(docs_path)
    
    for md_file in sorted(docs_dir.rglob('*.md')):
        # Saltar archivos en directorios especiales
        if any(x in str(md_file) for x in ['unified/', 'improved/', 'assets/']):
            continue
            
        # Saltar archivos de configuración
        if md_file.name in ['mkdocs.yml', 'index.md', 'about.md']:
            continue
        
        try:
            content = md_file.read_text(encoding='utf-8')
        except Exception as e:
            print(f"⚠️ Error leyendo {md_file}: {e}", file=sys.stderr)
            continue
        
        # Extraer metadata
        frontmatter = extract_frontmatter(content)
        title = frontmatter.get('title', md_file.stem.replace('-', ' ').title())
        category = frontmatter.get('category', 'General')
        
        article = Article(
            path=str(md_file.relative_to(docs_dir.parent)),
            title=title,
            category=category,
            content_preview=get_content_preview(content),
            size_bytes=md_file.stat().st_size,
            word_count=len(content.split()),
        )
        
        classify_article(article)
        articles.append(article)
    
    return articles


def generate_report(articles: list, output_path: str) -> None:
    """Genera reporte JSON de clasificación."""
    # Agrupar por clasificación
    groups = {}
    for art in articles:
        if art.classification not in groups:
            groups[art.classification] = []
        groups[art.classification].append({
            'path': art.path,
            'title': art.title,
            'category': art.category,
            'subcategory': art.subcategory,
            'confidence': round(art.confidence, 2),
            'notes': art.notes,
            'word_count': art.word_count,
        })
    
    # Resumen estadístico
    summary = {
        'total_articles': len(articles),
        'by_classification': {k: len(v) for k, v in groups.items()},
        'by_confidence': {
            'high (>0.8)': sum(1 for a in articles if a.confidence > 0.8),
            'medium (0.5-0.8)': sum(1 for a in articles if 0.5 < a.confidence <= 0.8),
            'low (<0.5)': sum(1 for a in articles if a.confidence <= 0.5),
        },
    }
    
    report = {
        'summary': summary,
        'articles_by_classification': groups,
    }
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    # Imprimir resumen en consola
    print(f"\n{'='*60}")
    print(f"📊 REPORTE DE CLASIFICACIÓN")
    print(f"{'='*60}\n")
    print(f"Total de artículos analizados: {summary['total_articles']}")
    print(f"\nPor clasificación:")
    for cls, count in sorted(summary['by_classification'].items(), key=lambda x: -x[1]):
        print(f"  • {cls}: {count} artículos")
    print(f"\nPor confianza:")
    for conf, count in summary['by_confidence'].items():
        print(f"  • {conf}: {count} artículos")
    
    print(f"\nReporte completo: {output_path}")


def generate_move_commands(articles: list) -> None:
    """Genera comandos de bash para mover archivos."""
    print(f"\n{'='*60}")
    print(f"📁 COMANDOS DE REORGANIZACIÓN")
    print(f"{'='*60}\n")
    
    # Publishable → docs/ (mantener estructura actual)
    publishable = [a for a in articles if a.classification == 'publishable']
    if publishable:
        print("# ✅ PUBLICABLES - Mantener en docs/")
        for art in publishable[:10]:  # Mostrar primeros 10
            print(f"  # {art.path} → docs/{art.category.lower()}/{os.path.basename(art.path)}")
        if len(publishable) > 10:
            print(f"  ... y {len(publishable) - 10} más")
        print()
    
    # Second brain → brain/
    second_brain = [a for a in articles if a.classification == 'second-brain']
    if second_brain:
        print("# 🔒 SEGUNDO CEREBRO - Mover a brain/")
        for art in second_brain[:10]:
            target = f"brain/{art.subcategory or 'referencia'}/{os.path.basename(art.path)}"
            print(f"  # {art.path} → {target}")
        if len(second_brain) > 10:
            print(f"  ... y {len(second_brain) - 10} más")
        print()
    
    # LinkedIn priority
    linkedin = [a for a in articles if a.classification == 'linkedin-priority']
    if linkedin:
        print("# 🌟 LINKEDIN PRIORITY - Reescribir para LinkedIn")
        for art in linkedin:
            print(f"  # {art.path} → linkedin/drafts/{os.path.basename(art.path)}")
        print()
    
    # Review needed
    review = [a for a in articles if a.classification == 'review']
    if review:
        print("# ❓ REQUIEREN REVISIÓN MANUAL")
        for art in review[:10]:
            print(f"  # {art.path} → Revisar manualmente")
        if len(review) > 10:
            print(f"  ... y {len(review) - 10} más")


def main():
    if len(sys.argv) < 2:
        docs_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'docs')
    else:
        docs_path = sys.argv[1]
    
    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'classification-report.json')
    
    print(f"🔍 Escaneando directorio: {docs_path}")
    articles = scan_directory(docs_path)
    
    if not articles:
        print("⚠️ No se encontraron artículos para clasificar.")
        return
    
    generate_report(articles, output_path)
    generate_move_commands(articles)
    
    print(f"\n✅ Clasificación completada: {len(articles)} artículos procesados")


if __name__ == '__main__':
    main()
