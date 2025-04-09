import json
import boto3
import os
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table_name = os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        # Extract S3 event data
        for record in event['Records']:
            bucket = record['s3']['bucket']['name']
            key = record['s3']['object']['key']
            size = record['s3']['object']['size']
            event_time = record['eventTime']
            
            # Convert eventTime to datetime object
            upload_time = datetime.strptime(event_time, "%Y-%m-%dT%H:%M:%S.%fZ")
            
            # Store metadata in DynamoDB
            response = table.put_item(
                Item={
                    'FileName': key,
                    'FileSize': str(size),
                    'UploadTime': upload_time.isoformat(),
                    'Bucket': bucket
                }
            )
        
        return {
            'statusCode': 200,
            'body': json.dumps('File metadata stored successfully!')
        }
    except Exception as e:
        print(f"Error processing event: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error processing file metadata')
        }
