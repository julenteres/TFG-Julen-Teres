# setup.py
from setuptools import setup
from Cython.Build import cythonize
import sys

setup(
    name="Cantidad_de_figuras_cython",
    ext_modules=cythonize(
        "Cantidad_de_figuras_cython_main.pyx",
        compiler_directives={'language_level': "3"}
    ),
    zip_safe=False,
)

