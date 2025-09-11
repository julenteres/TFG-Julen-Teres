from setuptools import setup
from Cython.Build import cythonize

setup(
    name="matrix_multiplication_cython",
    ext_modules=cythonize("matrix_multiplication_cython.pyx"),
)
