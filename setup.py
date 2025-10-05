#!/usr/bin/env python3
"""
Setup script for Wshot package
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="wshot",
    version="1.0.0",
    author="Daniel Martinez Sebastian",
    author_email="",
    description="Herramienta profesional para capturas de pantalla web en múltiples dispositivos",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DanielMartinezSebastian/scriptshotweb",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "playwright>=1.40.0",
        "requests>=2.32.0",
    ],
    entry_points={
        "console_scripts": [
            "wshot=wshot.cli:main",
        ],
    },
    keywords="screenshot web testing playwright automation",
    project_urls={
        "Bug Reports": "https://github.com/DanielMartinezSebastian/scriptshotweb/issues",
        "Source": "https://github.com/DanielMartinezSebastian/scriptshotweb",
    },
)
