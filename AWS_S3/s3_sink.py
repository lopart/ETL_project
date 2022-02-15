import boto3 
import glob

path = 'path/to/the/folder' # path to the folder with files outputted from Structured Streaming in docker
text_file = glob.glob(path + "/*.csv", recursive=True)

s3_resourse = boto3.resource('s3')

# uncomment if bucket is not created yet and enter the name for a new bucket 
#s3_resourse.create_bucket(Bucket='bucket_name', CreateBucketConfiguration={'LocationConstraint': 'eu-north-1'})

s3_resourse.Object('bucket_name', text_file[0]).upload_file(Filename = text_file[0])
