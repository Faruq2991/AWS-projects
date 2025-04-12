import unittest
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lambda_function import lambda_handler

class TestLambdaFunction(unittest.TestCase):
    def test_lambda_handler(self):
        # Mock S3 event
        event = {
            "Records": [{
                "s3": {
                    "bucket": {"name": "test-bucket"},
                    "object": {"key": "test-file.txt"}
                }
            }]
        }
        
        # Invoke lambda handler
        result = lambda_handler(event, None)
        
        # Verify results
        self.assertEqual(result['statusCode'], 200)
        body = json.loads(result['body'])
        self.assertIn('FileMetadata', body)
        
if __name__ == '__main__':
    unittest.main()
