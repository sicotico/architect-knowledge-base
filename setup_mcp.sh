#!/bin/bash
# =============================================================================
# PICONOCIMIENTO - Setup MCP Server para RAG
# =============================================================================
# Este script configura el servidor MCP para que Pi/OpenCode/Claude
# pueda consultar tu segundo cerebro local.
#
# Uso:
#   bash setup_mcp.sh          # Configurar todo automáticamente
#   bash setup_mcp.sh test     # Probar la conexión
#   bash setup_mcp.sh stop     # Detener servidor
# =============================================================================

set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MCP_PORT=8765
MCP_CONFIG="${PROJECT_DIR}/.vscode/mcp.json"
PID_FILE="${PROJECT_DIR}/mcp_server.pid"
SERVER_SCRIPT="${PROJECT_DIR}/scripts/rag_server_std.py"

# Funciones de logging
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"
}

success() {
    echo "✅ $*"
}

error() {
    echo "❌ ERROR: $*" >&2
}

# Verificar dependencias
check_dependencies() {
    log "🔍 Verificando dependencias..."
    
    # Verificar Python 3
    if ! command -v python3 &> /dev/null; then
        error "Python 3 no encontrado"
        exit 1
    fi
    
    # Verificar servidor estándar (no requiere dependencias)
    if [ ! -f "$SERVER_SCRIPT" ]; then
        error "Servidor MCP no encontrado: $SERVER_SCRIPT"
        exit 1
    fi
    
    log "✅ Dependencias verificadas"
}

# Configurar MCP en VS Code / Pi
setup_vscode_config() {
    log "⚙️  Configurando MCP para VS Code / Pi..."
    
    # Crear directorio .vscode si no existe
    mkdir -p "${PROJECT_DIR}/.vscode"
    
    # Crear config MCP
    cat > "$MCP_CONFIG" << EOF
{
    "mcpServers": {
        "piconocimiento-rag": {
            "command": "python3",
            "args": [
                "${PROJECT_DIR}/scripts/rag_server.py"
            ],
            "env": {},
            "cwd": "${PROJECT_DIR}",
            "port": ${MCP_PORT}
        }
    }
}
EOF
    
    success "Config MCP creada en: $MCP_CONFIG"
    echo "📋 Ahora en VS Code:"
    echo "   1. Abre la configuración de MCP (si usa MCP)"
    echo "   2. El servidor se conectará automáticamente"
}

# Iniciar servidor MCP
start_server() {
    log "🚀 Iniciando servidor MCP..."
    
    # Verificar si ya está corriendo
    if [ -f "$PID_FILE" ]; then
        local old_pid=$(cat "$PID_FILE")
        if kill -0 "$old_pid" 2>/dev/null; then
            log "⚠️  Servidor ya corriendo (PID: $old_pid)"
            echo "   Para reiniciar: bash setup_mcp.sh stop && bash setup_mcp.sh start"
            return 0
        fi
    fi
    
    # Iniciar servidor en background
    nohup python3 "${PROJECT_DIR}/scripts/rag_server.py" --port $MCP_PORT > "${PROJECT_DIR}/mcp_server.log" 2>&1 &
    local server_pid=$!
    
    echo "$server_pid" > "$PID_FILE"
    
    # Esperar a que el servidor inicie
    sleep 2
    
    if kill -0 "$server_pid" 2>/dev/null; then
        success "Servidor MCP iniciado (PID: $server_pid)"
        echo "📡 Puerto: $MCP_PORT"
        echo "📋 Logs: ${PROJECT_DIR}/mcp_server.log"
        echo "🧪 Probar: bash setup_mcp.sh test"
    else
        error "Error al iniciar servidor"
        cat "${PROJECT_DIR}/mcp_server.log"
        exit 1
    fi
}

