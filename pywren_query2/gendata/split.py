import boto3
client = boto3.client('s3', 'us-east-1')

bucketName = 'query2-input'
keyname = "part-" + '{:0>5d}'.format(0)


obj = client.get_object(Bucket=bucketName, Key=keyname)
fileobj = obj['Body']

raw_data = fileobj.read().decode()
# print(raw_data)
raw_data = raw_data.split('\n')
print(len(raw_data))
raw_data = '\n'.join(raw_data[0:400000])
# with open('/tmp/part-00000-00.txt', 'w') as f:
#     f.write(raw_data)

client.put_object(Body=raw_data, Bucket="query2-input", Key=f'part_00000_00000')