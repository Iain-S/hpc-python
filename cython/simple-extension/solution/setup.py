from distutils.core import setup
from Cython.Build import cythonize

setup(
     # language_level="3"
     ext_modules=cythonize("cyt_module.pyx", gdb_debug=True)
)
