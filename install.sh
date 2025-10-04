#!/bin/bash

# ScriptShotWeb - Installation Script
# Automates the setup process for ScriptShotWeb

echo "🚀 Instalando ScriptShotWeb..."

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 no está instalado. Por favor instala Python 3.7+ primero."
    exit 1
fi

echo "✅ Python3 encontrado: $(python3 --version)"

# Crear entorno virtual si no existe
if [ ! -d ".venv" ]; then
    echo "📦 Creando entorno virtual..."
    python3 -m venv .venv
else
    echo "✅ Entorno virtual ya existe"
fi

# Activar entorno virtual
echo "🔧 Activando entorno virtual..."
source .venv/bin/activate

# Instalar dependencias
echo "📋 Instalando dependencias..."
pip install --upgrade pip
pip install -r requirements.txt

# Instalar navegador Chromium
echo "🌐 Instalando navegador Chromium..."
playwright install chromium

# Hacer scripts ejecutables
echo "🔐 Configurando permisos..."
chmod +x scriptshotweb.sh
chmod +x scriptshotweb

echo ""
echo "✅ ¡Instalación completada!"
echo ""
echo "🎯 Para usar ScriptShotWeb:"
echo "   ./scriptshotweb.sh https://example.com -all"
echo ""
echo "📖 Ver más ejemplos en el README.md"