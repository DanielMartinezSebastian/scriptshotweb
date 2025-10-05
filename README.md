# 📸 ScriptShotWeb

Una herramienta profesional para capturar pantallas de sitios web en múltiples dispositivos y resoluciones, optimizada para sitios modernos con animaciones y contenido dinámico.

## ✨ Características

- 🚀 **Sintaxis ultra-simple**: `scriptshotweb URL -all`
- 📱 **Múltiples dispositivos**: iPhone SE, iPhone 17, iPad, Desktop
- 🔄 **Doble captura**: Viewport + página completa scrolleable
- 🛡️ **Validación inteligente**: Verifica URLs antes de crear carpetas
- 📁 **Organización automática**: Carpetas por cliente y dispositivo
- ⚡ **Sin configuración manual**: Todo automatizado
- 📂 **Capturas organizadas**: Guarda en ./capturas/ del proyecto por defecto
- ⏳ **Control de animaciones**: Tiempo de espera configurable para animaciones (3s por defecto)
- 📜 **Scroll inteligente**: Scroll suave para disparar animaciones basadas en scroll
- 🤖 **Cierre automático de pop-ups**: Detecta y cierra banners de cookies y avisos automáticamente
- � **Extracción OpenGraph**: Obtiene metadatos og:* y descarga imágenes sociales
- �🚀 **Modo Super**: Captura optimizada completa con un solo comando
- 📖 **Ayuda completa**: Sistema de ayuda extensivo con `--help` e `--info`

## 🚩 Próximas Features

- [x] ~~Realizar captura completa de la url navegando primero hasta abajo para disparar animaciones basadas en scroll~~ ✅ **COMPLETADO**
- [x] ~~Control de tiempo de espera para animaciones~~ ✅ **COMPLETADO**
- [x] ~~Modo super para captura completa optimizada~~ ✅ **COMPLETADO**
- [x] ~~Alojar las capturas dentro de una carpeta general como downloads o similar en lugar de simplemente en la carpeta del script~~ ✅ **COMPLETADO**
- [ ] Refactorizar para homogeneizar uso de idioma castellano vs ingles
- [ ] Obtener capturas en webp optimizado
- [ ] Capturar webs completas navegando por todos los links bajo ese dominio para obtener toda la web
- [ ] Scrapear contenido en formato .md
- [ ] Obtener todo el contenido media que exista en la url objetivo
## 🚀 Instalación

### Opción 1: Instalación Automática (Recomendada) ⭐

El nuevo instalador mejorado maneja automáticamente errores y proporciona instrucciones claras:

```bash
git clone https://github.com/DanielMartinezSebastian/scriptshotweb.git
cd scriptshotweb
./install.sh
```

**Características del nuevo instalador:**
- ✅ Instalación paso a paso con mensajes claros
- ✅ Solo instala Chromium (más rápido y ligero)
- ✅ Manejo inteligente de errores sin detener el proceso
- ✅ Instrucciones específicas para cada distribución Linux
- ✅ No requiere sudo durante la instalación inicial

### Verificar instalación

Después de instalar, verifica que todo funcione correctamente:

```bash
./check.sh
```

Este script verifica:
- Python y entorno virtual
- Dependencias Python (playwright, requests)
- Navegador Chromium
- Dependencias del sistema
- Realiza un test funcional básico

### Instalar dependencias del sistema (si es necesario)

Si `check.sh` reporta dependencias faltantes, ejecuta:

```bash
sudo ./install-deps.sh
```

Este script detecta automáticamente tu distribución (Ubuntu, Debian, Fedora, Arch) e instala las librerías necesarias.

### Opción 2: Instalación Manual

Si prefieres más control:

1. **Clonar repositorio**:
```bash
git clone https://github.com/DanielMartinezSebastian/scriptshotweb.git
cd scriptshotweb
```

2. **Configurar entorno virtual**:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

3. **Instalar dependencias del sistema** (Ubuntu/Debian):
```bash
sudo apt install -y libnss3 libnspr4 libatk1.0-0 libatk-bridge2.0-0 \
  libcups2 libdrm2 libxkbcommon0 libxcomposite1 libxdamage1 libxfixes3 \
  libxrandr2 libgbm1 libpango-1.0-0 libcairo2 libasound2
```

