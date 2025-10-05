#!/bin/bash

# ScriptShotWeb - Verification Script
# Verifica que todos los componentes estén instalados correctamente

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

print_success() { echo -e "${GREEN}✅ $1${NC}"; }
print_error() { echo -e "${RED}❌ $1${NC}"; }
print_warning() { echo -e "${YELLOW}⚠️  $1${NC}"; }
print_info() { echo -e "${BLUE}ℹ️  $1${NC}"; }

ERRORS=0
WARNINGS=0

echo "╔════════════════════════════════════════════════════════════╗"
echo "║       🔍 Verificación de ScriptShotWeb v2.1 🔍           ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# 1. Verificar Python
echo "📋 Verificando Python..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    print_success "Python instalado: $PYTHON_VERSION"
    
    # Verificar versión de Python
    PYTHON_MINOR=$(python3 -c 'import sys; print(sys.version_info.minor)')
    if [ $PYTHON_MINOR -lt 7 ]; then
        print_warning "Python 3.$PYTHON_MINOR detectado. Se recomienda Python 3.7+"
        WARNINGS=$((WARNINGS + 1))
    fi
else
    print_error "Python3 no está instalado"
    ERRORS=$((ERRORS + 1))
fi
echo ""

# 2. Verificar entorno virtual
echo "📋 Verificando entorno virtual..."
if [ -d ".venv" ]; then
    print_success "Entorno virtual existe"
    
    # Verificar que tiene los binarios necesarios
    if [ -f ".venv/bin/python" ] && [ -f ".venv/bin/pip" ]; then
        print_success "Binarios del entorno virtual OK"
    else
        print_error "Entorno virtual incompleto"
        ERRORS=$((ERRORS + 1))
    fi
else
    print_error "Entorno virtual no existe (.venv/)"
    print_info "Ejecuta: ./install.sh"
    ERRORS=$((ERRORS + 1))
fi
echo ""

# 3. Verificar dependencias Python (activando entorno virtual)
echo "📋 Verificando dependencias Python..."
if [ -d ".venv" ]; then
    source .venv/bin/activate
    
    # Verificar playwright
    if python3 -c "import playwright" 2>/dev/null; then
        PLAYWRIGHT_VERSION=$(python3 -c "import playwright; print(playwright.__version__)" 2>/dev/null)
        print_success "Playwright instalado: v$PLAYWRIGHT_VERSION"
    else
        print_error "Playwright no está instalado"
        print_info "Ejecuta: ./install.sh"
        ERRORS=$((ERRORS + 1))
    fi
    
    # Verificar requests
    if python3 -c "import requests" 2>/dev/null; then
        REQUESTS_VERSION=$(python3 -c "import requests; print(requests.__version__)" 2>/dev/null)
        print_success "Requests instalado: v$REQUESTS_VERSION"
    else
        print_error "Requests no está instalado"
        print_info "Ejecuta: ./install.sh"
        ERRORS=$((ERRORS + 1))
    fi
else
    print_warning "No se pueden verificar dependencias sin entorno virtual"
    WARNINGS=$((WARNINGS + 1))
fi
echo ""

# 4. Verificar navegador Chromium
echo "📋 Verificando navegador Chromium..."
if [ -d ".venv" ]; then
    # Buscar el ejecutable de Chromium en la ubicación típica de Playwright
    CHROMIUM_PATH="$HOME/.cache/ms-playwright/chromium-*/chrome-linux/chrome"
    
    if ls $CHROMIUM_PATH 2>/dev/null 1>&2; then
        print_success "Chromium instalado"
        
        # Obtener versión de chromium
        CHROMIUM_VERSION=$(ls -d $HOME/.cache/ms-playwright/chromium-* 2>/dev/null | head -1 | sed 's/.*chromium-//')
        if [ ! -z "$CHROMIUM_VERSION" ]; then
            print_info "Versión: $CHROMIUM_VERSION"
        fi
    else
        print_error "Chromium no está instalado"
        print_info "Ejecuta: .venv/bin/playwright install chromium"
        ERRORS=$((ERRORS + 1))
    fi
