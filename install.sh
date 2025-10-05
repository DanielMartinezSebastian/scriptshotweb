#!/bin/bash

# ScriptShotWeb - Installation Script
# Automates the setup process for ScriptShotWeb

set -e  # Salir si algún comando falla (excepto donde se maneje explícitamente)

echo "╔════════════════════════════════════════════════════════════╗"
echo "║          🚀 Instalador de ScriptShotWeb v2.1 🚀           ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Función para imprimir con colores
print_success() { echo -e "${GREEN}✅ $1${NC}"; }
print_error() { echo -e "${RED}❌ $1${NC}"; }
print_warning() { echo -e "${YELLOW}⚠️  $1${NC}"; }
print_info() { echo -e "${BLUE}ℹ️  $1${NC}"; }

# Verificar Python
echo "🔍 Paso 1/6: Verificando Python..."
if ! command -v python3 &> /dev/null; then
    print_error "Python3 no está instalado."
    echo ""
    print_info "Instala Python 3.7+ según tu distribución:"
    echo "  • Ubuntu/Debian: sudo apt install python3 python3-venv python3-pip"
    echo "  • Fedora: sudo dnf install python3 python3-pip"
    echo "  • Arch: sudo pacman -S python python-pip"
    exit 1
fi

PYTHON_VERSION=$(python3 --version)
print_success "Python3 encontrado: $PYTHON_VERSION"
echo ""

# Crear entorno virtual si no existe
echo "🔍 Paso 2/6: Configurando entorno virtual..."
if [ ! -d ".venv" ]; then
    echo "📦 Creando entorno virtual..."
    if python3 -m venv .venv; then
        print_success "Entorno virtual creado correctamente"
    else
        print_error "Error al crear entorno virtual"
        print_info "Intenta: sudo apt install python3-venv  # Ubuntu/Debian"
        exit 1
    fi
else
    print_success "Entorno virtual ya existe"
fi
echo ""

# Activar entorno virtual
echo "� Paso 3/6: Activando entorno virtual..."
source .venv/bin/activate
print_success "Entorno virtual activado"
echo ""

# Instalar dependencias Python
echo "� Paso 4/6: Instalando dependencias Python..."
echo "📋 Actualizando pip..."
pip install --upgrade pip --quiet

echo "📋 Instalando playwright y requests..."
if pip install -r requirements.txt; then
    print_success "Dependencias Python instaladas correctamente"
else
    print_error "Error al instalar dependencias Python"
    exit 1
fi
echo ""

# Instalar solo Chromium (más rápido y ligero)
echo "🔍 Paso 5/6: Instalando navegador Chromium..."
print_info "Solo instalamos Chromium para optimizar el proceso"
print_info "Si necesitas Firefox o WebKit, ejecuta: .venv/bin/playwright install firefox webkit"
echo ""

if .venv/bin/playwright install chromium; then
    print_success "Chromium instalado correctamente"
else
    print_warning "Hubo problemas al instalar Chromium"
    echo ""
    print_info "Esto puede deberse a librerías del sistema faltantes."
    echo ""
fi
echo ""

# Verificar dependencias del sistema (solo advertencia, no detener instalación)
echo "🔍 Paso 6/6: Verificando dependencias del sistema..."
print_info "Verificando librerías del sistema necesarias..."
echo ""

# Intentar instalar dependencias del sistema sin detener si falla
if .venv/bin/playwright install-deps chromium 2>/dev/null; then
    print_success "Dependencias del sistema instaladas/verificadas"
else
    print_warning "No se pudieron instalar automáticamente las dependencias del sistema"
    echo ""
    print_info "SOLUCIÓN MANUAL (requiere permisos de administrador):"
    echo ""
    echo "  1. Para Ubuntu/Debian:"
    echo "     sudo apt update"
    echo "     sudo apt install -y libnss3 libnspr4 libatk1.0-0 libatk-bridge2.0-0 \\"
    echo "       libcups2 libdrm2 libxkbcommon0 libxcomposite1 libxdamage1 \\"
    echo "       libxfixes3 libxrandr2 libgbm1 libpango-1.0-0 libcairo2 \\"
    echo "       libasound2 libatspi2.0-0 libxshmfence1"
    echo ""
    echo "  2. Para Fedora:"
    echo "     sudo dnf install -y nss nspr atk at-spi2-atk cups-libs libdrm \\"
    echo "       libxkbcommon libXcomposite libXdamage libXrandr libgbm pango cairo alsa-lib"
    echo ""
    echo "  3. Para Arch Linux:"
    echo "     sudo pacman -S nss nspr atk at-spi2-atk cups libdrm libxkbcommon \\"
    echo "       libxcomposite libxdamage libxrandr mesa pango cairo alsa-lib"
    echo ""
    print_info "O ejecuta como administrador:"
    echo "  sudo .venv/bin/playwright install-deps chromium"
    echo ""
fi

# Hacer scripts ejecutables
echo "🔐 Configurando permisos de ejecución..."
chmod +x scriptshotweb.sh 2>/dev/null || true
chmod +x scriptshotweb 2>/dev/null || true
print_success "Permisos configurados"
echo ""

# Mensaje final
echo "╔════════════════════════════════════════════════════════════╗"
echo "║            ✅ ¡Instalación completada! ✅                 ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
print_success "ScriptShotWeb está listo para usar"
echo ""
echo "🎯 PRÓXIMOS PASOS:"
echo ""
echo "  1. Verificar instalación (recomendado):"
echo "     ./check.sh"
echo ""
echo "  2. Uso básico:"
echo "     ./scriptshotweb.sh https://example.com -all"
echo ""
echo "  3. Modo super (recomendado):"
echo "     ./scriptshotweb.sh https://example.com --super"
echo ""
echo "  4. Ver ayuda completa:"
echo "     ./scriptshotweb.sh --help"
echo "     ./scriptshotweb.sh --info"
echo ""
echo "📖 Más ejemplos en README.md"
echo ""
print_info "Si encuentras errores sobre librerías faltantes, revisa las"
print_info "instrucciones de dependencias del sistema mostradas arriba."
echo ""