4. **Hacer ejecutables**:
```bash
chmod +x scriptshotweb.sh scriptshotweb
```

5. **Verificar**:
```bash
./check.sh
```

## 🎯 Uso Básico

### Capturar todos los dispositivos:
```bash
./scriptshotweb.sh https://example.com -all
```

### Capturar dispositivo específico:
```bash
./scriptshotweb.sh https://example.com --device mobile-17
./scriptshotweb.sh https://example.com --device tablet
./scriptshotweb.sh https://example.com --device desktop
```

### 🚀 Modo Super (Recomendado para sitios complejos):
```bash
./scriptshotweb.sh https://example.com --super
# Activa automáticamente: todos los dispositivos + scroll suave + tiempo optimizado (2s)
```

### ⚙️ Opciones avanzadas:
```bash
# Con tiempo de espera personalizado para animaciones
./scriptshotweb.sh https://example.com --device desktop --wait-time 7

# Con scroll suave para disparar animaciones basadas en scroll  
./scriptshotweb.sh https://example.com -all --smooth-scroll

# Cerrar automáticamente banners de cookies y pop-ups
./scriptshotweb.sh https://example.com --device desktop --auto-dismiss

# Extraer metadatos OpenGraph (og:title, og:description, og:image, etc.)
./scriptshotweb.sh https://example.com --device desktop --open-graph
# O usar el alias corto:
./scriptshotweb.sh https://example.com --device desktop --og

# Abrir explorador de archivos automáticamente al finalizar
./scriptshotweb.sh https://example.com --super --open

# Combinando opciones (recomendado para sitios con cookies)
./scriptshotweb.sh https://example.com --device tablet --wait-time 4 --smooth-scroll --auto-dismiss --og --open
```

### 📖 Ver ayuda:
```bash
./scriptshotweb.sh --help      # Ayuda estándar
./scriptshotweb.sh --info      # Guía completa con ejemplos
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
- 📁 `./capturas/` (carpeta en el directorio del proyecto)
- 📁 O ruta personalizada con `--output-dir ~/Pictures/ScriptShotWeb`

```
scriptshotweb/
├── capturas/
│   └── example/                    # Nombre extraído de la URL
│       ├── mobile-17/             # Solo carpetas solicitadas
│       │   ├── pagina-mobile-17-20231004_142958.png           # Viewport
│       │   └── pagina-mobile-17-completa-20231004_142958.png  # Página completa
│       ├── tablet/
│       │   ├── pagina-tablet-20231004_142958.png
│       │   └── pagina-tablet-completa-20231004_142958.png
│       └── opengraph/             # Metadatos OpenGraph (si se usa --og o --all)
│           ├── opengraph-20231004_142958.json     # Todos los metadatos
│           └── og-image-20231004_142958.jpg       # Imagen social descargada
└── scriptshotweb
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

ScriptShotWeb verifica automáticamente que las URLs sean válidas antes de proceder:

```bash
# ✅ URL válida
./scriptshotweb.sh https://google.com -all
# 🔍 Validando URL...
# ✅ URL válida (Status: 200)
# 📁 Creando capturas...

# ❌ URL inexistente
./scriptshotweb.sh https://sitio-que-no-existe.com -all
# 🔍 Validando URL...
# ❌ Error: La URL no responde
# ❌ No se crean carpetas
```

## ⚙️ Opciones Avanzadas

### Todas las opciones disponibles:
```bash
# Especificar cliente manualmente:
./scriptshotweb.sh https://example.com -all --cliente "MiCliente"

# Control de tiempo de espera para animaciones (default: 3 segundos):
./scriptshotweb.sh https://example.com --device desktop --wait-time 5

# Scroll suave para disparar animaciones basadas en scroll:
./scriptshotweb.sh https://example.com -all --smooth-scroll

# Modo super (combina lo mejor de todo):
./scriptshotweb.sh https://example.com --super
# Equivale a: -all + --smooth-scroll + --wait-time 2
```

