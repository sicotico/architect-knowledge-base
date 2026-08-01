#!/bin/bash
# Git Backup - Push semanal a GitHub
# Uso: bash git-backup.sh

set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"
}

# Verificar si hay cambios
if ! git diff --quiet 2>/dev/null; then
    log "📤 Haciendo backup a GitHub..."
    
    # Añadir todos los cambios
    git add -A
    
    # Commit con fecha actual
    git commit -m "Backup automático $(date +%Y-%m-%d_%H:%M:%S)" || true
    
    # Push al remote principal
    git push origin main 2>/dev/null || git push origin master 2>/dev/null || {
        log "⚠️ No se pudo hacer push. Verifica la conexión."
        exit 1
    }
    
    log "✅ Backup GitHub completado"
else
    log "ℹ️ No hay cambios para backup"
fi

# Mostrar estado actual
log "📊 Estado del repositorio:"
git status --short 2>/dev/null || echo "No es un repositorio git"
