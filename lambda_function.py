import httplib
import urlparse
import json
import boto3

from cfnresponse import send, SUCCESS

def lambda_handler(event, context):
    if event['RequestType'] == 'Delete':
        send(event, context, SUCCESS)
        return

    data = {'key1': 'value1'}

    send(event, context, SUCCESS, response_data=data)
