# 📸 Wshot

Una herramienta profesional para capturar pantallas de sitios web en múltiples dispositivos y resoluciones, optimizada para sitios modernos con animaciones y contenido dinámico.

## ✨ Características

- 🚀 **Sintaxis ultra-simple**: `wshot URL -all`
- 📱 **Múltiples dispositivos**: iPhone SE, iPhone 17, iPad, Desktop
- 🔄 **Doble captura**: Viewport + página completa scrolleable
- 🛡️ **Validación inteligente**: Verifica URLs antes de crear carpetas
- 📁 **Organización automática**: Carpetas por cliente y dispositivo
- ⚡ **Sin configuración manual**: Todo automatizado
- 📂 **Capturas organizadas**: Guarda en ./capturas/ del proyecto por defecto
- ⏳ **Control de animaciones**: Tiempo de espera configurable para animaciones (3s por defecto)
- 📜 **Scroll inteligente**: Scroll suave para disparar animaciones basadas en scroll
- 🤖 **Cierre automático de pop-ups**: Detecta y cierra banners de cookies y avisos automáticamente
- 📊 **Extracción OpenGraph**: Obtiene metadatos og:* y descarga imágenes sociales
- 🚀 **Modo Super**: Captura optimizada completa con un solo comando
- 📖 **Ayuda completa**: Sistema de ayuda extensivo con `--help` e `--info`

## 🚩 Próximas Features

- [x] ~~Realizar captura completa de la url navegando primero hasta abajo para disparar animaciones basadas en scroll~~ ✅ **COMPLETADO**
- [x] ~~Control de tiempo de espera para animaciones~~ ✅ **COMPLETADO**
- [x] ~~Modo super para captura completa optimizada~~ ✅ **COMPLETADO**
- [x] ~~Alojar las capturas dentro de una carpeta general como downloads o similar en lugar de simplemente en la carpeta del script~~ ✅ **COMPLETADO**
- [x] ~~Refactorización para uso mediante pip~~ ✅ **COMPLETADO**
- [ ] Refactorizar para homogeneizar uso de idioma castellano vs ingles
- [ ] Obtener capturas en webp optimizado
- [ ] Capturar webs completas navegando por todos los links bajo ese dominio para obtener toda la web
- [ ] Scrapear contenido en formato .md
- [ ] Obtener todo el contenido media que exista en la url objetivo

## 🚀 Instalación

### Instalación mediante pip (Recomendada) ⭐

Instala wshot como un paquete Python global o en un entorno virtual:

**Para la mayoría de sistemas:**
```bash
# Instalación desde el repositorio con pip
pip install git+https://github.com/DanielMartinezSebastian/wshot.git

# O en un entorno virtual (recomendado)
python3 -m venv wshot-env
source wshot-env/bin/activate  # En Windows: wshot-env\Scripts\activate
pip install git+https://github.com/DanielMartinezSebastian/wshot.git
```

**Para Arch Linux (recomendado - pipx):**
```bash
# Instalar pipx si no lo tienes
sudo pacman -S python-pipx

# Instalar wshot globalmente con pipx
pipx install git+https://github.com/DanielMartinezSebastian/wshot.git

# Instalar Chromium
~/.local/share/pipx/venvs/wshot/bin/playwright install chromium
```

**Para Arch Linux (alternativa - entorno virtual):**
```bash
# Crear entorno virtual
python3 -m venv ~/.wshot-env
source ~/.wshot-env/bin/activate
pip install git+https://github.com/DanielMartinezSebastian/wshot.git
playwright install chromium

# Crear alias en tu .zshrc o .bashrc para uso global
echo 'alias wshot="~/.wshot-env/bin/wshot"' >> ~/.zshrc
source ~/.zshrc
```

**Paso adicional necesario:**

Después de instalar con pip, debes instalar el navegador Chromium de Playwright:

```bash
# Si instalaste con pip normal
playwright install chromium

# Si instalaste con pipx en Arch Linux
~/.local/share/pipx/venvs/wshot/bin/playwright install chromium
```

**Verificar instalación:**

Puedes verificar que todo está instalado correctamente ejecutando:

```bash
# Verificación básica
wshot --help

# Verificación completa con script de test
python test_installation.py
```

