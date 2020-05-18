import numpy as np

arb = np.random.random((4, 4))
print(arb)
print(arb[1])
print(arb[:, 2])
arb[:2,:2] = 0.21
print(arb)

p = print
ones = np.ones((8,8))
p(ones)
ones[::2, 1::2] = 0  # on even numbered rows, start with second
ones[1::2, ::2] = 0  # on odd numbered rows, start with first
p(ones)

