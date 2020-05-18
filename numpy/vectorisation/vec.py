import numpy as np

arr = np.arange(1000)


def for_diff(arr):
    diff = np.zeros(arr.shape[0]-1)
    for i in range(1, arr.shape[0]):
        diff[i-1] = arr[i] - arr[i-1]
    return diff


def vec_diff(arr):
    return arr[1:] - arr[:-1]