### 📖 Sistema de ayuda:
```bash
./scriptshotweb.sh --help      # Ayuda rápida con todas las opciones
./scriptshotweb.sh --info      # Guía completa con ejemplos detallados
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

## ✨ Nuevas Características (v2.0)

### 🤖 **Cierre Automático de Pop-ups (NUEVO en v2.4)**
```bash
# Cerrar automáticamente banners de cookies, avisos GDPR y otros pop-ups
./scriptshotweb.sh https://site.com --device desktop --auto-dismiss

# Combinar con otras opciones para capturas perfectas
./scriptshotweb.sh https://site.com --super --auto-dismiss
```

**¿Qué hace?**
- 🍪 Detecta y cierra automáticamente banners de cookies
- 📋 Cierra avisos de privacidad y consentimiento GDPR
- 🚫 Elimina pop-ups que bloquean la vista de la página
- 🌍 Soporte multiidioma (español, inglés, francés, alemán, italiano, portugués)
- 🎯 Compatible con frameworks populares: OneTrust, Cookiebot, Quantcast, TrustArc, Osano

**Ideal para:**
- Sitios con banners de cookies molestos (Google, Facebook, etc.)
- Páginas con avisos GDPR obligatorios
- Sitios con pop-ups de marketing o suscripciones
- Auditorías visuales sin obstrucciones
- Capturas profesionales para presentaciones

**Selectores detectados:**
- Botones: "Aceptar", "Accept", "Accepter", "Akzeptieren", "Accetta", "Aceitar"
- Clases comunes: `.cookie-consent`, `.gdpr-accept`, `.cc-allow`
- Frameworks: OneTrust, Cookiebot, Cookie Consent, Quantcast, TrustArc, Osano
- Atributos ARIA: `aria-label="Accept"`, `aria-label="Close"`

### 📊 **Extracción de Metadatos OpenGraph (NUEVO en v2.5)**
```bash
# Extraer metadatos OpenGraph de cualquier página
./scriptshotweb.sh https://site.com --device desktop --open-graph
# O usar el alias corto:
./scriptshotweb.sh https://site.com --device desktop --og

# Se activa automáticamente con --all y --super
./scriptshotweb.sh https://site.com --all  # ← OpenGraph incluido
./scriptshotweb.sh https://site.com --super  # ← OpenGraph incluido
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

**Archivos generados:**
```
capturas/
└── [cliente]/
    └── opengraph/
        ├── opengraph-20241005_143025.json  ← Todos los metadatos
        └── og-image-20241005_143025.jpg    ← Imagen social descargada
```

**Ejemplo de JSON generado:**
```json
{
  "title": "Mi Sitio Web Increíble",
  "description": "Descripción optimizada para compartir en redes sociales",
  "image": "https://example.com/social-image.jpg",
  "url": "https://example.com",
  "type": "website",
  "site_name": "Example",
  "twitter_card": "summary_large_image",
  "extracted_at": "2024-10-05T14:30:25",
  "source_url": "https://example.com",
  "image_local_path": "/path/to/og-image.jpg"
}
```

**Ideal para:**
- 🔍 Auditorías SEO completas
- 📱 Verificar optimización para redes sociales
- 🎨 Revisar imágenes compartidas (Facebook, Twitter, LinkedIn)
- 📊 Análisis de contenido y metadatos
- 🚀 Testing de Open Graph antes de publicar

### ⏳ **Control de Animaciones**
```bash
# Tiempo de espera personalizado para que carguen animaciones (default: 3s)
./scriptshotweb.sh https://site.com --wait-time 5
```
Perfecto para sitios con animaciones CSS, JavaScript o contenido que se carga con delay.

### 📜 **Scroll Suave Inteligente**
```bash
# Scroll gradual para disparar animaciones basadas en scroll
./scriptshotweb.sh https://site.com --smooth-scroll
```
Ideal para:
- Sitios con **lazy loading**
- Efectos **parallax**
- Animaciones activadas por **intersection observer**
- Contenido que aparece al hacer scroll