**Dependencias del sistema (opcional):**

Si encuentras errores relacionados con librerías del sistema faltantes, instálalas según tu distribución:

```bash
# Ubuntu/Debian
sudo apt install -y libnss3 libnspr4 libatk1.0-0 libatk-bridge2.0-0 \
  libcups2 libdrm2 libxkbcommon0 libxcomposite1 libxdamage1 libxfixes3 \
  libxrandr2 libgbm1 libpango-1.0-0 libcairo2 libasound2

# Fedora
sudo dnf install -y nss nspr atk at-spi2-atk cups-libs libdrm libxkbcommon \
  libxcomposite libxdamage libXrandr mesa-libgbm pango cairo alsa-lib

# Arch Linux
sudo pacman -S nss nspr atk at-spi2-atk cups libdrm libxkbcommon \
  libxcomposite libxdamage libxrandr mesa pango cairo alsa-lib
```

### Instalación desde el repositorio (Desarrollo)

Si quieres desarrollar o contribuir al proyecto:

```bash
git clone https://github.com/DanielMartinezSebastian/wshot.git
cd wshot

# Instalar en modo desarrollo
pip install -e .
playwright install chromium
```

## 🎯 Uso Básico

### Capturar todos los dispositivos:
```bash
wshot https://example.com -all
```

### Capturar dispositivo específico:
```bash
wshot https://example.com --device mobile-17
wshot https://example.com --device tablet
wshot https://example.com --device desktop
```

### 🚀 Modo Super (Recomendado para sitios complejos):
```bash
wshot https://example.com --super
# Activa automáticamente: todos los dispositivos + scroll suave + tiempo optimizado (2s) + OpenGraph
```

### ⚙️ Opciones avanzadas:
```bash
# Con tiempo de espera personalizado para animaciones
wshot https://example.com --device desktop --wait-time 7

# Con scroll suave para disparar animaciones basadas en scroll  
wshot https://example.com -all --smooth-scroll

# Cerrar automáticamente banners de cookies y pop-ups
wshot https://example.com --device desktop --auto-dismiss

# Extraer metadatos OpenGraph (og:title, og:description, og:image, etc.)
wshot https://example.com --device desktop --open-graph
# O usar el alias corto:
wshot https://example.com --device desktop --og

# Abrir explorador de archivos automáticamente al finalizar
wshot https://example.com --super --open

# Combinando opciones (recomendado para sitios con cookies)
wshot https://example.com --device tablet --wait-time 4 --smooth-scroll --auto-dismiss --og --open
```

### 📖 Ver ayuda:
```bash
wshot --help      # Ayuda estándar
wshot --info      # Guía completa con ejemplos
```

## 📱 Dispositivos Disponibles

| Dispositivo | Dimensiones | Descripción |
|-------------|-------------|-------------|
| `mobile-se` | 375×667 | iPhone SE |
| `mobile-17` | 393×852 | iPhone 17 |
| `tablet` | 768×1024 | iPad |
| `desktop` | 1920×1080 | Desktop |

## 📂 Estructura de Salida

**Ubicación por defecto:**
- 📁 `./capturas/` (carpeta en el directorio actual)
- 📁 O ruta personalizada con `--output-dir ~/Pictures/Wshot`

```
wshot/
├── capturas/
│   └── example/                    # Nombre extraído de la URL
│       ├── mobile-17/             # Solo carpetas solicitadas
│       │   ├── pagina-mobile-17-20241005_142958.png           # Viewport
│       │   └── pagina-mobile-17-completa-20241005_142958.png  # Página completa
│       ├── tablet/
│       │   ├── pagina-tablet-20241005_142958.png
│       │   └── pagina-tablet-completa-20241005_142958.png
│       └── opengraph/             # Metadatos OpenGraph (si se usa --og o --all)
│           ├── opengraph-20241005_142958.json     # Todos los metadatos
│           └── og-image-20241005_142958.jpg       # Imagen social descargada
└── wshot/
```

**Con `--all` o `--super` se crean todas las carpetas automáticamente:**
```
capturas/example/
├── mobile-se/
├── mobile-17/
├── tablet/
├── desktop/
└── opengraph/    ← Incluye JSON + imagen og:image
```

## 🛡️ Validación de URLs

