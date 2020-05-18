import numpy as np

py_list = [1, 2, 3.0, 4.0]
print(type(py_list[0]))
print(type(py_list[2]))
npy_arr = np.array(py_list)
print(npy_arr.dtype)

two = np.arange(-2.0, 2.2, 0.2)
# are there data-type args to arange()?
print(two)

three = np.linspace(0.5, 1.5, 11)
print(three)

four = np.array('qfour', dtype='c')
print(four)

