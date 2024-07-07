import json
import boto3
import base64
import os

ENDPOINT = "image-classification-2024-07-07-06-37-14-799"
CONTENT_TYPE = "image/png"

def lambda_handler(event, context):
    client = boto3.client('sagemaker-runtime')
    image = event["body"]["image_data"]

    image = base64.b64decode(image)

    # Make a prediction:
    inferences  = client.invoke_endpoint(EndpointName=ENDPOINT, 
                                  ContentType=CONTENT_TYPE, 
                                  Body=image)
    
    # We return the data back to the Step Function as a JSON format
    event["inferences"] = inferences['Body'].read().decode('utf-8')
    event["inferences"] = json.loads(event["inferences"])
    return {
        'statusCode': 200,
        'body':  json.dumps(event["inferences"])
    }

import json
import boto3
import base64
import os

ENDPOINT = "image-classification-2024-07-07-06-37-14-799"
CONTENT_TYPE = "image/png"

def lambda_handler(event, context):
    client = boto3.client('sagemaker-runtime')
    image = event["body"]["image_data"]

    image = base64.b64decode(image)

    # Make a prediction:
    inferences  = client.invoke_endpoint(EndpointName=ENDPOINT, 
                                  ContentType=CONTENT_TYPE, 
                                  Body=image)
    
    # We return the data back to the Step Function as a JSON format
    event["inferences"] = inferences['Body'].read().decode('utf-8')
    event["inferences"] = json.loads(event["inferences"])
    return {
        'statusCode': 200,
        'body':  json.dumps(event["inferences"])
import json


THRESHOLD = .93


def lambda_handler(event, context):
    
    # Grab the inferences from the event
    
    inferences = json.loads(event['body'])

    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = max(inferences) >= THRESHOLD
    
    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }