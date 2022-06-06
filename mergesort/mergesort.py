import numpy as np
a = np.random.rand(1024*1024)

def lambda_handler(event, context):
    # import time
    # start = time.time()
    for i in range(5):
        b = np.sort(a, kind='mergesort')
    # end = time.time()
    # print(end - start)
    return a[0]

    
    
# print(lambda_handler({},{})) 
