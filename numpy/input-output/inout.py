import numpy as np

xy = np.loadtxt('xy-coordinates.dat')
print(xy[:, 1])
xy[:, 1] += 10
print(xy[:, 1])
np.savetxt('output.dat', xy, encoding='utf-8')
