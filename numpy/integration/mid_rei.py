import numpy as np


def integrate(func, a, b, dx):
    interval_prime = np.arange(a, b + dx, dx)
    interval_prime = interval_prime[1:] + interval_prime[:-1]
    interval_prime = interval_prime / 2
    integral = func(interval_prime)
    return np.sum(integral) * dx


integrate(lambda x: x, 1, 4, 1)

for delta in (1, 0.1, 0.01, 0.001, 0.0001):
    auc = integrate(np.sin, 0, np.pi / 2, delta)
    print(auc, auc - 1.0)
