from sklearn.svm import NuSVC
import numpy as np
from sklearn.datasets import make_classification
import time


X, y = make_classification(n_samples=20000,
                               n_features=700,
                               n_informative=700,
                               n_repeated=0,
                               n_redundant=0,
                               n_classes=2,
                               random_state=777)
y = np.asfortranarray(y).ravel()
def lambda_handler(event, context):
    
    gamma = 1.0 / X.shape[1]
    n_classes = len(np.unique(y))

    

    start = time.time()
    clf = NuSVC(nu=0.5, kernel='sigmoid', cache_size=8,
                tol=1e-3, gamma=gamma, probability=False,
                random_state=43, degree=3)

    alg = clf.fit(X,y)
    end = time.time()
    print(end-start)
        
    # print(end-start)
    return end - start
    
    
    
    
print(lambda_handler({},{}))
