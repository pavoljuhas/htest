#import timeit
import time
import htest 
import numpy as np

h = htest.hist1d(10, 0, 10);
x = np.random.random(1000000)*40;
w= np.ones_like(x)

print("Timing Cython")
tstart = time.time()
h.fillcy(x,w)
tend = time.time()
print("Total time: {} s".format(tend-tstart))

print("Timing Numpy")
tstart = time.time()
h.fillnp(x,w)
tend = time.time()
print("Total time: {} s".format(tend-tstart))

print("Timing Python Looping (no cython)")
tstart = time.time()
h.fill(x,w)
tend = time.time()
print("Total time: {} s".format(tend-tstart))
