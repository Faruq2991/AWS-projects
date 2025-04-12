import unittest
import json
import sys
import os
from unittest.mock import patch, MagicMock
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lambda_function import process_s3_event, lambda_handler

class TestLambdaFunction(unittest.TestCase):
    @patch('lambda_function.table.put_item')
    def test_process_s3_event(self, mock_put_item):
        # Mock S3 event record
        record = {
            's3': {
                'bucket': {'name': 'test-bucket'},
                'object': {'key': 'test-file.txt', 'size': 12345}
            },
            'eventTime': '2025-04-12T12:34:56.789Z'
        }

        # Call the function
        process_s3_event(record)

        # Assert that DynamoDB put_item was called with correct arguments
        mock_put_item.assert_called_once_with(
            Item={
                'FileName': 'test-file.txt',
                'FileSize': '12345',
                'UploadTime': '2025-04-12T12:34:56',
                'Bucket': 'test-bucket'
            }
        )

    @patch('lambda_function.process_s3_event')
    def test_lambda_handler(self, mock_process_s3_event):
        # Mock Lambda event
        event = {
            'Records': [
                {
                    's3': {
                        'bucket': {'name': 'test-bucket'},
                        'object': {'key': 'test-file.txt', 'size': 12345}
                    },
                    'eventTime': '2025-04-12T12:34:56.789Z'
                }
            ]
        }

        # Call the handler
        response = lambda_handler(event, None)

        # Assert that process_s3_event was called
        mock_process_s3_event.assert_called_once()

        # Assert the response
        self.assertEqual(response['statusCode'], 200)
        self.assertIn('File metadata stored successfully!', response['body'])

if __name__ == '__main__':
    unittest.main()
