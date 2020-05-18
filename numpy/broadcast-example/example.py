import numpy as np

points = np.random.random((100, 3))
origin = np.array([-4.0, 2.2, 5.1])

distances = (points - origin)**2
distances = np.sqrt(np.sum(distances, axis=1))
print(distances)
# print(points.shape)
# print(origin.shape)


a = np.arange(2, 26)
a.shape = (2, 3, 4)
