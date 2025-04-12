#!/bin/bash

# Install AWS CLI
pip install awscli

# Configure AWS CLI
aws configure

# Install Boto3
pip install boto3

# Print completion message
echo "Environment setup complete. AWS CLI and Boto3 installed."