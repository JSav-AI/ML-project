import boto3
from botocore.exceptions import ClientError
import os
import io
from botocore.config import Config
from botocore import UNSIGNED 


s3 = boto3.client('s3',
                  region_name = os.getenv('region_name'),
                  config = Config(signature_version=UNSIGNED))

bucket_name = os.getenv("BUCKET_NAME")



def list_s3_file(bucket_name, prefix):
    try:
        response = s3.list_objects_v2(Bucket=bucket_name, prefix=prefix)
        return [item['key'] for item in response.get('Contents', [])]
    except ClientError as e:
        print(f"Error listing files from S£: {e}")
        return []
    
def download_s3_file(bucket_name, key):
    try:
        response = s3.get_object(Bucket=bucket_name, key=key)
        return response['Body'].read().decode('utf-8')
    except ClientError as e:
        print(f"Error Downloading file from S3: {e}")
        return None
    
def save_s3_file(file_content, bucket_name, key):
    try:
        file_obj = io.BytesIO(file_content)

        s3.upload_fileobj(file_obj, bucket_name, key)
        return True
    except ClientError as e:
        print(f"Error uploading file to S3: {e}")
        return False 