# Detener servidor MCP
stop_server() {
    log "🛑 Deteniendo servidor MCP..."
    
    if [ -f "$PID_FILE" ]; then
        local pid=$(cat "$PID_FILE")
        if kill -0 "$pid" 2>/dev/null; then
            kill "$pid"
            success "Servidor detenido (PID: $pid)"
        else
            log "ℹ️  Servidor no estaba corriendo"
        fi
        rm -f "$PID_FILE"
    else
        log "ℹ️  No hay servidor corriendo"
    fi
}

# Probar conexión MCP
test_connection() {
    log "🧪 Probando conexión MCP..."
    
    if [ ! -f "$PID_FILE" ]; then
        error "Servidor no corriendo. Inicia con: bash setup_mcp.sh start"
        exit 1
    fi
    
    # Probar búsqueda básica
    python3 -c "
import sys
sys.path.insert(0, '${PROJECT_DIR}/scripts')
from rag_server import search_articles, get_summary

print('🔍 Probando búsqueda...')
results = search_articles('Azure', limit=3)
print(f'✅ Búsqueda Azure: {len(results)} resultados')

for art in results[:2]:
    print(f'   - {art[\"title\"]}')

print()
print('📊 Resumen del conocimiento:')
summary = get_summary()
print(f'   Total artículos: {summary[\"total_articles\"]}')
print(f'   Categorías: {len(summary[\"categories\"])}')
"
    
    success "✅ Conexión MCP verificada"
}

# Mostrar estado
show_status() {
    echo "📊 Estado del Sistema Piconocimiento"
    echo "====================================="
    echo ""
    
    # Servidor MCP
    if [ -f "$PID_FILE" ]; then
        local pid=$(cat "$PID_FILE")
        if kill -0 "$pid" 2>/dev/null; then
            echo "🟢 Servidor MCP: Corriendo (PID: $pid)"
        else
            echo "🔴 Servidor MCP: Detenido"
        fi
    else
        echo "⚪ Servidor MCP: No configurado"
    fi
    
    # Artículos
    local docs_count=$(find "${PROJECT_DIR}/docs" -name "*.md" 2>/dev/null | wc -l)
    local brain_count=$(find "${PROJECT_DIR}/brain" -name "*.md" 2>/dev/null | wc -l)
    local linkedin_count=$(find "${PROJECT_DIR}/linkedin" -name "*.md" 2>/dev/null | wc -l)
    
    echo "📚 Artículos:"
    echo "   Docs (públicos): $docs_count"
    echo "   Brain (privados): $brain_count"
    echo "   LinkedIn: $linkedin_count"
    
    # Backups
    local backup_count=$(find "${PROJECT_DIR}/backups" -name "*.tar.gz" 2>/dev/null | wc -l)
    echo ""
    echo "💾 Backups:"
    echo "   Backups locales: $backup_count"
    
    if [ -f "${PROJECT_DIR}/backup-status.json" ]; then
        local last_backup=$(python3 -c "import json; d=json.load(open('${PROJECT_DIR}/backup-status.json')); print(d.get('last_backup', 'N/A'))")
        echo "   Último backup: $last_backup"
    fi
}

# =============================================================================
# Main
# =============================================================================

main() {
    local command="${1:-setup}"
    
    case "$command" in
        setup)
            check_dependencies
            setup_vscode_config
            start_server
            test_connection
            show_status
            ;;
        start)
            start_server
            ;;
        stop)
            stop_server
            ;;
        restart)
            stop_server
            sleep 1
            start_server
            ;;
        test)
            test_connection
            ;;
        status)
            show_status
            ;;
        help|--help|-h)
            echo "📦 PICONOCIMIENTO MCP SETUP"
            echo ""
            echo "Uso: $0 [comando]"
            echo ""
            echo "Comandos:"
            echo "  setup   Configurar todo automáticamente"
            echo "  start   Iniciar servidor MCP"
            echo "  stop    Detener servidor MCP"
            echo "  restart Reiniciar servidor MCP"
            echo "  test    Probar conexión"
            echo "  status  Mostrar estado del sistema"
            echo "  help    Mostrar esta ayuda"
            ;;
        *)
            error "Comando desconocido: $command"
            show_help
            exit 1
            ;;
    esac
}

main "$@"
