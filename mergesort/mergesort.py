import numpy as np

def lambda_handler(event, context):
    
    a = np.random.rand(1024*event['size'],)
    for i in range(1000):
        a.sort(kind='mergesort')
    return a[0]

    
    
# print(lambda_handler({},{}))
