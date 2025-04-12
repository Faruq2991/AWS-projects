# CloudFormation S3 Alarm Project

This project sets up an AWS infrastructure using CloudFormation to upload files to an S3 bucket and monitor the file count with CloudWatch alarms.

## Project Structure

```
cloudformation-s3-alarm-project
├── templates
│   ├── s3-bucket.yaml          # CloudFormation template for creating an S3 bucket
│   ├── cloudwatch-alarm.yaml    # CloudFormation template for setting up CloudWatch alarms
│   └── iam-roles.yaml           # CloudFormation template for IAM roles and policies
├── scripts
│   ├── upload-file.py           # Python script for uploading files to S3
│   └── setup-environment.sh     # Shell script for setting up the environment
├── README.md                    # Project documentation
└── .gitignore                   # Files and directories to ignore in version control
```

## Setup Instructions

1. **Clone the Repository**  
   Clone this repository to your local machine using:
   ```
   git clone git@github.com:Faruq2991/AWS-projects.git
   ```

2. **Set Up Environment**  
   Run the setup script to install necessary dependencies and configure AWS CLI:
   ```
   chmod +x scripts/setup-environment.sh
   ./scripts/setup-environment.sh
   ```

3. **Deploy CloudFormation Templates**  
   Use the AWS CLI to deploy the CloudFormation templates:
   ```
   aws cloudformation deploy --template-file templates/iam-roles.yaml --stack-name S3AlarmStack --capabilities CAPABILITY_IAM
   aws cloudformation deploy --template-file templates/s3-bucket.yaml --stack-name S3BucketStack
   aws cloudformation deploy --template-file templates/cloudwatch-alarm.yaml --stack-name CloudWatchAlarmStack
   ```

4. **Set Environment Variable**  
   After deploying the stack, export the S3 bucket name as an environment variable:
   ```
   export S3_BUCKET_NAME=<your-s3-bucket-name>
   ```

## Usage Example

To upload a file to the S3 bucket, run the following command:
```
python scripts/upload-file.py <file-path>
```

## Configuration Details

- **S3 Bucket**:  
  The S3 bucket is configured with versioning enabled and a lifecycle rule to expire files in the `uploads/` prefix after 30 days.

- **Bucket Policy**:  
  The bucket policy allows public `s3:PutObject` actions for objects in the bucket.

- **S3 Notifications**:  
  The bucket is configured to trigger a Lambda function (`ProcessFileFunction`) whenever a new object is created in the bucket.

## CloudFormation Templates

- **s3-bucket.yaml**: Creates an S3 bucket with versioning, lifecycle rules, and event notifications.
- **cloudwatch-alarm.yaml**: Sets up a CloudWatch alarm that triggers when the file count exceeds a specified threshold.
- **iam-roles.yaml**: Defines IAM roles and policies for Lambda function access to S3 and CloudWatch.

## License

This project is licensed under the MIT License.
