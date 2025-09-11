# setup.py

from setuptools import setup
from Cython.Build import cythonize

setup(
    name="cross_product_cython",
    ext_modules=cythonize("cross_product_cython.pyx", language_level=3),
)
