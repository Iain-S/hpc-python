import numpy as np
from scipy.integrate import solve_ivp

mm = 100000  # number of initial conditions
m = 500000  # interval of integration
step = 0.0001  # integration step
N = 36
F = 8


# ----------------------------------------
# differential equations to be integrated
def lorenz96(t, x):
    """Lorenz 96 model."""
    # Compute state derivatives
    d = np.zeros(N)

    # First the 3 edge cases: i=1,2,N
    d[0] = (x[1] - x[N - 2]) * x[N - 1] - x[0]
    d[1] = (x[2] - x[N - 1]) * x[0] - x[1]
    d[N - 1] = (x[0] - x[N - 3]) * x[N - 2] - x[N - 1]
    # Then the general case
    for i in range(2, N - 1):
        d[i] = (x[i + 1] - x[i - 2]) * x[i - 1] - x[i]
    # Add the forcing term
    d = d + F

    # Return the state derivatives
    return d


# ----------------------------------------
# x0 part (initial transient)

x0 = np.zeros(N)
for i in range(0, N):
    x0[i] = np.random.uniform() * (2 * 0.4)
esemble = np.zeros((mm, N))

# time lag iniziale
lag = int((50.0) / step)
tlag = np.arange(0.0, float(lag * step), step)  # time steps

b = 0
x = solve_ivp(lorenz96, [0.0, float(lag * step)], x0, t_eval=tlag)

for j in range(0, N):
    x0[j] = x.y[j, lag - 1]  # end lag as CI
    esemble[0, j] = x.y[j, lag - 1]

# ---------------------------------------
# Creating the esemble of initial conditions from a long run of the differential system
m_es = int((10.0) / step)  # distanza membri esemble
t_es = np.arange(0.0, float(m_es * step), step)

for ll in range(1, mm):

    x = solve_ivp(lorenz96, [0.0, float(m_es * step)], x0, t_eval=t_es)
    for j in range(0, N):
        x0[j] = x.y[j, m_es - 1]  # end as CI for next cycle
        esemble[ll, j] = x.y[j, m_es - 1]

### Heading---This the loop to be parallelized ##

Gamma_psi = np.zeros(
    (2, m))  # array which will contain the result of the integration along the time interval (0, m*step)

for i in range(mm):  # pick the ensemble member I

    xx0 = np.zeros(N)

    for j in range(0, N):
        xx0[j] = esemble[i, j]  # pick the start for each ensemble member I

    # FORWARD m STEPS
    tt = np.arange(0.0, float(m * step), step)  # interval of integration
    xx00 = solve_ivp(lorenz96, [0.0, float(m * step)], xx0, t_eval=tt)

    # saving result for just two dynamical variables
    loc = 1
    for p in range(0, m):  # cycle over time steps

        Gamma_psi[0, p] = Gamma_psi[0, p] + (xx00.y[loc, p])
        Gamma_psi[1, p] = Gamma_psi[1, p] + (xx00.y[loc - 1, p])

Gamma_psi = Gamma_psi / (float(mm))  # NB
# ---------------------------------------------
