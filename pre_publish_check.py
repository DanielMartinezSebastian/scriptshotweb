#!/usr/bin/env python3
"""
Script de verificación pre-publicación para wshot
Verifica que todo esté listo para publicar en PyPI
"""

import sys
import subprocess
import os
from pathlib import Path

def run_command(cmd, description):
    """Ejecuta un comando y verifica su salida"""
    print(f"🔍 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} - OK")
            return True
        else:
            print(f"❌ {description} - FALLO")
            print(f"Error: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ {description} - ERROR: {e}")
        return False

def check_file_exists(filepath, description):
    """Verifica que un archivo existe"""
    if Path(filepath).exists():
        print(f"✅ {description} - OK")
        return True
    else:
        print(f"❌ {description} - NO ENCONTRADO")
        return False

def main():
    print("🚀 Verificación pre-publicación de Wshot")
    print("=" * 50)
    
    checks_passed = 0
    total_checks = 0
    
    # Verificar archivos esenciales
    files_to_check = [
        ("README.md", "README principal"),
        ("LICENSE", "Archivo de licencia"),
        ("pyproject.toml", "Configuración del proyecto"),
        ("MANIFEST.in", "Manifest de distribución"),
        ("wshot/__init__.py", "Módulo principal"),
        ("wshot/cli.py", "CLI principal"),
        ("DOCS.md", "Documentación extendida"),
        ("DEVICES.md", "Referencia de dispositivos"),
        ("ROADMAP.md", "Roadmap del proyecto"),
        ("TROUBLESHOOTING.md", "Guía de solución de problemas"),
    ]
    
    print("\n📁 Verificando archivos esenciales:")
    for filepath, description in files_to_check:
        total_checks += 1
        if check_file_exists(filepath, description):
            checks_passed += 1
    
    # Verificar sintaxis Python
    print("\n🐍 Verificando sintaxis Python:")
    total_checks += 1
    if run_command("python -m py_compile wshot/__init__.py wshot/cli.py", "Sintaxis Python"):
        checks_passed += 1
    
    # Verificar que se puede construir el paquete
    print("\n📦 Verificando construcción del paquete:")
    total_checks += 1
    if run_command("python -m build --check", "Verificación de build"):
        checks_passed += 1
    
    # Verificar pyproject.toml
    print("\n⚙️ Verificando configuración:")
    total_checks += 1
    if run_command("python -c \"import tomllib; tomllib.load(open('pyproject.toml', 'rb'))\"", "Sintaxis pyproject.toml"):
        checks_passed += 1
    
    # Verificar que wshot se puede importar
    print("\n🔌 Verificando importación:")
    total_checks += 1
    if run_command("python -c \"import wshot; print('Wshot importado correctamente')\"", "Importación de wshot"):
        checks_passed += 1
    
    # Resumen
    print("\n" + "=" * 50)
    print(f"📊 Resumen: {checks_passed}/{total_checks} verificaciones pasadas")
    
    if checks_passed == total_checks:
        print("🎉 ¡Todo listo para publicar!")
        print("\n📝 Próximos pasos:")
        print("1. python -m build")
        print("2. python -m twine check dist/*")
        print("3. python -m twine upload --repository testpypi dist/*")
        print("4. python -m twine upload dist/*")
        return True
    else:
        print("⚠️  Hay problemas que resolver antes de publicar")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)