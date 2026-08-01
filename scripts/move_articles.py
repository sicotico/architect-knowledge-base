#!/usr/bin/env python3
"""
move_articles.py - Mueve archivos según clasificación (Fase 2 del plan)

Ejecución:
    python3 move_articles.py --dry-run   # Ver qué se moverá
    python3 move_articles.py --execute   # Ejecutar movimiento real
"""

import json
import os
import sys
import shutil
from pathlib import Path
from dataclasses import dataclass


@dataclass
class MoveOperation:
    source: str
    destination: str
    category: str
    title: str


def load_classification(report_path: str) -> dict:
    """Carga el reporte de clasificación."""
    with open(report_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def move_articles(dry_run: bool = True):
    """Mueve archivos según la clasificación."""
    project_root = Path(__file__).parent.parent
    report_path = project_root / 'classification-report.json'
    
    if not report_path.exists():
        print("❌ No se encontró classification-report.json")
        return
    
    data = load_classification(str(report_path))
    operations = []
    
    # 1. Mover second-brain a brain/
    for art in data['articles_by_classification']['second-brain']:
        src = project_root / art['path']
        subdir = art.get('subcategory', 'referencia-general')
        dst = project_root / 'brain' / subdir / os.path.basename(art['path'])
        
        operations.append(MoveOperation(
            source=str(src),
            destination=str(dst),
            category='second-brain',
            title=art['title']
        ))
    
    # 2. Mover linkedin-priority a linkedin/drafts/
    for art in data['articles_by_classification']['linkedin-priority']:
        src = project_root / art['path']
        dst = project_root / 'linkedin' / 'drafts' / os.path.basename(art['path'])
        
        operations.append(MoveOperation(
            source=str(src),
            destination=str(dst),
            category='linkedin',
            title=art['title']
        ))
    
    # 3. Eliminar de docs/ los que se mueven (publishable se quedan)
    for op in operations:
        if dry_run:
            print(f"📁 DRY-RUN: {op.source}")
            print(f"   → {op.destination}")
            print(f"   📝 {op.title}")
            print()
        else:
            # Crear directorio destino si no existe
            os.makedirs(os.path.dirname(op.destination), exist_ok=True)
            
            # Mover archivo
            if os.path.exists(op.source):
                shutil.move(op.source, op.destination)
                print(f"✅ Movido: {op.source} → {op.destination}")
            else:
                print(f"⚠️ No encontrado: {op.source}")


def update_mkdocs():
    """Actualiza mkdocs.yml para excluir directorios privados."""
    project_root = Path(__file__).parent.parent
    mkdocs_path = project_root / 'mkdocs.yml'
    
    if not mkdocs_path.exists():
        print("❌ No se encontró mkdocs.yml")
        return
    
    # Leer contenido actual
    with open(mkdocs_path, 'r') as f:
        content = f.read()
    
    # Añadir exclusiones si no existen
    exclusions = [
        "exclude_docs:",
        "  - brain/",
        "  - linkedin/",
        "  - scripts/",
        "  - backups/",
    ]
    
    # Verificar si ya existen exclusiones
    if 'exclude_docs:' not in content:
        # Añadir al final del archivo
        content += "\n" + "\n".join(exclusions) + "\n"
        
        with open(mkdocs_path, 'w') as f:
            f.write(content)
        
        print("✅ mkdocs.yml actualizado con exclusiones")
    else:
        print("ℹ️ mkdocs.yml ya tiene exclusiones configuradas")


def main():
    dry_run = '--dry-run' in sys.argv
    execute = '--execute' in sys.argv
    
    if not dry_run and not execute:
        print("⚠️ Uso: python3 move_articles.py --dry-run o --execute")
        print("   --dry-run: Solo muestra qué se moverá")
        print("   --execute: Ejecuta los movimientos reales")
        return
    
    if dry_run:
        print("🔍 Modo DRY-RUN (sin cambios reales)")
        print("="*60)
    
    move_articles(dry_run=not execute)
    
    if execute:
        print("\n" + "="*60)
        update_mkdocs()
        print("\n✅ Movimiento completado")
        print("📋 Ahora ejecuta:")
        print("   - bash backup.sh backup  # Backup post-movimiento")
        print("   - mkdocs build           # Regenerar sitio")


if __name__ == '__main__':
    main()
