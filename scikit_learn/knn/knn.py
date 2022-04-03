from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.datasets import make_classification
import time


X, y = make_classification(n_samples=20000,
                               n_features=50,
                               n_informative=50,
                               n_repeated=0,
                               n_redundant=0,
                               n_classes=2,
                               random_state=777)

def lambda_handler(event, context):
    start = time.time()
    knn_clsf = KNeighborsClassifier(n_neighbors=3,
                                weights='uniform',
                                algorithm='kd_tree',
                                metric='euclidean')

    alg = knn_clsf.fit(X,y)
    end = time.time()
    print(end-start)
        
    # print(end-start)
    return end - start
    
    
    
    
# print(lambda_handler({},{}))
