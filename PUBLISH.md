# 📦 Guía de Publicación PyPI - Wshot

Pasos para publicar Wshot en el repositorio oficial de PyPI.

## 🛠️ Requisitos Previos

Instalar herramientas de publicación:

```bash
pip install --upgrade build twine
```

## 🔍 Verificación Pre-Publicación

Ejecutar script de verificación:

```bash
python pre_publish_check.py
```

## 📦 Construcción del Paquete

### 1. Limpiar builds anteriores
```bash
rm -rf dist/ build/ *.egg-info/
```

### 2. Construir el paquete
```bash
python -m build
```

Esto genera:
- `dist/wshot-1.0.0.tar.gz` (código fuente)
- `dist/wshot-1.0.0-py3-none-any.whl` (wheel)

### 3. Verificar el paquete
```bash
python -m twine check dist/*
```

## 🧪 Prueba en TestPyPI (Recomendado)

### 1. Crear cuenta en TestPyPI
- Ir a https://test.pypi.org/account/register/
- Configurar API token en ~/.pypirc

### 2. Subir a TestPyPI
```bash
python -m twine upload --repository testpypi dist/*
```

### 3. Probar instalación desde TestPyPI
```bash
pip install --index-url https://test.pypi.org/simple/ wshot
```

### 4. Verificar funcionamiento
```bash
wshot --help
python test_installation.py
```

## 🚀 Publicación en PyPI Oficial

### 1. Crear cuenta en PyPI
- Ir a https://pypi.org/account/register/
- Configurar API token

### 2. Subir a PyPI
```bash
python -m twine upload dist/*
```

### 3. Verificar en PyPI
- Ir a https://pypi.org/project/wshot/
- Verificar que toda la información se muestra correctamente

### 4. Probar instalación oficial
```bash
pip install wshot
```

## 🔑 Configuración de API Tokens

Crear archivo `~/.pypirc`:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-tu-token-aqui

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-tu-token-testpypi-aqui
```

## 📝 Checklist Pre-Publicación

- [ ] ✅ Todos los tests pasan
- [ ] ✅ Documentación actualizada
- [ ] ✅ Versión actualizada en pyproject.toml
- [ ] ✅ CHANGELOG/ROADMAP actualizado
- [ ] ✅ README muestra instalación con `pip install wshot`
- [ ] ✅ URLs del repositorio son correctas
- [ ] ✅ Licencia incluida
- [ ] ✅ Todos los archivos en MANIFEST.in
- [ ] ✅ Script de verificación pasa
- [ ] ✅ Build local funciona
- [ ] ✅ TestPyPI funciona

## 🔄 Actualizaciones Futuras

Para nuevas versiones:

1. **Actualizar versión** en `pyproject.toml`
2. **Actualizar ROADMAP.md** con cambios
3. **Ejecutar verificaciones**:
   ```bash
   python pre_publish_check.py
   ```
4. **Construir y publicar**:
   ```bash
   rm -rf dist/
   python -m build
   python -m twine check dist/*
   python -m twine upload dist/*
   ```

## 🚨 Solución de Problemas

### Error: "File already exists"
- El nombre/versión ya existe en PyPI
- Incrementar versión en pyproject.toml

### Error: "Invalid credentials"
- Verificar API token en ~/.pypirc
- Regenerar token si es necesario

### Error: "Package validation failed"
- Ejecutar `python -m twine check dist/*`
- Revisar README.md formato markdown
- Verificar que LICENSE existe

### Error: "Missing files in distribution"
- Actualizar MANIFEST.in
- Verificar que todos los archivos están incluidos

## 📊 Post-Publicación

### Verificar instalación
```bash
pip install wshot
wshot --version
wshot --help
```

### Actualizar documentación
- README.md ✅ (ya actualizado)
- DOCS.md ✅ (ya actualizado)
- GitHub releases/tags

### Promoción
- Anunciar en redes sociales
- Actualizar portfolio/CV
- Documentar en blog personal

## 🎯 URLs Importantes

- **PyPI Oficial**: https://pypi.org/project/wshot/
- **TestPyPI**: https://test.pypi.org/project/wshot/
- **Documentación Build**: https://packaging.python.org/
- **Twine Docs**: https://twine.readthedocs.io/

---

¡Wshot estará disponible oficialmente en PyPI! 🎉