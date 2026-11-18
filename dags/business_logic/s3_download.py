import boto3
from airflow.providers.amazon.aws.hooks.base_aws import AwsBaseHook

def s3_download_file(bucket_name, object_key, path):
    
    # Initialize the hook using the Connection ID from the UI
    aws_hook = AwsBaseHook(aws_conn_id="aws_profile", client_type="s3")

    s3_client = aws_hook.get_client_type(region_name="us-east-1")
    response = s3_client.list_objects_v2(
        Bucket=bucket_name,
        Prefix=object_key  # Omit to list the entire bucket
    )

    # Extract file keys from the response
    for obj in response.get('Contents', []):
        key = obj['Key']
        file = key.split('/')[1]
        s3_client.download_file(bucket_name, key, f'{path}/{file}')
