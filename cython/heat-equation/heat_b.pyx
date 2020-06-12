# cython: profile=True
import numpy as np
cimport numpy as cnp
import matplotlib
cimport cython

matplotlib.use('Agg')
import matplotlib.pyplot as plt

# reminder: use `cython -3 -a heat_b.pyx` to annotate this file
# reminder: use profile=True at the top to enable profiling with `python -m cProfile -o output.dat heat_main.py`
# reminder: user `python3 setup.py build_ext --inplace` to build the cython lib

# Set the colormap
plt.rcParams['image.cmap'] = 'BrBG'

@cython.boundscheck(False)
@cython.wraparound(False)
cdef evolve(cnp.ndarray[cnp.double_t, ndim=2] u,cnp.ndarray[cnp.double_t, ndim=2] u_previous, float a, float dt, float dx2, float dy2):
    """Explicit time evolution.
       u:            new temperature field
       u_previous:   previous field
       a:            diffusion constant
       dt:           time step. """
    cdef int n, m
    # n, m = u.shape
    n = u.shape[0]
    m = u.shape[1]

    cdef int i, j  # this causes a x100 speedup
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            u[i, j] = u_previous[i, j] + a * dt * (
                        (u_previous[i + 1, j] - 2 * u_previous[i, j] +
                         u_previous[i - 1, j]) / dx2 + \
                        (u_previous[i, j + 1] - 2 * u_previous[i, j] +
                         u_previous[i, j - 1]) / dy2)
    u_previous[:] = u[:]

def iterate(field, field0, a, dx, dy, timesteps, image_interval):
    """Run fixed number of time steps of heat equation"""

    dx2 = dx ** 2
    dy2 = dy ** 2

    # For stability, this is the largest interval possible
    # for the size of the time-step:
    dt = dx2 * dy2 / (2 * a * (dx2 + dy2))

    for m in range(1, timesteps + 1):
        evolve(field, field0, a, dt, dx2, dy2)
        if m % image_interval == 0:
            write_field(field, m)

def init_fields(filename):
    # Read the initial temperature field from file
    field = np.loadtxt(filename)
    field0 = field.copy()  # Array for field of previous time step
    return field, field0

def write_field(field, step):
    plt.gca().clear()
    plt.imshow(field)
    plt.axis('off')
    plt.savefig('heat_{0:03d}.png'.format(step))
