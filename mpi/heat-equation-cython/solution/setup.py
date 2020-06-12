from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

setup(
    language_level=3,
    ext_modules=cythonize("evolve.pyx"),
    include_dirs=[numpy.get_include()]
)