else
    print_warning "No se puede verificar Chromium sin entorno virtual"
    WARNINGS=$((WARNINGS + 1))
fi
echo ""

# 5. Verificar scripts ejecutables
echo "📋 Verificando scripts..."
if [ -f "scriptshotweb" ]; then
    if [ -x "scriptshotweb" ]; then
        print_success "Script scriptshotweb ejecutable"
    else
        print_warning "Script scriptshotweb no es ejecutable"
        print_info "Ejecuta: chmod +x scriptshotweb"
        WARNINGS=$((WARNINGS + 1))
    fi
else
    print_error "Script scriptshotweb no encontrado"
    ERRORS=$((ERRORS + 1))
fi

if [ -f "scriptshotweb.sh" ]; then
    if [ -x "scriptshotweb.sh" ]; then
        print_success "Wrapper scriptshotweb.sh ejecutable"
    else
        print_warning "Wrapper scriptshotweb.sh no es ejecutable"
        print_info "Ejecuta: chmod +x scriptshotweb.sh"
        WARNINGS=$((WARNINGS + 1))
    fi
else
    print_error "Wrapper scriptshotweb.sh no encontrado"
    ERRORS=$((ERRORS + 1))
fi
echo ""

# 6. Verificar dependencias del sistema (test rápido)
echo "📋 Verificando dependencias del sistema..."
if [ -d ".venv" ]; then
    source .venv/bin/activate
    
    # Intentar una verificación rápida
    PLAYWRIGHT_CHECK=$(.venv/bin/playwright install --dry-run chromium 2>&1)
    
    if echo "$PLAYWRIGHT_CHECK" | grep -q "Host system is missing dependencies"; then
        print_warning "Faltan dependencias del sistema"
        print_info "Ejecuta: sudo ./install-deps.sh"
        WARNINGS=$((WARNINGS + 1))
    else
        print_success "Dependencias del sistema OK"
    fi
else
    print_warning "No se pueden verificar dependencias del sistema"
    WARNINGS=$((WARNINGS + 1))
fi
echo ""

# 7. Test funcional básico (opcional pero útil)
echo "📋 Test funcional (opcional)..."
if [ $ERRORS -eq 0 ]; then
    print_info "Intentando captura de prueba en example.com..."
    
    if timeout 30s ./scriptshotweb.sh https://example.com --device desktop 2>&1 | grep -q "Capturas completadas"; then
        print_success "Test funcional PASADO"
        print_info "ScriptShotWeb funciona correctamente"
    else
        print_warning "Test funcional falló o tardó demasiado"
        print_info "Esto podría ser por problemas de red o dependencias faltantes"
        WARNINGS=$((WARNINGS + 1))
    fi
else
    print_warning "Test funcional omitido (errores críticos detectados)"
fi
echo ""

# Resumen
echo "╔════════════════════════════════════════════════════════════╗"
echo "║                     📊 RESUMEN                            ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

if [ $ERRORS -eq 0 ] && [ $WARNINGS -eq 0 ]; then
    print_success "TODO CORRECTO - ScriptShotWeb está listo para usar"
    echo ""
    echo "🎯 Prueba con:"
    echo "   ./scriptshotweb.sh https://example.com --super"
    echo ""
elif [ $ERRORS -eq 0 ]; then
    print_warning "$WARNINGS advertencia(s) encontrada(s)"
    echo ""
    print_info "ScriptShotWeb debería funcionar, pero revisa las advertencias"
    echo ""
else
    print_error "$ERRORS error(es) crítico(s) y $WARNINGS advertencia(s)"
    echo ""
    print_info "Soluciones recomendadas:"
    echo ""
    echo "  1. Reinstalar componentes:"
    echo "     ./install.sh"
    echo ""
    echo "  2. Instalar dependencias del sistema:"
    echo "     sudo ./install-deps.sh"
    echo ""
    echo "  3. Verificar nuevamente:"
    echo "     ./check.sh"
    echo ""
fi

exit $ERRORS
