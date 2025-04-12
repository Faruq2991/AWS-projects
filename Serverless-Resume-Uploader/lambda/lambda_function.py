import json
import boto3
import os
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table_name = os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)

def process_s3_event(record):
    """
    Processes a single S3 event record and stores metadata in DynamoDB.
    """
    bucket = record['s3']['bucket']['name']
    key = record['s3']['object']['key']
    size = record['s3']['object']['size']
    event_time = record['eventTime']
    
    # Convert eventTime to datetime object
    upload_time = datetime.strptime(event_time, "%Y-%m-%dT%H:%M:%S.%fZ")
    
    # Store metadata in DynamoDB
    table.put_item(
        Item={
            'FileName': key,
            'FileSize': str(size),
            'UploadTime': upload_time.isoformat(),
            'Bucket': bucket
        }
    )

def lambda_handler(event, context):
    """
    AWS Lambda handler function.
    """
    try:
        # Process each record in the event
        for record in event['Records']:
            process_s3_event(record)
        
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
