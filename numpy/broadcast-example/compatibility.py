import numpy as np

a = np.arange(2, 26)
a.shape = (2, 3, 4)

b = np.ones((2, 3, 4))  # compatible, same dimensions
print(a * b)

b = np.ones((3, 4))  # compatible, a = l, m, n and b = m, n
print(a * b)

b = np.ones((1, 3, 4))  # compatible, a = l, m, n and b = 1, m, n
print(a * b)

b = np.ones((3, 1))  # compatible, a = l, m, n and b = m, 1
print(a * b)

b = np.ones((2, 1, 4))  # compatible, a = l, m, n and b = m, 1
print(a * b)

# b = np.ones((2, 3))  # not compatible, though (2, 3, 1) would be
# print(a * b)

# summary
# compare dimensions from the right-most
# if dimensions match or either one is 1 then they are compatible
# stop when you run out of dimensions on the shortest
# e.g. (256, 256, 3) * (1) or (1, 1) or (1, 1, 1) should be compatible
# e.g. (256, 256, 3) * (3) or (1, 3) or (256, 3) or (256, 1, 3) or (1, 1, 3) should be compatible
# e.g. (256, 256, 3) * (2, 256, 256, 3) should be compatible