### 🚀 **Modo Super (Todo-en-Uno)**
```bash
# Un solo comando para captura completa optimizada
./scriptshotweb.sh https://site.com --super
```
**Activa automáticamente:**
- ✅ Todos los dispositivos (`-all`)
- ✅ Scroll suave (`--smooth-scroll`)
- ✅ Extracción OpenGraph (`--open-graph`)
- ✅ Tiempo optimizado (`--wait-time 2`)

**Recomendado para:**
- Sitios complejos con animaciones
- Auditorías completas (capturas + metadatos)
- Sitios modernos con efectos avanzados

### 📖 **Sistema de Ayuda Extendido**
```bash
./scriptshotweb.sh --help      # Ayuda rápida
./scriptshotweb.sh --info      # Guía completa con ejemplos
```

### 📂 **Abrir Explorador de Archivos Automáticamente**
```bash
# Abrir explorador al finalizar (multiplataforma)
./scriptshotweb.sh https://site.com --super --open

# En Windows abre Explorer
# En macOS abre Finder  
# En Linux detecta tu gestor: Dolphin (KDE), Nautilus (GNOME), Thunar (XFCE), etc.
```
**Detecta automáticamente tu sistema operativo y gestor de archivos:**
- ✅ Windows: Explorer
- ✅ macOS: Finder
- ✅ Linux: xdg-open (detecta Dolphin, Nautilus, Thunar, Nemo, Caja, PCManFM, etc.)

### 📂 **Ubicación de Archivos**
```bash
# Por defecto guarda en ./capturas/ dentro del proyecto
./scriptshotweb.sh https://site.com --super

# Especificar ubicación personalizada (ej: Pictures o Downloads)
./scriptshotweb.sh https://site.com --super --output-dir ~/Pictures/ScriptShotWeb
./scriptshotweb.sh https://site.com --super --output-dir ~/Downloads/Capturas
```
**Beneficios:**
- ✅ Mantiene las capturas organizadas en el proyecto
- ✅ Fácil de encontrar y gestionar
- ✅ Opción de mover a Pictures/Downloads si lo prefieres
- ✅ Compatible con .gitignore para no subir capturas al repo

## 🔧 Requisitos

- Python 3.7+
- Playwright
- Requests
- Conexión a internet

## 📄 Ejemplos Prácticos

```bash
# Capturar página de contacto en todos los dispositivos (básico)
./scriptshotweb.sh https://miempresa.com/contacto -all

# Capturar solo en móvil iPhone 17
./scriptshotweb.sh https://mitienda.com/productos --device mobile-17

# Capturar página principal en tablet con tiempo de espera extra
./scriptshotweb.sh https://miblog.com --device tablet --wait-time 6

# Sitio con banner de cookies - cerrar automáticamente
./scriptshotweb.sh https://google.com --device desktop --auto-dismiss

# Extraer solo metadatos OpenGraph sin capturas
./scriptshotweb.sh https://miempresa.com --device desktop --og

# Sitio con muchas animaciones - usar modo super y abrir explorador
./scriptshotweb.sh https://sitio-animado.com --super --open

# Sitio con lazy loading, cookies y OpenGraph - combinación completa
./scriptshotweb.sh https://sitio-parallax.com -all --smooth-scroll --auto-dismiss

# Auditoría SEO completa: capturas + metadatos OpenGraph
./scriptshotweb.sh https://cliente-importante.com --super --cliente "ClienteVIP"

# Guardar en ubicación personalizada y abrir automáticamente
./scriptshotweb.sh https://proyecto.com --super --output-dir ~/Proyectos/AuditoriasWeb --open
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
scriptshotweb/
├── scriptshotweb.sh      # Script principal (wrapper)
├── scriptshotweb         # Script Python core
├── install.sh           # Script de instalación automática
├── requirements.txt     # Dependencias Python
├── .venv/              # Entorno virtual
├── .gitignore          # Archivos a ignorar en Git
├── LICENSE             # Licencia MIT
└── README.md           # Este archivo
```

