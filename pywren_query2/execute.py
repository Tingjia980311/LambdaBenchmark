import boto3
import base64
import json
import time
lambda_client = boto3.client('lambda')
memory = [256, 512, 1024, 2048, 3072, 4096, 5120, 6144, 7168, 8192]
memory.reverse()
for m in memory:
    print ("memory size setted to: ", m)
    response = lambda_client.update_function_configuration(
        FunctionName='query2',
        MemorySize=m,
    )
    time.sleep(3)
    # print(response)
    billtimes = []
    maxMemories = []
    read_times = []
    execute_times = []
    upload_times = []
    for i in range (11):
        response = lambda_client.invoke(
            FunctionName='query2',
            LogType='Tail',
            Payload='',
        )
        if i==0:
            time.sleep(0.2)
            continue
        timestamps = response['Payload'].read().decode("utf-8")
        # 
        timestamps = json.loads(timestamps) #dict(toks.split(":") for toks in timestamps[1:-1].split(","))
        # print(timestamps)
        logresults = response['LogResult']
        logresults = (base64.b64decode(logresults)).decode()
        logresults = logresults.split("\n")[-2]
        # print(logresults)
        logresults = dict(toks.split(":") for toks in logresults.split("\t")[1:-1])
        # print(logresults)
        
        billtimes.append(int(logresults['Billed Duration'][0:-3]))
        maxMemories.append(int(logresults['Max Memory Used'][0:-3]))
        read_times.append(timestamps['read'])
        execute_times.append(timestamps['execute'])
        upload_times.append(timestamps['upload'])
        time.sleep(0.2)

    billedtime = sum(billtimes)/len(billtimes)
    maxMemory = max(maxMemories)
    readtime = sum(read_times)/len(read_times)
    executetime = sum(execute_times)/len(execute_times)
    uploadtime = sum(upload_times)/len(upload_times)

    print("billedtime = ", billedtime)
    print("maxMemory = ", maxMemory)
    print("readtime = ", readtime)
    print("executetime = ", executetime)
    print("uploadtime = ", uploadtime)
# billedtime = response[""]
# aws lambda invoke  --function-name query2 --payload '{}' out --log-type Tail --query 'LogResult' --output text |  base64 -d