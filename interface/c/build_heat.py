from cffi import FFI

ffibuilder = FFI()

ffibuilder.cdef("""
    void evolve(double *u, double *u_previous, int nx, int ny, 
                double a, double dt, double dx2, double dy2);
                """)

# set_source() gives the name of the python extension module to
# produce, and some C source code as a string.  This C code needs
# to make the declarated functions, types and globals available,
# so it is often just the "#include".
ffibuilder.set_source("_c_evolve",
                      """
                           #include "evolve.h"   // the C header of the library
                      """,
                      library_dirs=['.'],  # here we can provide where the library is located,
                      # as we are using C standard library empty list is enough
                      libraries=['evolve']  # name of the library we want to interface
                      )

ffibuilder.compile(verbose=True)