Wshot verifica automáticamente que las URLs sean válidas antes de proceder:

```bash
# ✅ URL válida
wshot https://google.com -all
# 🔍 Validando URL...
# ✅ URL válida (Status: 200)
# 📁 Creando capturas...

# ❌ URL inexistente
wshot https://sitio-que-no-existe.com -all
# 🔍 Validando URL...
# ❌ Error: La URL no responde
# ❌ No se crean carpetas
```

## ⚙️ Opciones Avanzadas

### Todas las opciones disponibles:
```bash
# Especificar cliente manualmente:
wshot https://example.com -all --cliente "MiCliente"

# Control de tiempo de espera para animaciones (default: 3 segundos):
wshot https://example.com --device desktop --wait-time 5

# Scroll suave para disparar animaciones basadas en scroll:
wshot https://example.com -all --smooth-scroll

# Modo super (combina lo mejor de todo):
wshot https://example.com --super
# Equivale a: -all + --smooth-scroll + --open-graph + --wait-time 2
```

### 📖 Sistema de ayuda:
```bash
wshot --help      # Ayuda rápida con todas las opciones
wshot --info      # Guía completa con ejemplos detallados
```

### 🎛️ Lista completa de parámetros:
| Parámetro | Descripción | Ejemplo |
|-----------|-------------|---------|
| `URL` | URL del sitio web a capturar | `https://example.com` |
| `-all, --all-devices` | Capturar en todos los dispositivos | `-all` |
| `--device DEVICE` | Dispositivo específico | `--device mobile-17` |
| `--cliente NOMBRE` | Nombre personalizado del cliente | `--cliente "MiEmpresa"` |
| `--output-dir PATH` | Directorio personalizado de salida | `--output-dir ~/Proyectos` |
| `--wait-time SEGUNDOS` | Tiempo de espera para animaciones | `--wait-time 5` |
| `--smooth-scroll` | Scroll suave antes de captura completa | `--smooth-scroll` |
| `--auto-dismiss` | 🤖 Cerrar automáticamente banners de cookies y pop-ups | `--auto-dismiss` |
| `--open-graph, --og` | 📊 Extraer metadatos OpenGraph y descargar imagen social | `--og` |
| `--super` | 🚀 Modo completo optimizado (incluye OpenGraph) | `--super` |
| `--open` | 📂 Abrir explorador de archivos al finalizar | `--open` |
| `--help, -h` | Ayuda estándar | `--help` |
| `--info` | Guía completa extendida | `--info` |

## 🎨 Tipos de Captura

### 📏 **Viewport (Normal)**
Captura el área visible del navegador según el tamaño del dispositivo.

### 📜 **Completa (Full Page)**
Captura toda la página incluyendo contenido scrolleable (`full_page=True`).

## ✨ Características Destacadas

### 🤖 **Cierre Automático de Pop-ups**
```bash
# Cerrar automáticamente banners de cookies, avisos GDPR y otros pop-ups
wshot https://site.com --device desktop --auto-dismiss

# Combinar con otras opciones para capturas perfectas
wshot https://site.com --super --auto-dismiss
```

**¿Qué hace?**
- 🍪 Detecta y cierra automáticamente banners de cookies
- 📋 Cierra avisos de privacidad y consentimiento GDPR
- 🚫 Elimina pop-ups que bloquean la vista de la página
- 🌍 Soporte multiidioma (español, inglés, francés, alemán, italiano, portugués)
- 🎯 Compatible con frameworks populares: OneTrust, Cookiebot, Quantcast, TrustArc, Osano

### 📊 **Extracción de Metadatos OpenGraph**
```bash
# Extraer metadatos OpenGraph de cualquier página
wshot https://site.com --device desktop --open-graph
# O usar el alias corto:
wshot https://site.com --device desktop --og

# Se activa automáticamente con --all y --super
wshot https://site.com --all  # ← OpenGraph incluido
wshot https://site.com --super  # ← OpenGraph incluido
```

**¿Qué extrae?**
- 🏷️ **og:title** - Título para redes sociales
- 📝 **og:description** - Descripción optimizada
- 🖼️ **og:image** - Imagen social (descargada automáticamente)
- 🌐 **og:url** - URL canónica
- 🎯 **og:type** - Tipo de contenido (website, article, etc.)
- 📱 **og:site_name** - Nombre del sitio
- 🐦 **Twitter Card** - Metadatos de Twitter
- 📄 Y muchos más...

