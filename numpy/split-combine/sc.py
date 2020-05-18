import numpy as np

e = np.random.random((8, 8))
a, b = np.split(e, 2, axis=0)
assert a.shape == (4, 8)
print(b.shape)
c = np.concatenate((a, b))
assert c.shape == (8, 8)
print(c.shape)

a, b = np.split(e, 2, axis=1)
assert a.shape == (8, 4)
print(b.shape)
c = np.concatenate((a, b), axis=1)
assert c.shape == (8, 8)
print(c.shape)
