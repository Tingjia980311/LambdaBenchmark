
from sklearn.cluster import DBSCAN
import numpy as np
import os
# os.environ["OMP_NUM_THREADS"] = str(2)

from sklearn.datasets import make_blobs
import time


X, y = make_blobs(n_samples=100000,
                    n_features=3,
                    centers=50,
                    center_box=(-32, 32),
                    shuffle=True)

def lambda_handler(event, context):
    start = time.time()
    dbscan = DBSCAN(eps=10, 
                    min_samples=5, metric='euclidean',
                    algorithm='auto', leaf_size = event['leaf_size'], n_jobs = -1)

    dbscan = dbscan.fit(X)
    end = time.time()
    # print(end-start)
    return (end - start), event['leaf_size']
    
    
    
    
# print(lambda_handler({"n-clusters": 100},{}))
