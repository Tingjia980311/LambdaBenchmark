import numpy as np
import boto3
import io
from multiprocessing.pool import ThreadPool 
import time

import redis


# def A(x):
#     elements = x.split('.')
#     # print(elements)
#     tmp = '.'.join('0' * (3-len(e)) + e for e in elements)
#     tmp = tmp[0:7]
#     return tmp

pool = ThreadPool(processes=300) 
# f = open('part-00000','r')
# records=np.loadtxt('part-00000',delimiter=',',dtype=np.str_)
# records = records[0:100,:]
# print(records.shape)
# records[:,0] = np.frompyfunc(A,1,1)(records[:,0])
# # np.frompyfunc(lambda x: x[0:8],1,1)(records[:,0])

# records = records[:,[0,-1]]

# # records = np.sort(records, axis = 0)

# boundaries = []
# for i in range(1, 255):
#     b = str(i)
#     b = '0' * (3-len(b)) + b + '.000'
#     boundaries.append(b)

# ps = np.searchsorted(boundaries, records[:,0])

# num_partitions = 255
# outputs = [[] for _ in range(0, num_partitions)]
# for idx, record in enumerate(records):
#     outputs[ps[idx]].append(record)
# print(outputs)
def lambda_handler(event, context):
    r = redis.Redis(
        host='ephe-store.7y4xmn.ng.0001.use1.cache.amazonaws.com',
        port=6379)

    def A(x):
        elements = x.split('.')
        # print(elements)
        tmp = '.'.join('0' * (3-len(e)) + e for e in elements)
        tmp = tmp[0:7]
        return tmp
    start_t = time.time()

    # TODO: make the parameters configurable
    fileId = 0 # key['fileId']
    taskId = 0

    # s3 = S3FileSystem()
    client = boto3.client('s3', 'us-east-1')

    bucketName = 'query2-input'
    keyname = "part_" + '{:0>5d}'.format(fileId) + "_" +  '{:0>5d}'.format(taskId)

    obj = client.get_object(Bucket=bucketName, Key=keyname)
    fileobj = obj['Body']
    """
    # raw_data = fileobj.read().decode()
    # # print(raw_data)
    # raw_data = raw_data.split('\n')
    # print(len(raw_data))
    # raw_data = '\n'.join(raw_data[0:1000])
    # with open('/tmp/part-00000-00.txt', 'w') as f:
    #     f.write(raw_data)
    # print(len(raw_data))
    """
    with io.BytesIO(fileobj.read()) as f:
        f.seek(0)
        records=np.loadtxt(f, delimiter=',', dtype=np.str_)
    read_t = time.time()

    boundaries = []
    for i in range(1, 255):
        b = str(i)
        b = '0' * (3-len(b)) + b + '.000'
        boundaries.append(b)

    records[:,0] = np.frompyfunc(A,1,1)(records[:,0])

    records = records[:,[0,-1]]
    ps = np.searchsorted(boundaries, records[:,0])

    num_partitions = 255
    outputs = [[] for _ in range(0, num_partitions)]
    for idx, record in enumerate(records):
        outputs[ps[idx]].append(record)
    # print(outputs)
    outputs_dict = {}
    for partition_idx, data in enumerate(outputs):
        # print(data)
        outputs[partition_idx] = np.asarray(data).tobytes()
        outputs_dict[partition_idx] = np.asarray(data).tobytes()
        # print(np.asarray(data).dtype)
    # for partition_idx,  in enumerate(outputs):
        # client.put_object(Body=data, Bucket="query2-ephe", Key=f'{fileId}_{partition_idx}')
    upload_t = time.time()
    def upload(partition_idx): 
        client.put_object(Body=outputs[partition_idx], Bucket="query2-ephe", Key=f'{fileId}_{partition_idx}')
    print("upload")
    pool.map(upload, list(range(0,len(outputs))))
    # print("upload")
    # for i in range(100):
    #     r.mset(outputs_dict)
    # tmp = r.get('1')
    # print(np.fromstring(tmp, dtype = '<U152'))
    finish_t = time.time()
    return {
        "read": read_t - start_t,
        "execute": upload_t - read_t,
        "upload": finish_t - upload_t
    }

print(lambda_handler(0,0))