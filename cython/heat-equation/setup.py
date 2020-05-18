from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy


setup(
    language_level=3,
    ext_modules=cythonize("heat_b.pyx"),
    include_dirs=[numpy.get_include()]
    # ext_modules=[
    #     Extension("heat_b",
    #               ["heat_b.pyx"],
    #               include_dirs=[np.get_include()])
    # ]
)
