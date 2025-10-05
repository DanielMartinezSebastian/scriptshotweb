# 🔧 Troubleshooting - Wshot

Complete guide to solve common issues with Wshot.

## 🚨 Most Common Issues

### 1. Error: "requests library not installed" or dependency issues

**Symptom:** `❌ Error: The 'requests' library is not installed` or similar dependency errors.

**Cause:** This happens when using `pipx` due to isolated environments.

**Solutions:**

#### Option A: Use pip (Recommended for most users)
```bash
# Uninstall pipx version if installed
pipx uninstall wshot

# Install with pip
pip install wshot
playwright install chromium
```

#### Option B: Fix pipx installation
```bash
# Inject missing dependencies
pipx inject wshot playwright requests
```

#### Option C: Virtual environment (Best practice)
```bash
python -m venv wshot-env
source wshot-env/bin/activate  # Linux/Mac
# wshot-env\Scripts\activate     # Windows
pip install wshot
playwright install chromium
```

### 2. Error: "libicudata.so.66 not found" or other missing libraries

**Symptom:** Error when running captures mentioning missing `.so` libraries.

**Cause:** Missing system dependencies for Playwright/Chromium.

**Solution:**

#### Ubuntu/Debian
```bash
sudo apt update && sudo apt install -y libnss3 libnspr4 libatk1.0-0 \
  libatk-bridge2.0-0 libcups2 libdrm2 libxkbcommon0 libxcomposite1 \
  libxdamage1 libxfixes3 libxrandr2 libgbm1 libpango-1.0-0 libcairo2 libasound2
```

#### Fedora
```bash
sudo dnf install -y nss nspr atk at-spi2-atk cups-libs libdrm \
  libxkbcomposite libxdamage libXrandr libgbm pango cairo alsa-lib
```

#### Arch Linux
```bash
sudo pacman -S nss nspr atk at-spi2-atk cups libdrm libxkbcommon \
  libxcomposite libxdamage libxrandr mesa pango cairo alsa-lib
```

### 2. Error: "playwright: command not found"

**Symptom:** Playwright command is not found.

**Cause:** Playwright is not installed or not in PATH.

**Solution:**
```bash
# Reinstall playwright
pip install playwright
playwright install chromium

# If you used pipx on Arch Linux
~/.local/share/pipx/venvs/wshot/bin/playwright install chromium
```

### 3. Screenshots come out black or empty

**Symptom:** Captured images are black or show no content.

**Possible Causes:**
- Website requires more time to load
- JavaScript needs extra time to render
- Permission or configuration issues

**Solutions:**

#### Increase wait time
```bash
# Increase wait time to 10 seconds
wshot https://site.com --device desktop --wait-time 10
```

#### Use super mode with optimizations
```bash
# Super mode includes smooth scroll and optimized timing
wshot https://site.com --super
```

#### Verify installation
```bash
# Verify everything is correctly installed
python test_installation.py
```

### 4. Error: "URL no responde" con URLs válidas

**Síntoma:** Wshot dice que la URL no responde pero funciona en el navegador.

**Posibles Causas:**
- Firewall o proxy bloqueando conexiones
- Sitio web bloquea requests automatizados
- Problemas de DNS o conectividad

**Soluciones:**

#### Verificar conectividad
```bash
# Probar conectividad básica
curl -I https://sitio.com

# Verificar DNS
nslookup sitio.com
```

#### Probar con sitios conocidos
```bash
# Probar con sitios que definitivamente funcionan
wshot https://example.com --device desktop
wshot https://google.com --device desktop
```

### 5. Error: "No such file or directory" al instalar

**Síntoma:** Error durante la instalación con pip.

**Causa:** Problemas con pip, Python o permisos.

**Solución:**
```bash
# Actualizar pip
python3 -m pip install --upgrade pip

# Reinstalar desde cero
pip uninstall wshot
pip install git+https://github.com/DanielMartinezSebastian/wshot.git

# Si hay problemas de permisos, usar entorno virtual
python3 -m venv wshot-env
source wshot-env/bin/activate
pip install git+https://github.com/DanielMartinezSebastian/wshot.git
```

## 🐧 Problemas Específicos de Linux

### Wayland vs X11
**Síntoma:** Problemas de captura en escritorios Wayland.

**Solución:**
```bash
# Forzar uso de X11 temporalmente
export XDG_SESSION_TYPE=x11

# O ejecutar en modo compatibilidad
wshot https://sitio.com --device desktop
```

### Permisos de escritura
**Síntoma:** Error al crear carpetas en `~/Pictures/WSHOT/`.

**Solución:**
```bash
# Verificar permisos
ls -la ~/Pictures/

# Crear carpeta manualmente si es necesario
mkdir -p ~/Pictures/WSHOT/

# Usar directorio alternativo
wshot https://sitio.com --device desktop --output-dir ~/Descargas/capturas
```

## 🪟 Problemas Específicos de Windows

### PowerShell vs CMD
**Síntoma:** Comandos no funcionan correctamente.

**Solución:**
```powershell
# Usar PowerShell (recomendado)
wshot https://example.com --device desktop

# En CMD usar comillas
wshot "https://example.com" --device desktop
```

### Rutas con espacios
**Síntoma:** Error con rutas que contienen espacios.

**Solución:**
```powershell
# Usar comillas para rutas con espacios
wshot https://example.com --device desktop --output-dir "C:\Mis Documentos\Capturas"
```

