import timeit
import time
import htest
import numpy as np

h = htest.hist1d(10, 0, 10);
x = np.random.random(1000000)*40;
w= np.ones_like(x)
gg = globals()

def timethis(stmt):
    return np.mean(timeit.repeat(stmt, number=10, repeat=5, globals=gg))

print("Timing")
print("Cython:", timethis('h.fillcy(x, w)'))
print("Cython with call:", timethis('h.fillcywithcall(x, w)'))
print("Numpy", timethis('h.fillnp(x, w)'))
# print("Python Looping", timethis('h.fill(x, w)'))
