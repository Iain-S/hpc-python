import matplotlib.pyplot as plt
import numpy as np

one_d = np.random.normal(100, 1000, (1000,))
print(np.mean(one_d))
print(np.std(one_d))
plt.hist(one_d)

one_d = np.random.uniform(100, 1000, (1000,))
print(np.mean(one_d))
print(np.std(one_d))
plt.hist(one_d)
plt.show()
