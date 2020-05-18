import timeit
import numpy as np
import numexpr

x = np.random.random((10, 10))


def standard_way():
    poly = ((.25 * x + .75) * x - 1.5) * x - 2
    return poly


def numexpr_way():
    poly = numexpr.evaluate("((.25*x + .75)*x - 1.5)*x - 2")
    return poly


print('standard way: ', min(timeit.repeat('standard_way()',
                                          setup='from __main__ import standard_way',
                                          number=100)))
print('numexpr way: ', min(timeit.repeat('numexpr_way()',
                                         setup='from __main__ import numexpr_way',
                                         number=100)))
# For me at least, this doesn't show any speedup with numexpr
