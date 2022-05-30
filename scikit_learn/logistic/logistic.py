from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.datasets import make_classification
import time


X, y = make_classification(n_samples=250000,
                               n_features=50,
                               n_informative=50,
                               n_repeated=0,
                               n_redundant=0,
                               n_classes=2,
                               random_state=777)

def lambda_handler(event, context):
    start = time.time()
    clf = LogisticRegression(penalty='l2', C=1.0,
                             fit_intercept=True,
                             verbose=False,
                             tol=1e-10, max_iter=100,
                             solver="lbfgs", multi_class='auto')

    alg = clf.fit(X,y)
    end = time.time()
    print(end-start)
        
    # print(end-start)
    return end - start
    
    
    
    
# print(lambda_handler({},{}))