### ⏳ **Control de Animaciones**
```bash
# Tiempo de espera personalizado para que carguen animaciones (default: 3s)
wshot https://site.com --wait-time 5
```
Perfecto para sitios con animaciones CSS, JavaScript o contenido que se carga con delay.

### 📜 **Scroll Suave Inteligente**
```bash
# Scroll gradual para disparar animaciones basadas en scroll
wshot https://site.com --smooth-scroll
```
Ideal para:
- Sitios con **lazy loading**
- Efectos **parallax**
- Animaciones activadas por **intersection observer**
- Contenido que aparece al hacer scroll

### 🚀 **Modo Super (Todo-en-Uno)**
```bash
# Un solo comando para captura completa optimizada
wshot https://site.com --super
```
**Activa automáticamente:**
- ✅ Todos los dispositivos (`-all`)
- ✅ Scroll suave (`--smooth-scroll`)
- ✅ Extracción OpenGraph (`--open-graph`)
- ✅ Tiempo optimizado (`--wait-time 2`)

### 📂 **Abrir Explorador de Archivos Automáticamente**
```bash
# Abrir explorador al finalizar (multiplataforma)
wshot https://site.com --super --open

# En Windows abre Explorer
# En macOS abre Finder  
# En Linux detecta tu gestor: Dolphin (KDE), Nautilus (GNOME), Thunar (XFCE), etc.
```

## 🔧 Requisitos

- Python 3.8+
- Playwright (instalado automáticamente con pip)
- Requests (instalado automáticamente con pip)
- Conexión a internet

## 📄 Ejemplos Prácticos

```bash
# Capturar página de contacto en todos los dispositivos (básico)
wshot https://miempresa.com/contacto -all

# Capturar solo en móvil iPhone 17
wshot https://mitienda.com/productos --device mobile-17

# Capturar página principal en tablet con tiempo de espera extra
wshot https://miblog.com --device tablet --wait-time 6

# Sitio con banner de cookies - cerrar automáticamente
wshot https://google.com --device desktop --auto-dismiss

# Extraer solo metadatos OpenGraph sin capturas
wshot https://miempresa.com --device desktop --og

# Sitio con muchas animaciones - usar modo super y abrir explorador
wshot https://sitio-animado.com --super --open

# Sitio con lazy loading, cookies y OpenGraph - combinación completa
wshot https://sitio-parallax.com -all --smooth-scroll --auto-dismiss

# Auditoría SEO completa: capturas + metadatos OpenGraph
wshot https://cliente-importante.com --super --cliente "ClienteVIP"

# Guardar en ubicación personalizada y abrir automáticamente
wshot https://proyecto.com --super --output-dir ~/Proyectos/AuditoriasWeb --open
```

### 🎯 Casos de uso recomendados:

| Tipo de sitio | Comando recomendado | Razón |
|---------------|---------------------|-------|
| **Sitio estático simple** | `--device desktop` | Rápido y eficiente |
| **Sitio responsive** | `-all` | Ver en todos los dispositivos + OpenGraph |
| **Sitio con animaciones** | `--super` | Tiempo optimizado + scroll + OpenGraph |
| **Sitio con lazy loading** | `--smooth-scroll` | Activa el contenido diferido |
| **Sitio con cookies/GDPR** | `--auto-dismiss` | Cierra banners automáticamente |
| **Auditoría SEO** | `--super` | Capturas completas + metadatos OpenGraph |
| **Google, Facebook, etc.** | `--super --auto-dismiss` | Capturas limpias sin pop-ups + metadatos |
| **Auditoría completa** | `--super --auto-dismiss` | Captura exhaustiva sin obstrucciones + SEO |
| **Sitio lento** | `--wait-time 7` | Más tiempo para cargar |

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📜 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 🛠️ Desarrollo

### Estructura del proyecto:
```
wshot/
├── wshot/                   # Paquete Python principal
│   ├── __init__.py         # Módulo del paquete
│   └── cli.py              # Código principal CLI
├── pyproject.toml          # Configuración del proyecto (PEP 621)
├── MANIFEST.in             # Archivos incluidos en distribución
├── test_installation.py    # Script de verificación
├── .gitignore              # Archivos a ignorar en Git
├── LICENSE                 # Licencia MIT
└── README.md               # Este archivo
```

