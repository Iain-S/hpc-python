import numpy as np

matrix_a = np.random.random((3, 3))
matrix_a_t = np.transpose(matrix_a)
print(matrix_a)
print(matrix_a_t)
matrix_a_sym = matrix_a_t + matrix_a
print(matrix_a_sym)
print(matrix_a_sym == np.transpose(np.copy(matrix_a_sym)))

matrix_b = np.random.random((3, 3))
matrix_b_t = np.transpose(matrix_b)
print(matrix_b)
print(matrix_b_t)
matrix_b_sym = matrix_b_t + matrix_b

matrix_c = np.dot(matrix_a_sym, matrix_b_sym)
print(matrix_c)
print('eigenvalues', np.linalg.eigvals(matrix_c))
