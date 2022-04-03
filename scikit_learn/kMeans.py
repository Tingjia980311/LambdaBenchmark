import os
import multiprocessing
# n_cpu = multiprocessing.cpu_count()
# if n_cpu == 1:
#     n_job = 1
# else:
#     n_job = int(n_cpu / 2)
# os.environ["OMP_NUM_THREADS"] = str(n_job)
# print(os.environ["OMP_NUM_THREADS"])

from sklearn.cluster import KMeans
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.metrics.cluster import davies_bouldin_score
import time

# from sklearnex import patch_sklearn
# patch_sklearn()

"""
# def convert_data(data, dtype, data_order, data_format):
#     '''
#     Convert input data (numpy array) to needed format, type and order
#     '''
#     if data_order == 'F':
#         data = np.asfortranarray(data, dtype)
#     elif data_order == 'C':
#         data = np.ascontiguousarray(data, dtype)

#     # Secondly, change format of data
#     if data_format == 'numpy':
#         return data
#     if data_format == 'pandas':
#         import pandas as pd

#         if data.ndim == 1:
#             return pd.Series(data)
#         return pd.DataFrame(data)

# def load_data(dtype, file_paths):
#     full_data = {
#         file: None for file in ['X_train', 'X_test']
#     }
#     for element in full_data:
#         file_arg = f'file_{element}'
#         new_dtype = dtype
#         if file_paths[file_arg] is not None:
#             data = np.load(file_paths[file_arg], allow_pickle = True)
#         full_data[element] = convert_data(
#             data,
#             new_dtype,
#             'F', 'pandas'
#         )
#     for data in ['X']:
#         if full_data[f'{data}_train'] is not None and full_data[f'{data}_test'] is None:
#             full_data[f'{data}_test'] = full_data[f'{data}_train']
    
#     return tuple(full_data.values())

# def fit_kmeans(X, X_init, params):
    # alg = KMeans(n_clusters=params["n_clusters"], tol=params["tol"],
    #                  max_iter=params["maxiter"], init=X_init, n_init=params["n_init"],
    #                  algorithm=params["algorithm"], random_state=params["random_state"])
    # alg.fit(X)
    # return alg
"""
"""
python3 sklearn_bench/kmeans.py --no-intel-optimized --arch ip-172-31-81-244 --data-format pandas --data-order F --dtype float32 --device host --time-method box_filter --time-limit 50 --n-clusters 1000 --maxiter 50 --tol 0.0 --file-X-train data/synthetic-blobs-1000-X-train-100000x20.npy --dataset-name synthetic_blobs
"""

X, y = make_blobs(n_samples=1000000,
                    n_features=100,
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
