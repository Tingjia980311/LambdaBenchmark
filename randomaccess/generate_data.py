import numpy as np

a = np.memmap("input.dat", dtype='float32', mode='w+', shape=(1024*1024*256,))
a[:] = np.random.rand(1024*1024*256,)
a.flush()