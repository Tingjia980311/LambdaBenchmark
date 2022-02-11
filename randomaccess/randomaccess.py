import numpy as np
import random
# a = np.memmap("test.dat", dtype='float32', mode='w+', shape=(1024*1024*256,))
# a[:] = np.random.rand(1024*1024*256,)
# a.flush()
def lambda_handler(event, context):
    a = np.memmap("test.dat", dtype = 'float32', mode='r', shape=(1024*1024*512,))
    results = []
    for i in range(1024*128):
        results.append(str(a[random.randint(0, 1024*1024*512-1)]))
    return results

    
    
# print(lambda_handler({},{}))
