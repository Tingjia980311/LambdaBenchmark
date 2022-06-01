from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.datasets import make_regression
from sklearn.metrics.cluster import davies_bouldin_score
from sklearn.utils import check_random_state
import time


rs = check_random_state(777)
X, y = make_regression(n_targets=1,
                        n_samples=1000000,
                        n_features=200,
                        n_informative=200,
                        bias=rs.normal(0, 3),
                        random_state=rs)

def lambda_handler(event, context):
    start = time.time()
    regr = LinearRegression(fit_intercept=True)
    alg = regr.fit(X,y)
    end = time.time()
    # print(end-start)
    return end - start
    
    
    
    
# print(lambda_handler({},{}))
