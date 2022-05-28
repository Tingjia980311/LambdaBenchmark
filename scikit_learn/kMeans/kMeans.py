import os
import multiprocessing
from sklearn.cluster import KMeans
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.metrics.cluster import davies_bouldin_score
import time

X, y = make_blobs(n_samples=50000,
                    n_features=20,
                    centers=100,
                    center_box=(-32, 32),
                    shuffle=True)

def lambda_handler(event, context):
    start = time.time()
    k_means = KMeans(n_clusters=100, max_iter=50).fit(X)
    end = time.time()
    # print(end-start)
    return end - start
    
    
    
    
print(lambda_handler({"n-clusters": 100},{}))
