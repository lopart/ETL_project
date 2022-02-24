import boto3 
import os
import shutil
import glob
import datetime

path = '/usr/local/airflow'
text_file = glob.glob(path + "/*.parquet", recursive=True)


print(text_file)

x = datetime.datetime.now()
x = str(x)
x = x[:10]

for content in text_file:
	os.rename(content, path + "/" + x + ".parquet")

print(text_file)
text_file = glob.glob(path + "/*.parquet", recursive=True)

s3_resourse = boto3.resource('s3')
#s3_resourse.create_bucket(Bucket='bookmakerdata1', CreateBucketConfiguration={'LocationConstraint': 'eu-north-1'})
s3_resourse.Object('bookmakerdata1', path + "/" + x + ".parquet" ).upload_file(Filename = path + "/" + x + ".parquet")

for content in text_file:
	os.remove(content)
