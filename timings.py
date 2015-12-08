#import timeit
import time
import htest 
import numpy as np

print('hello')
h = htest.hist1d(10, 0, 10);
x = np.random.random(1000000)*40;
w= np.ones_like(x)

tstart = time.time()
#h.fillnp(x,w)
h.fillcy(x,w)
#h.fill(x,w)
tend = time.time()
print("{}".format(tend-tstart))

tstart = time.time()
h.fillnp(x,w)
tend = time.time()
print("{}".format(tend-tstart))
tstart = time.time()
h.fill(x,w)
tend = time.time()
print("{}".format(tend-tstart))
print(h.data)