## 🍎 Problemas Específicos de macOS

### Permisos de seguridad
**Síntoma:** macOS bloquea la ejecución por seguridad.

**Solución:**
1. Ir a Configuración del Sistema > Privacidad y Seguridad
2. Permitir la aplicación en la sección de desarrollador
3. O ejecutar desde Terminal con permisos de administrador

### Rosetta en Apple Silicon
**Síntoma:** Problemas en Macs con chip M1/M2.

**Solución:**
```bash
# Instalar Rosetta si es necesario
softwareupdate --install-rosetta

# Verificar arquitectura
arch

# Reinstalar con arquitectura correcta
pip uninstall wshot
pip install git+https://github.com/DanielMartinezSebastian/wshot.git
```

## 🌐 Problemas de Red

### Proxy corporativo
**Síntoma:** Error de conexión en redes corporativas.

**Solución:**
```bash
# Configurar proxy para pip
pip install --proxy http://proxy.empresa.com:8080 git+https://github.com/DanielMartinezSebastian/wshot.git

# Configurar proxy para Playwright
export HTTP_PROXY=http://proxy.empresa.com:8080
export HTTPS_PROXY=http://proxy.empresa.com:8080
```

### VPN o geobloqueo
**Síntoma:** Sitios no cargan correctamente con VPN.

**Solución:**
```bash
# Probar sin VPN temporalmente
# O usar headers personalizados (funcionalidad futura)

# Aumentar tiempo de espera
wshot https://sitio.com --device desktop --wait-time 15
```

## 🔄 Verificación Completa del Sistema

Si tienes múltiples problemas o no sabes cuál es la causa:

### Paso 1: Diagnóstico básico
```bash
# Verificar versiones
python3 --version
pip --version

# Verificar instalación de wshot
wshot --version
wshot --help
```

### Paso 2: Test de instalación
```bash
# Ejecutar script de verificación
python test_installation.py
```

### Paso 3: Reinstalación completa
```bash
# Desinstalar completamente
pip uninstall wshot playwright

# Limpiar cache
pip cache purge

# Reinstalar desde cero
pip install git+https://github.com/DanielMartinezSebastian/wshot.git
playwright install chromium
```

### Paso 4: Prueba funcional
```bash
# Probar con sitio simple
wshot https://example.com --device desktop

# Si funciona, probar con sitio objetivo
wshot https://tu-sitio.com --device desktop
```

## 📊 Diagnóstico de Problemas

### Generar logs detallados
```bash
# Ejecutar con logs detallados y guardar en archivo
wshot https://sitio.com --device desktop 2>&1 | tee error.log

# Revisar el archivo error.log para encontrar la causa
cat error.log
```

### Información del sistema
```bash
# Linux
cat /etc/os-release
uname -a

# macOS
sw_vers
system_profiler SPSoftwareDataType

# Windows (PowerShell)
Get-ComputerInfo
```

## 🆘 Obtener Ayuda Adicional

Si ninguna solución funciona:

### 1. Recopilar información
- Salida de `python test_installation.py`
- Contenido de `error.log`
- Información del sistema operativo
- Comando exacto que estabas ejecutando
- URL del sitio web (si es público)

### 2. Abrir un issue en GitHub
1. Ir a https://github.com/DanielMartinezSebastian/wshot/issues
2. Crear un nuevo issue
3. Usar la plantilla de bug report
4. Incluir toda la información recopilada

### 3. Incluir en el issue
```
**Sistema Operativo:** [Ubuntu 22.04 / macOS 13 / Windows 11]
**Versión de Python:** [salida de python3 --version]
**Comando ejecutado:** [comando exacto que falló]
**Error obtenido:** [error completo]
**Salida del test:** [salida de python test_installation.py]
```

## 🔧 Soluciones Rápidas por Síntoma

| Síntoma | Solución Rápida |
|---------|----------------|
| **Capturas en negro** | `wshot URL --device desktop --wait-time 10` |
| **"playwright not found"** | `pip install playwright && playwright install chromium` |
| **Librerías faltantes** | Instalar dependencias del sistema según distribución |
| **URL no responde** | Verificar conectividad: `curl -I URL` |
| **Error de permisos** | Usar `--output-dir ~/Descargas` |
| **Instalación falla** | Crear entorno virtual y reinstalar |
| **Sitio carga lento** | Usar `--super` o `--wait-time 15` |
| **Pop-ups molestan** | Usar `--auto-dismiss` |

## 🏥 Casos Especiales

### Sitios con autenticación
```bash
# Actualmente no soportado directamente
# Workaround: hacer login manual y usar cookies del navegador
# (funcionalidad planificada para futuras versiones)
```

### Sitios con contenido dinámico
```bash
# Usar scroll suave para activar lazy loading
wshot https://sitio.com --device desktop --smooth-scroll --wait-time 7
```

### Sitios muy lentos
```bash
# Aumentar tiempo significativamente
wshot https://sitio-lento.com --device desktop --wait-time 20
```

### Sitios con muchos pop-ups
```bash
# Usar auto-dismiss y tiempo extra
wshot https://sitio-popups.com --device desktop --auto-dismiss --wait-time 5
```

---

> **Nota**: Si encuentras una solución a un problema no documentado aquí, considera contribuir al proyecto actualizando esta guía mediante un Pull Request.