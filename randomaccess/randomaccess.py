import numpy as np
import random
# a = np.memmap("input.dat", dtype='float32', mode='w+', shape=(1024*1024*256,))
# a[:] = np.random.rand(1024*1024*256,)
# a.flush()
def lambda_handler(event, context):
    # size should be how many MB you want to get from the input.dat
    # it is from 1 to 256
    size = event['size']
    times = event['time']
    a = np.memmap("input.dat", dtype = 'uint8', mode='r', shape=(1024*1024*size,))
    results = []
    for _ in range(times):
        results.append(str(a[random.randint(0, 1024*1024*size-1)]))
    return results
    
# print(lambda_handler({'size':256},{}))
