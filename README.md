# 📸 ScriptShotWeb

Una herramienta simplificada para capturar pantallas de sitios web en múltiples dispositivos y resoluciones, con capturas completas scrolleables.

## ✨ Características

- 🚀 **Sintaxis ultra-simple**: `scriptshotweb URL -all`
- 📱 **Múltiples dispositivos**: iPhone SE, iPhone 17, iPad, Desktop
- 🔄 **Doble captura**: Viewport + página completa scrolleable
- 🛡️ **Validación inteligente**: Verifica URLs antes de crear carpetas
- 📁 **Organización automática**: Carpetas por cliente y dispositivo
- ⚡ **Sin configuración manual**: Todo automatizado

## 🚀 Instalación

### Opción 1: Instalación Automática (Recomendada)
```bash
git clone https://github.com/DanielMartinezSebastian/scriptshotweb.git
cd scriptshotweb
./install.sh
```

### Opción 2: Instalación Manual
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

3. **Hacer ejecutable**:
```bash
chmod +x scriptshotweb.sh
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

## 📱 Dispositivos Disponibles

| Dispositivo | Dimensiones | Descripción |
|-------------|-------------|-------------|
| `mobile-se` | 375×667 | iPhone SE |
| `mobile-17` | 393×852 | iPhone 17 |
| `tablet` | 768×1024 | iPad |
| `desktop` | 1920×1080 | Desktop |

## 📂 Estructura de Salida

```
proyecto/
├── example/                    # Nombre extraído de la URL
│   ├── mobile-17/             # Solo carpetas solicitadas
│   │   ├── pagina-mobile-17-20231004_142958.png           # Viewport
│   │   └── pagina-mobile-17-completa-20231004_142958.png  # Página completa
│   └── tablet/
│       ├── pagina-tablet-20231004_142958.png
│       └── pagina-tablet-completa-20231004_142958.png
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

### Especificar cliente manualmente:
```bash
./scriptshotweb.sh https://example.com -all --cliente "MiCliente"
```

### Ver ayuda:
```bash
./scriptshotweb.sh --help
```

## 🎨 Tipos de Captura

### 📏 **Viewport (Normal)**
Captura el área visible del navegador según el tamaño del dispositivo.

### 📜 **Completa (Full Page)**
Captura toda la página incluyendo contenido scrolleable (`full_page=True`).

## 🔧 Requisitos

- Python 3.7+
- Playwright
- Requests
- Conexión a internet

## 📄 Ejemplos Prácticos

```bash
# Capturar página de contacto en todos los dispositivos
./scriptshotweb.sh https://miempresa.com/contacto -all

# Capturar solo en móvil iPhone 17
./scriptshotweb.sh https://mitienda.com/productos --device mobile-17

# Capturar página principal en tablet
./scriptshotweb.sh https://miblog.com --device tablet
```

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
```