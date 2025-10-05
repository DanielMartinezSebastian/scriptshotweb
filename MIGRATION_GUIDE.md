# Guía de Migración: ScriptShotWeb → Wshot

## 📦 Resumen de Cambios

Este documento describe la refactorización del proyecto de un script independiente a un paquete Python instalable con pip.

### Cambios Principales

1. **Nuevo nombre del comando**: `scriptshotweb` → `wshot`
2. **Instalación mediante pip**: Ahora se puede instalar con `pip install git+https://...`
3. **Estructura de paquete Python**: Código organizado en el directorio `wshot/`
4. **Compatibilidad legacy**: Los scripts originales (`scriptshotweb`, `scriptshotweb.sh`) se mantienen para retrocompatibilidad

## 🚀 Cómo Usar el Nuevo Paquete

### Instalación Recomendada (pip)

```bash
# Opción 1: Instalación global
pip install git+https://github.com/DanielMartinezSebastian/scriptshotweb.git

# Opción 2: Instalación en entorno virtual (recomendado)
python3 -m venv wshot-env
source wshot-env/bin/activate
pip install git+https://github.com/DanielMartinezSebastian/scriptshotweb.git

# Paso adicional: Instalar Chromium
playwright install chromium
```

### Uso del Comando `wshot`

Después de la instalación, el comando `wshot` estará disponible globalmente:

```bash
# Captura básica
wshot https://example.com --device desktop

# Captura completa en todos los dispositivos
wshot https://example.com -all

# Modo super (recomendado)
wshot https://example.com --super

# Ver ayuda
wshot --help
wshot --info
```

## 📁 Estructura del Proyecto

### Nueva Estructura

```
scriptshotweb/
├── wshot/                      # 🆕 Paquete Python principal
│   ├── __init__.py            # Definición del paquete
│   └── cli.py                 # Código principal (antes scriptshotweb)
├── setup.py                   # 🆕 Configuración de instalación
├── pyproject.toml             # 🆕 Configuración moderna del proyecto
├── MANIFEST.in                # 🆕 Archivos a incluir en distribución
├── test_installation.py       # 🆕 Script de verificación de instalación
├── requirements.txt           # Dependencias (sin cambios)
├── scriptshotweb.sh          # Script legacy (mantenido)
├── scriptshotweb             # Script Python legacy (mantenido)
├── install.sh                # Script de instalación legacy (mantenido)
└── README.md                 # Actualizado con nueva documentación
```

### Archivos Clave Nuevos

1. **wshot/__init__.py**: Define el paquete y exporta la función `main()`
2. **wshot/cli.py**: Contiene todo el código del CLI (antes `scriptshotweb`)
3. **setup.py**: Configuración para instalar con setuptools
4. **pyproject.toml**: Configuración moderna según PEP 517/518
5. **test_installation.py**: Script para verificar que la instalación funciona

## 🔄 Migración desde Versión Anterior

### Si Usabas los Scripts Legacy

Los scripts originales siguen funcionando sin cambios:

```bash
# Estos comandos siguen funcionando igual
./scriptshotweb.sh https://example.com -all
source .venv/bin/activate && python scriptshotweb https://example.com --device desktop
```

### Si Quieres Migrar a la Nueva Versión

1. **Desinstala la versión legacy** (opcional):
   ```bash
   # Los scripts legacy pueden coexistir con la nueva versión
   # No es necesario desinstalar nada
   ```

2. **Instala la nueva versión**:
   ```bash
   pip install git+https://github.com/DanielMartinezSebastian/scriptshotweb.git
   playwright install chromium
   ```

3. **Actualiza tus scripts**:
   ```bash
   # Antes
   ./scriptshotweb.sh https://example.com -all
   
   # Ahora
   wshot https://example.com -all
   ```

## ✅ Verificación de Instalación

Después de instalar, verifica que todo funciona:

```bash
# Verificación básica
wshot --help

# Verificación completa
python test_installation.py
```

El script `test_installation.py` verificará:
- ✅ Importación del paquete wshot
- ✅ Instalación de playwright
- ✅ Instalación de requests
- ✅ Navegador Chromium instalado y funcional

## 🎯 Ventajas del Nuevo Sistema

### Instalación con pip
- ✅ Instalación con un solo comando
- ✅ No requiere clonar el repositorio
- ✅ Gestión automática de dependencias
- ✅ Fácil actualización: `pip install --upgrade`
- ✅ Desinstalación limpia: `pip uninstall wshot`

### Comando Global
- ✅ Disponible desde cualquier directorio
- ✅ No necesitas activar entorno virtual manualmente
- ✅ Sintaxis más corta: `wshot` vs `./scriptshotweb.sh`
- ✅ Integración con herramientas de Python

### Desarrollo
- ✅ Instalación en modo editable: `pip install -e .`
- ✅ Cambios reflejados inmediatamente
- ✅ Mejor organización del código
- ✅ Facilita contribuciones al proyecto

## 📚 Documentación Actualizada

La documentación en README.md ha sido completamente actualizada con:

1. **Nueva sección de instalación** con instrucciones para pip
2. **Ejemplos actualizados** usando el comando `wshot`
3. **Guía de desarrollo** con la nueva estructura
4. **Sección de scripts legacy** para retrocompatibilidad
5. **Changelog** documentando la versión 1.0.0

## 🔧 Para Desarrolladores

### Instalación en Modo Desarrollo

```bash
git clone https://github.com/DanielMartinezSebastian/scriptshotweb.git
cd scriptshotweb
pip install -e .
playwright install chromium
```

### Estructura del Código

El código principal está en `wshot/cli.py` con las siguientes actualizaciones:

- ✅ Referencias a "ScriptShotWeb" cambiadas a "Wshot"
- ✅ Comandos en ejemplos actualizados de `scriptshotweb` a `wshot`
- ✅ Ayuda y documentación actualizadas
- ✅ Funcionalidad sin cambios (100% compatible)

## 🐛 Solución de Problemas

### Error: "wshot: command not found"

**Causa**: El paquete no está instalado o el PATH no incluye los scripts de Python.

**Solución**:
```bash
# Reinstalar el paquete
pip install git+https://github.com/DanielMartinezSebastian/scriptshotweb.git

# O usar directamente
python -m wshot.cli --help
```

### Error: "playwright: command not found"

**Causa**: Chromium no está instalado.

**Solución**:
```bash
playwright install chromium
```

### Los scripts legacy no funcionan

**Causa**: Se espera que el entorno virtual `.venv` exista.

**Solución**:
```bash
# Usar la instalación con pip en su lugar
pip install git+https://github.com/DanielMartinezSebastian/scriptshotweb.git

# O reinstalar usando scripts legacy
./install.sh
```

## 📝 Notas Adicionales

- ✅ El repositorio sigue llamándose `scriptshotweb` en GitHub
- ✅ El nombre del paquete Python es `wshot`
- ✅ El comando CLI es `wshot`
- ✅ Todos los scripts legacy se mantienen para compatibilidad
- ✅ No hay cambios en la funcionalidad, solo en la forma de instalación y uso

## 🎉 ¡Listo!

El proyecto ha sido exitosamente refactorizado para uso mediante pip. Ahora es más fácil de instalar, usar y mantener.

Para cualquier problema o pregunta, abre un issue en GitHub:
https://github.com/DanielMartinezSebastian/scriptshotweb/issues
