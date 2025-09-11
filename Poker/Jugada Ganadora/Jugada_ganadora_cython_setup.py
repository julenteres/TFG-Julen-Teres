from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("Jugada_ganadora_cython_main.pyx"),
)

