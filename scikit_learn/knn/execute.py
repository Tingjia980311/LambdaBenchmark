import boto3
import base64
import json
import time
import statistics

lambda_client = boto3.client('lambda',  region_name='us-east-1')
memory = [ 1024, 2048, 3072, 4096, 5120, 6144, 7168, 8192, 10240]
memory.reverse()

execute_times = {}
max_memorys = {}
for m in memory:
    execute_times[m] = []
    max_memorys[m] = []
for i in range(5):
    for m in memory:
        print ("memory size set to: ", m)
        while 1:
            try:
                response = lambda_client.update_function_configuration(
                    FunctionName='AnalysisKnn',
                    MemorySize=m,
                )
                break
            except:
                time.sleep(1)
        time.sleep(1)
        response = lambda_client.get_function_configuration(
            FunctionName='AnalysisKnn'
        )
        while response["MemorySize"]!=m:
            time.sleep(1)
            response = lambda_client.get_function_configuration(
                FunctionName='AnalysisKnn'
            )
        print("memory size setted to: ", response["MemorySize"])
        time.sleep(3)
        i = 0
        while i < 11:
            response = lambda_client.invoke(
                FunctionName='AnalysisKnn',
                LogType='Tail',
                Payload='',
            )
            logresults = response['LogResult']
            logresults = (base64.b64decode(logresults)).decode()
            logresults = logresults.split("\n")[-2]
            logresults = dict(toks.split(":") for toks in logresults.split("\t")[1:-1])
            if int(logresults['Memory Size'][0:-3]) != m:
                time.sleep(1)
                continue
            if i == 0:
                time.sleep(1)
                i += 1
                continue
            i += 1
            print(logresults)
            
            max_memorys[m].append(int(logresults['Max Memory Used'][0:-3]))
            execute_times[m].append(float(logresults['Duration'][0:-3]))
            time.sleep(1)
        print(execute_times)
        print(max_memorys)
            
print(execute_times)
print(max_memorys)
for m in memory:
    print("memory: ", m)
    executetime_avg = sum(execute_times[m])/len(execute_times[m])
    executetime_dev = statistics.stdev(execute_times[m])
    maxMemory = max(max_memorys[m])
    print("maxMemory = ", maxMemory)
    print("executetime average = ", executetime_avg)
    print("executetime dev     = ", executetime_dev)
    print("---------------------------------------------")