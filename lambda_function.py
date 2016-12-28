import httplib
import urlparse
import json
import boto
from boto.exception import BotoServerError

from cfnresponse import send, SUCCESS, FAILED

def lambda_handler(event, context):
    ## allow CF template to be deleted easily if we make a mistake
    #send(event, context, SUCCESS)
    #return

    print("My event is " + str(event))
    print("My event type is " + str(type(event)))

    instance_profile_name = event['ResourceProperties']['InstanceProfileName']

    iam = boto.connect_iam()
    status = SUCCESS

    if event['RequestType'] == 'Delete':
        try:
            iam.delete_instance_profile(instance_profile_name)
        except BotoServerError as e:
            print("Could not find instance profile, assuming it has been removed "+ str(e))
            status=SUCCESS

        send(event, context, status)
        return

    # Example of returning data
    data = {'InstanceProfileName': instance_profile_name}

    try:
        iam.create_instance_profile(instance_profile_name)
    except BotoServerError as e:
        print("Failed to create "+ str(e))
        status = FAILED

    send(event, context, status, response_data=data)
