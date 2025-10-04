#!/bin/bash

# ScriptShotWeb - Wrapper Script
# Activa automáticamente el entorno virtual y ejecuta el comando

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_PATH="$SCRIPT_DIR/.venv"
SCRIPTSHOTWEB_SCRIPT="$SCRIPT_DIR/scriptshotweb"

# Verificar que existe el entorno virtual
if [ ! -d "$VENV_PATH" ]; then
    echo "❌ Error: No se encontró el entorno virtual en $VENV_PATH"
    exit 1
fi

# Verificar que existe el script principal
if [ ! -f "$SCRIPTSHOTWEB_SCRIPT" ]; then
    echo "❌ Error: No se encontró el script scriptshotweb en $SCRIPT_DIR"
    exit 1
fi

# Activar entorno virtual y ejecutar
source "$VENV_PATH/bin/activate"
"$SCRIPTSHOTWEB_SCRIPT" "$@"