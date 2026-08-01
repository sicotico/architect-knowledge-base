#!/bin/bash
# =============================================================================
# PICONOCIMIENTO - Sistema de Backup
# =============================================================================
# 
# Este script crea backups automáticos de tu proyecto Piconocimiento.
# Incluye: conversaciones originales, artículos markdown, scripts, y sitio generado.
#
# Uso:
#   bash backup.sh                  # Backup incremental con fecha
#   bash backup.sh full             # Backup completo (sin compresión)
#   bash backup.sh restore <dir>    # Restaurar desde un backup
#   bash backup.sh verify           # Verificar integridad del último backup
#
# =============================================================================

set -euo pipefail

# Configuración
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BACKUP_BASE="${PROJECT_DIR}/backups"
TIMESTAMP=$(date +%Y-%m-%d_%H-%M-%S)
BACKUP_NAME="piconocimiento_${TIMESTAMP}"
LOG_FILE="${BACKUP_BASE}/backup.log"

# Archivos/directorios críticos a incluir
CRITICAL_FILES=(
    "conversations-*.json"
    "export_manifest.json"
    "library_files.json"
    "classification-report.json"
    "MEMORIA.md"
    "PLAN_REORGANIZACION.md"
)

# Directorios a backup
BACKUP_DIRS=(
    "docs"
    "scripts"
    "conversations-*.json"
    "*.py"
    "*.yml"
    "*.md"
    "backups"  # Incluir backups anteriores (para rotación)
)

# Excluir archivos grandes innecesarios
EXCLUDE_PATTERN=(
    "--exclude=site/*"  # El sitio generado puede recrearse
    "--exclude=venv/*"  # Virtual environment
    "--exclude=*.pyc"
    "--exclude=__pycache__/*"
    "--exclude=.git/*"
)

# Funciones de logging
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

error() {
    echo "❌ ERROR: $*" >&2
    log "ERROR: $*"
}

success() {
    echo "✅ $*"
    log "SUCCESS: $*"
}

# Crear directorio de backups si no existe
ensure_backup_dir() {
    mkdir -p "$BACKUP_BASE"
    log "Directorio de backups: $BACKUP_BASE"
}

# Calcular checksum MD5 de un archivo
calc_md5() {
    md5sum "$1" 2>/dev/null | awk '{print $1}' || echo "error"
}

# Verificar espacio disponible
check_disk_space() {
    local required_mb=300  # Proyecto tiene ~285MB
    local available_mb=$(df -m "$BACKUP_BASE" | tail -1 | awk '{print $4}')
    
    if [ "$available_mb" -lt "$required_mb" ]; then
        error "Espacio insuficiente. Disponible: ${available_mb}MB, Necesario: ${required_mb}MB"
        exit 1
    fi
    
    log "Espacio disponible: ${available_mb}MB"
}

# Crear backup incremental con tar+gzip
create_backup() {
    local backup_path="${BACKUP_BASE}/${BACKUP_NAME}"
    local archive="${backup_path}.tar.gz"
    
    log "📦 Creando backup en: $archive"
    
    # Excluir site/ y venv/ para ahorrar espacio
    tar czf "$archive" \
        --exclude='site/*' \
        --exclude='venv/*' \
        --exclude='backups/*' \
        --exclude='*.pyc' \
        --exclude='__pycache__/*' \
        -C "$PROJECT_DIR" \
        . 2>/dev/null
    
    if [ -f "$archive" ]; then
        local size_mb=$(du -m "$archive" | cut -f1)
        local checksum=$(calc_md5 "$archive")
        
        success "Backup creado: ${size_mb}MB"
        echo "✅ MD5: $checksum"
        echo "📁 Ubicación: $archive"
        
        # Guardar checksum en archivo separado para verificación
        echo "${checksum}  ${BACKUP_NAME}.tar.gz" > "${archive}.md5"
        
        return 0
    else
        error "Error al crear el backup"
        return 1
    fi
}

# Crear backup full (sin excluir nada)
create_full_backup() {
    local backup_path="${BACKUP_BASE}/${BACKUP_NAME}_full"
    local archive="${backup_path}.tar.gz"
    
    log "📦 Creando backup FULL en: $archive"
    
    tar czf "$archive" \
        -C "$PROJECT_DIR" \
        . 2>/dev/null
    
    if [ -f "$archive" ]; then
        local size_mb=$(du -m "$archive" | cut -f1)
        success "Backup FULL creado: ${size_mb}MB"
        echo "📁 Ubicación: $archive"
        return 0
    else
        error "Error al crear el backup FULL"
        return 1
    fi
}

# Restaurar desde un backup
restore_backup() {
    local backup_file="$1"
    
    if [ -z "$backup_file" ]; then
        error "Uso: $0 restore <archivo-backup.tar.gz>"
        exit 1
    fi
    
    if [ ! -f "$backup_file" ]; then
        error "Archivo no encontrado: $backup_file"
        exit 1
    fi
    
    log "🔄 Restaurando desde: $backup_file"
    
    # Verificar integridad primero
    if ! tar tzf "$backup_file" > /dev/null 2>&1; then
        error "Archivo corrupto o inválido"
        exit 1
    fi
    
    # Crear backup de seguridad antes de restaurar
    local safety_backup="${PROJECT_DIR}/.backup_safety_$(date +%Y%m%d_%H%M%S)"
    log "Creando backup de seguridad en: $safety_backup"
    cp -r "$PROJECT_DIR" "$safety_backup" 2>/dev/null || true
    
    # Extraer
    tar xzf "$backup_file" -C "$PROJECT_DIR" --overwrite 2>/dev/null
    
    success "✅ Restauración completada"
    log "Backup de seguridad disponible en: $safety_backup"
}

