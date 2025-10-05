#!/bin/bash

# ScriptShotWeb - System Dependencies Installer
# Instala las dependencias del sistema necesarias para Playwright/Chromium

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

print_success() { echo -e "${GREEN}✅ $1${NC}"; }
print_error() { echo -e "${RED}❌ $1${NC}"; }
print_warning() { echo -e "${YELLOW}⚠️  $1${NC}"; }
print_info() { echo -e "${BLUE}ℹ️  $1${NC}"; }

echo "╔════════════════════════════════════════════════════════════╗"
echo "║     🔧 Instalador de Dependencias del Sistema 🔧         ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

print_warning "Este script instalará librerías del sistema necesarias para Chromium"
print_warning "Requiere permisos de administrador (sudo)"
echo ""

# Detectar distribución
if [ -f /etc/os-release ]; then
    . /etc/os-release
    DISTRO=$ID
    DISTRO_LIKE=$ID_LIKE
else
    print_error "No se pudo detectar la distribución de Linux"
    exit 1
fi

print_info "Distribución detectada: $NAME"
echo ""

# Función para Ubuntu/Debian
install_ubuntu_debian() {
    print_info "Instalando dependencias para Ubuntu/Debian..."
    echo ""
    
    sudo apt update
    sudo apt install -y \
        libnss3 \
        libnspr4 \
        libatk1.0-0 \
        libatk-bridge2.0-0 \
        libcups2 \
        libdrm2 \
        libxkbcommon0 \
        libxcomposite1 \
        libxdamage1 \
        libxfixes3 \
        libxrandr2 \
        libgbm1 \
        libpango-1.0-0 \
        libcairo2 \
        libasound2 \
        libatspi2.0-0 \
        libxshmfence1 \
        fonts-liberation \
        libappindicator3-1 \
        xdg-utils
    
    print_success "Dependencias instaladas correctamente"
}

# Función para Fedora/RHEL/CentOS
install_fedora() {
    print_info "Instalando dependencias para Fedora/RHEL..."
    echo ""
    
    sudo dnf install -y \
        nss \
        nspr \
        atk \
        at-spi2-atk \
        cups-libs \
        libdrm \
        libxkbcommon \
        libXcomposite \
        libXdamage \
        libXrandr \
        libgbm \
        pango \
        cairo \
        alsa-lib \
        liberation-fonts \
        mesa-libgbm
    
    print_success "Dependencias instaladas correctamente"
}

# Función para Arch Linux
install_arch() {
    print_info "Instalando dependencias para Arch Linux..."
    echo ""
    
    sudo pacman -S --needed --noconfirm \
        nss \
        nspr \
        atk \
        at-spi2-atk \
        cups \
        libdrm \
        libxkbcommon \
        libxcomposite \
        libxdamage \
        libxrandr \
        mesa \
        pango \
        cairo \
        alsa-lib \
        ttf-liberation
    
    print_success "Dependencias instaladas correctamente"
}

# Instalar según la distribución
case $DISTRO in
    ubuntu|debian|linuxmint|pop)
        install_ubuntu_debian
        ;;
    fedora|rhel|centos)
        install_fedora
        ;;
    arch|manjaro|endeavouros)
        install_arch
        ;;
    *)
        # Intentar según DISTRO_LIKE
        if [[ $DISTRO_LIKE == *"debian"* ]] || [[ $DISTRO_LIKE == *"ubuntu"* ]]; then
            install_ubuntu_debian
        elif [[ $DISTRO_LIKE == *"fedora"* ]] || [[ $DISTRO_LIKE == *"rhel"* ]]; then
            install_fedora
        elif [[ $DISTRO_LIKE == *"arch"* ]]; then
            install_arch
        else
            print_error "Distribución no soportada automáticamente: $DISTRO"
            echo ""
            print_info "Instala manualmente las siguientes librerías:"
            echo "  • nss, nspr, atk, at-spi2-atk"
            echo "  • cups, libdrm, libxkbcommon"
            echo "  • libxcomposite, libxdamage, libxrandr"
            echo "  • mesa/libgbm, pango, cairo, alsa-lib"
            exit 1
        fi
        ;;
esac

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║         ✅ Dependencias instaladas con éxito ✅          ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
print_info "Ahora puedes ejecutar ScriptShotWeb sin problemas"
echo ""
