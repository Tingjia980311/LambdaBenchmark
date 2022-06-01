from sklearn.svm import SVC
import numpy as np
from sklearn.datasets import make_classification
import time


X, y = make_classification(n_samples=20000,
                               n_features=30,
                               n_informative=30,
                               n_repeated=0,
                               n_redundant=0,
                               n_classes=2,
                               random_state=777)
y = np.asfortranarray(y).ravel()

def lambda_handler(event, context):
    gamma = 1.0 / X.shape[1]
    n_classes = len(np.unique(y))
    start = time.time()
    clf = SVC(kernel='sigmoid',
                tol=1e-3, gamma=gamma, probability=False,
                random_state=43, degree=3)

    alg = clf.fit(X,y)
    end = time.time()

    return end - start
    
    
    
    
# print(lambda_handler({},{}))
