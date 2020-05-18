import numpy as np
import matplotlib.pyplot as plt


def translate(points, by):
    c = points + by
    return c


circle = np.loadtxt('points_circle.dat', encoding='utf-8')
circle.tofile('zz.data')
# plt.scatter(*(np.split(circle, 2, axis=1)))
plt.plot(circle[:, 0], circle[:, 1], 'bo')
# plt.show()
assert circle.shape == (10, 2), 'shape was: {}'.format(circle.shape)

new_circle = translate(circle, np.array([-21, -21]))
print(new_circle)
# plt.scatter(*(np.split(new_circle, 2, axis=1)), 'o')
plt.plot(new_circle[:, 0], new_circle[:, 1], 'ro')
plt.show()
