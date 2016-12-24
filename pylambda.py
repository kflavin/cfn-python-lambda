from __future__ import print_function

import json
import requests

print('Loading function')


def lambda_handler(event, context):
    print(dir(context))
    print(context.log_stream_name)
    d = {
       "Status": "SUCCESS",
       "PhysicalResourceId": context.log_stream_name,
       "StackId": event.get("StackId"),
       "RequestId": event.get("RequestId"),
       "LogicalResourceId": event.get("LogicalResourceId"),
       "Data": {}
       }
   
    print(event)
    print(context)
    return json.dumps(d)
