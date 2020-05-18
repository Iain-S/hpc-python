from distutils.core import setup, Extension
from Cython.Build import cythonize

ext = Extension("cfib",
                sources=["cfib.pyx"],
                )

setup(
    ext_modules=cythonize(ext)
)
