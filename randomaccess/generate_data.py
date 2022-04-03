import numpy as np

a = np.memmap("input.dat", dtype='uint8', mode='w+', shape=(1024*1024*1900,))
a[:] = np.random.randint(np.iinfo(np.uint8).max, size = (1024*1024*1900,), dtype=np.uint8)

a.flush()