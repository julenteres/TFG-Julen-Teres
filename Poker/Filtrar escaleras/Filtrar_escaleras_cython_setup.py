# Filtrar_escaleras_cython_setup.py
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("Filtrar_escaleras_cython_main.pyx", compiler_directives={"language_level": "3"})
)

