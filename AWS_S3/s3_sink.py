import boto3 

s3_resourse = boto3.resource('s3')
# s3_resourse.create_bucket(Bucket='bookmakerdata1', CreateBucketConfiguration={'LocationConstraint': 'eu-north-1'}) creating s3 bucket if not created
