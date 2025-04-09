# Serverless Resume Uploader on AWS

This project lets users upload resumes via an API. Files are stored in S3, and a Lambda function processes the upload to extract and store metadata in DynamoDB.

## 🧱 Stack
- AWS S3
- AWS Lambda
- AWS DynamoDB
- API Gateway
- Python (boto3)
- CloudFormation / AWS SAM

---

## 📁 Project Structure
```
project/
├── README.md
├── template.yaml  # CloudFormation or AWS SAM template
├── lambda/
│   └── lambda_function.py
├── scripts/
│   └── upload_script.py
├── test/
│   └── sample_resume.pdf
└── requirements.txt
```

---

## 🚀 Deployment Steps
1. Clone the repo
2. Install AWS CLI and configure credentials
3. Run deployment (SAM or manually via console)

```bash
sam build
sam deploy --guided
```

---

## 📌 Features
- Upload a resume file via API
- Trigger a Lambda function to log metadata
- Store metadata in DynamoDB (e.g. filename, upload time)

---

## 🧪 Testing
Use Postman or `upload_script.py` to test the endpoint.

---

## 🧾 Metadata Saved
```json
{
  "filename": "resume.pdf",
  "upload_time": "2025-04-09T12:34:56Z",
  "bucket": "resume-bucket",
  "size": "145KB"
}
```

---

## 📚 Learning Objectives
- Build and deploy serverless architecture
- Automate file uploads with Python (boto3)
- Gain hands-on experience with AWS Lambda, API Gateway, and DynamoDB

---

## 📄 Blog Prompt (Optional)
**Title**: Building a Serverless Resume Uploader with AWS Lambda and S3
**Outline**:
- Why I built this project
- Architecture diagram
- Step-by-step explanation
- Code snippets
- Lessons learned
- What I’ll do next

---

## 🔗 Author
Built with ❤️ as part of my Cloud Engineering portfolio journey