### Ejecutar en modo desarrollo:
```bash
source .venv/bin/activate
python scriptshotweb https://example.com --device mobile-17

# O usando el modo super para pruebas completas:
python scriptshotweb https://example.com --super
```

---

## 🎉 Changelog

### v2.5 - Extracción de Metadatos OpenGraph 📊
- ✅ Nuevo parámetro `--open-graph` (alias `--og`) para extraer metadatos
- ✅ Extracción completa de todos los metadatos og:* (title, description, image, etc.)
- ✅ Descarga automática de imágenes og:image
- ✅ Soporte para Twitter Card metadata complementario
- ✅ Generación de archivos JSON estructurados con toda la información
- ✅ Se activa automáticamente con `--all` y `--super`
- ✅ Carpeta dedicada `opengraph/` para organizar archivos
- ✅ Ideal para auditorías SEO y análisis de redes sociales

### v2.4 - Cierre Automático de Pop-ups 🤖
- ✅ Nuevo parámetro `--auto-dismiss` para cerrar automáticamente pop-ups
- ✅ Detección inteligente de banners de cookies en múltiples idiomas
- ✅ Soporte para frameworks populares (OneTrust, Cookiebot, Quantcast, etc.)
- ✅ Selectores ARIA y clases comunes incluidos
- ✅ Ideal para sitios como Google, Facebook y otros con avisos GDPR

### v2.3 - Apertura Automática del Explorador de Archivos
- ✅ Nuevo parámetro `--open` para abrir explorador automáticamente
- ✅ Detección inteligente multiplataforma (Windows, macOS, Linux)
- ✅ Soporte para gestores de archivos Linux (Dolphin, Nautilus, Thunar, etc.)
- ✅ Usa xdg-open en Linux para detectar automáticamente el gestor predeterminado

### v2.2 - Mejoras en el Proceso de Instalación
- ✅ Nuevo instalador mejorado con mejor manejo de errores
- ✅ Script de verificación completo (`check.sh`)
- ✅ Script auxiliar para dependencias del sistema (`install-deps.sh`)
- ✅ Instalación optimizada (solo Chromium por defecto)
- ✅ Instrucciones claras para múltiples distribuciones Linux
- ✅ Documentación de troubleshooting mejorada

### v2.1 - Mejoras de Organización
- ✅ Organización en carpeta ./capturas/ por defecto
- ✅ Soporte para directorios personalizados (`--output-dir`)
- ✅ Optimización del modo super (2s en lugar de 5s)
- ✅ Mejoras en velocidad de scroll (0.08s por paso)

### v2.0 - Nuevas Características
- ✅ Control de tiempo de espera para animaciones (`--wait-time`)
- ✅ Scroll suave para disparar animaciones (`--smooth-scroll`) 
- ✅ Modo super optimizado (`--super`)
- ✅ Sistema de ayuda extendido (`--help`, `--info`)
- ✅ Mejor manejo de sitios modernos con animaciones

### v1.0 - Funcionalidades Base
- ✅ Capturas multi-dispositivo
- ✅ Validación inteligente de URLs
- ✅ Organización automática de archivos
- ✅ Capturas viewport y página completa

---

## 🔧 Troubleshooting (Solución de Problemas)

### Problema: "libicudata.so.66 not found" u otras librerías faltantes

**Síntoma:** Error al ejecutar capturas mencionando librerías `.so` faltantes.

**Solución:**
```bash
# Opción 1: Script automático (recomendado)
sudo ./install-deps.sh

# Opción 2: Manual para Ubuntu/Debian
sudo apt update
sudo apt install -y libnss3 libnspr4 libatk1.0-0 libatk-bridge2.0-0 \
  libcups2 libdrm2 libxkbcommon0 libxcomposite1 libxdamage1 \
  libxfixes3 libxrandr2 libgbm1 libpango-1.0-0 libcairo2 libasound2

# Opción 3: Manual para Fedora
sudo dnf install -y nss nspr atk at-spi2-atk cups-libs libdrm \
  libxkbcommon libXcomposite libXdamage libXrandr libgbm pango cairo alsa-lib
```

### Problema: "playwright: command not found"

