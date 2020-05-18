import numpy as np
import matplotlib.pyplot as plt


delta_x = 0.1
arr_interval = np.arange(0, np.pi/2, delta_x)
print(arr_interval)
arr_sin = np.sin(arr_interval)
print(arr_sin)
arr_sin_deriv = arr_sin[2:] - arr_sin[:-2]
arr_sin_deriv /= 2*delta_x
print(arr_sin_deriv)
plt.scatter(arr_interval[1:-1], arr_sin_deriv)
plt.scatter(arr_interval[1:-1], arr_sin[1:-1])
plt.show()


# def calc_deriv(func, interval):
#     assert len(interval) > 2
#     delta_x = interval[1] - interval[0]
#     # if not delta_x:
#     #     return
#     deriv = interval[2:] - interval[:-2]
#     return deriv / (2*delta_x)
#
#
# # deriv = calc_deriv(np)
# a = calc_deriv(lambda x: 2*x, np.array([1, 2, 3]))[0]
# assert a == 2, a
# # a = calc_deriv(lambda x: x, np.array([1, 1, 1]))[0]
# # assert a == 0, a