# Verificar integridad del último backup
verify_backup() {
    local latest=$(ls -t "${BACKUP_BASE}"/*.tar.gz 2>/dev/null | head -1)
    
    if [ -z "$latest" ]; then
        error "No hay backups encontrados en $BACKUP_BASE"
        exit 1
    fi
    
    log "🔍 Verificando último backup: $latest"
    
    # Verificar checksum si existe
    if [ -f "${latest}.md5" ]; then
        local stored_checksum=$(cat "${latest}.md5" | awk '{print $1}')
        local current_checksum=$(calc_md5 "$latest")
        
        if [ "$stored_checksum" = "$current_checksum" ]; then
            success "✅ Integridad verificada: MD5 coincide"
        else
            error "❌ Integridad fallida: MD5 no coincide"
            echo "Esperado: $stored_checksum"
            echo "Actual: $current_checksum"
            return 1
        fi
    fi
    
    # Verificar que se pueda listar el tar
    if tar tzf "$latest" > /dev/null 2>&1; then
        local file_count=$(tar tzf "$latest" | wc -l)
        local size_mb=$(du -m "$latest" | cut -f1)
        
        success "✅ Backup íntegro: ${size_mb}MB, ${file_count} archivos"
        return 0
    else
        error "❌ Backup corrupto o inválido"
        return 1
    fi
}

# Limpiar backups antiguos (rotación)
cleanup_old_backups() {
    local keep_days=${1:-30}  # Mantener últimos 30 días por defecto
    
    log "🧹 Limpiando backups anteriores a ${keep_days} días"
    
    local count=0
    while IFS= read -r old_backup; do
        rm -f "$old_backup" "${old_backup}.md5"
        log "Eliminado: $(basename "$old_backup")"
        ((count++))
    done < <(find "$BACKUP_BASE" -name "*.tar.gz" -mtime "+${keep_days}" 2>/dev/null)
    
    if [ "$count" -eq 0 ]; then
        log "No hay backups antiguos que eliminar"
    else
        success "Eliminados ${count} backups antiguos"
    fi
}

# Generar reporte de estado del proyecto
generate_status_report() {
    local report_file="${PROJECT_DIR}/backup-status.json"
    
    log "📊 Generando reporte de estado"
    
    cat > "$report_file" << EOF
{
    "timestamp": "$(date -Iseconds)",
    "project_dir": "$PROJECT_DIR",
    "total_size_mb": $(du -m "$PROJECT_DIR" | cut -f1),
    "file_count": $(find "$PROJECT_DIR" -type f | wc -l),
    "backup_count": $(find "${BACKUP_BASE}" -name "*.tar.gz" 2>/dev/null | wc -l),
    "last_backup": "$(ls -t ${BACKUP_BASE}/*.tar.gz 2>/dev/null | head -1)",
    "critical_files": {
        "conversations": $(ls conversations-*.json 2>/dev/null | wc -l),
        "articles": $(find docs -name "*.md" 2>/dev/null | wc -l),
        "scripts": $(find scripts -name "*.py" 2>/dev/null | wc -l)
    }
}
EOF
    
    success "Reporte generado: $report_file"
}

# Mostrar ayuda
show_help() {
    echo "📦 PICONOCIMIENTO BACKUP SYSTEM"
    echo ""
    echo "Uso: $0 [comando] [opciones]"
    echo ""
    echo "Comandos:"
    echo "  backup          Crear backup incremental (por defecto)"
    echo "  full            Crear backup completo (incluye todo)"
    echo "  restore <file>  Restaurar desde un backup"
    echo "  verify          Verificar integridad del último backup"
    echo "  cleanup [days]  Limpiar backups antiguos (default: 30 días)"
    echo "  status          Generar reporte de estado"
    echo "  help            Mostrar esta ayuda"
    echo ""
    echo "Directorio de backups: $BACKUP_BASE"
}

# =============================================================================
# MAIN
# =============================================================================

main() {
    local command="${1:-backup}"
    
    case "$command" in
        backup)
            ensure_backup_dir
            check_disk_space
            create_backup
            cleanup_old_backups 30
            generate_status_report
            ;;
        full)
            ensure_backup_dir
            check_disk_space
            create_full_backup
            ;;
        restore)
            restore_backup "$2"
            ;;
        verify)
            verify_backup
            ;;
        cleanup)
            cleanup_old_backups "${2:-30}"
            ;;
        status)
            generate_status_report
            cat "backup-status.json"
            ;;
        help|--help|-h)
            show_help
            ;;
        *)
            error "Comando desconocido: $command"
            show_help
            exit 1
            ;;
    esac
}

main "$@"