**Síntoma:** No se encuentra el comando playwright.

**Solución:**
```bash
# Activar entorno virtual
source .venv/bin/activate

# Reinstalar playwright
pip install playwright
playwright install chromium
```

### Problema: "Python3 not found"

**Síntoma:** Python3 no está instalado.

**Solución:**
```bash
# Ubuntu/Debian
sudo apt install python3 python3-venv python3-pip

# Fedora
sudo dnf install python3 python3-pip

# Arch Linux
sudo pacman -S python python-pip
```

### Problema: "Entorno virtual no se puede crear"

**Síntoma:** Error al ejecutar `python3 -m venv .venv`.

**Solución:**
```bash
# Ubuntu/Debian - instalar módulo venv
sudo apt install python3-venv

# Luego reintentar
./install.sh
```

### Problema: Las capturas salen en negro o vacías

**Síntoma:** Las imágenes capturadas están en negro o no muestran contenido.

**Solución:**
```bash
# 1. Verificar instalación
./check.sh

# 2. Aumentar tiempo de espera
./scriptshotweb.sh https://sitio.com --device desktop --wait-time 10

# 3. Usar modo super con scroll suave
./scriptshotweb.sh https://sitio.com --super
```

### Problema: "OS not officially supported by Playwright"

**Síntoma:** Advertencia sobre sistema operativo no soportado.

**Solución:**
Esta es solo una advertencia. Playwright intentará usar una versión compatible. Si funciona, puedes ignorarla. Si tienes problemas:

1. Asegúrate de tener todas las dependencias: `sudo ./install-deps.sh`
2. Verifica con: `./check.sh`
3. Si persiste, considera actualizar tu distribución Linux

### Problema: Permisos denegados al ejecutar scripts

**Síntoma:** "Permission denied" al ejecutar `./scriptshotweb.sh`.

**Solución:**
```bash
chmod +x scriptshotweb.sh scriptshotweb check.sh install-deps.sh
```

### Problema: URL válida pero no captura

**Síntoma:** La URL responde pero las capturas fallan.

**Causas comunes:**
1. **Sitio con captcha o protección anti-bot**
2. **Contenido dinámico que tarda en cargar**
3. **Sitio requiere JavaScript específico**

**Soluciones:**
```bash
# Aumentar tiempo de espera
./scriptshotweb.sh https://sitio.com --device desktop --wait-time 15

# Usar scroll suave
./scriptshotweb.sh https://sitio.com --device desktop --smooth-scroll

# Probar con modo super
./scriptshotweb.sh https://sitio.com --super
```

### Verificación completa del sistema

Si tienes múltiples problemas, ejecuta una verificación completa:

```bash
# 1. Verificar estado actual
./check.sh

# 2. Reinstalar desde cero
rm -rf .venv
./install.sh

# 3. Instalar dependencias del sistema
sudo ./install-deps.sh

# 4. Verificar nuevamente
./check.sh

# 5. Prueba funcional
./scriptshotweb.sh https://example.com --device desktop
```

### Obtener ayuda adicional

Si ninguna solución funciona:

1. **Revisa los logs detallados**:
   ```bash
   ./scriptshotweb.sh https://sitio.com --device desktop 2>&1 | tee error.log
   ```

2. **Información del sistema**:
   ```bash
   python3 --version
   lsb_release -a  # o cat /etc/os-release
   uname -a
   ```

3. **Abre un issue en GitHub** con:
   - Salida de `./check.sh`
   - Contenido de `error.log`
   - Información del sistema
   - Comando que estabas ejecutando

---

## 📚 Scripts Disponibles

| Script | Propósito | Requiere sudo |
|--------|-----------|---------------|
| `install.sh` | Instalación completa del proyecto | No* |
| `install-deps.sh` | Instalar dependencias del sistema | Sí |
| `check.sh` | Verificar instalación y funcionalidad | No |
| `scriptshotweb.sh` | Ejecutar capturas (wrapper) | No |
| `scriptshotweb` | Script principal Python | No |

*El instalador puede pedir sudo solo para dependencias del sistema, pero continúa sin ellas.