### Ejecutar en modo desarrollo:
```bash
# Instalar en modo editable
pip install -e .
playwright install chromium

# Ejecutar
wshot https://example.com --device mobile-17

# O usando el modo super para pruebas completas:
wshot https://example.com --super
```

## 🔧 Troubleshooting (Solución de Problemas)

### Problema: "libicudata.so.66 not found" u otras librerías faltantes

**Síntoma:** Error al ejecutar capturas mencionando librerías `.so` faltantes.

**Solución:**
```bash
# Ubuntu/Debian
sudo apt update && sudo apt install -y libnss3 libnspr4 libatk1.0-0 \
  libatk-bridge2.0-0 libcups2 libdrm2 libxkbcommon0 libxcomposite1 \
  libxdamage1 libxfixes3 libxrandr2 libgbm1 libpango-1.0-0 libcairo2 libasound2

# Fedora
sudo dnf install -y nss nspr atk at-spi2-atk cups-libs libdrm \
  libxkbcomposite libxdamage libXrandr libgbm pango cairo alsa-lib

# Arch Linux
sudo pacman -S nss nspr atk at-spi2-atk cups libdrm libxkbcommon \
  libxcomposite libxdamage libxrandr mesa pango cairo alsa-lib
```

### Problema: "playwright: command not found"

**Síntoma:** No se encuentra el comando playwright.

**Solución:**
```bash
# Reinstalar playwright
pip install playwright
playwright install chromium
```

### Problema: Las capturas salen en negro o vacías

**Síntoma:** Las imágenes capturadas están en negro o no muestran contenido.

**Solución:**
```bash
# 1. Verificar instalación
python test_installation.py

# 2. Aumentar tiempo de espera
wshot https://sitio.com --device desktop --wait-time 10

# 3. Usar modo super con scroll suave
wshot https://sitio.com --super
```

### Verificación completa del sistema

Si tienes múltiples problemas:

```bash
# 1. Verificar estado actual
python test_installation.py

# 2. Reinstalar desde cero
pip uninstall wshot
pip install git+https://github.com/DanielMartinezSebastian/wshot.git
playwright install chromium

# 3. Prueba funcional
wshot https://example.com --device desktop
```

### Obtener ayuda adicional

Si ninguna solución funciona:

1. **Revisa los logs detallados**:
   ```bash
   wshot https://sitio.com --device desktop 2>&1 | tee error.log
   ```

2. **Información del sistema**:
   ```bash
   python3 --version
   lsb_release -a  # o cat /etc/os-release
   ```

3. **Abre un issue en GitHub** con:
   - Salida de `python test_installation.py`
   - Contenido de `error.log`
   - Información del sistema
   - Comando que estabas ejecutando

---

## 🎉 Changelog

### v1.0.0 - Paquete pip production-ready 📦
- ✅ Proyecto refactorizado como paquete Python instalable
- ✅ Comando `wshot` disponible globalmente tras instalación pip
- ✅ Estructura limpia sin archivos legacy redundantes
- ✅ Configuración moderna con `pyproject.toml`
- ✅ Instalación simplificada: `pip install git+https://...`
- ✅ Script de verificación `test_installation.py`
- ✅ Compatible con desarrollo: `pip install -e .`

### Características principales incluidas:
- 📱 Capturas multi-dispositivo (iPhone SE, iPhone 17, iPad, Desktop)
- 🛡️ Validación inteligente de URLs
- 📁 Organización automática de archivos por cliente y dispositivo
- ⏳ Control de animaciones y tiempo de espera configurable
- 📜 Scroll suave para disparar animaciones basadas en scroll
- 🤖 Cierre automático de banners de cookies y pop-ups
- 📊 Extracción de metadatos OpenGraph con descarga de imágenes
- 🚀 Modo Super (all-devices + smooth-scroll + open-graph + optimizado)
- 📂 Apertura automática del explorador de archivos
- 📖 Sistema de ayuda extensivo (`--help` e `--info`)
- 🎨 Doble captura: viewport + página completa