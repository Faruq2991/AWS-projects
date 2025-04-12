import boto3
import os
import sys

def upload_file_to_s3(file_name, bucket_name):
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_name, bucket_name, os.path.basename(file_name))
        print(f"File {file_name} uploaded to bucket {bucket_name}.")
    except Exception as e:
        print(f"Error uploading file: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python upload-file.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    bucket_name = os.environ.get("BUCKET_NAME")
    if not bucket_name:
        print("Error: BUCKET_NAME environment variable is not set.")
        sys.exit(1)

    upload_file_to_s3(file_path, bucket_name)