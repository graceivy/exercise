#SNS
import json
import boto3

def lambda_handler(event, context):
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName="test")
    sns = boto3.client('sns')
    
    number = queue.attributes.get('ApproximateNumberOfMessages')
    
    if int(number) > 0:
        print("ApproximateNumberOfMessages:", number)

    for message in queue.receive_messages(MaxNumberOfMessages=10):
        print(message.body)
        sns.publish(TopicArn="arn:aws:sns:us-east-1:676490034575:test_sns", Message=message.body)
        
#SQS
import boto3
from datetime import datetime
import json

def lambda_handler(event, context):
    sqs = boto3.resource('sqs')
    timestamp = datetime.utcnow().replace(microsecond=0).isoformat()
    queue = sqs.get_queue_by_name(QueueName='test')
    message = "The time now is: " + timestamp

    if event["routeKey"] == 'POST /':
        # Create a new message
        response = queue.send_message(MessageBody=message)
        
        # The response is NOT a resource, but gives you a message ID and MD5
        print(response.get('MessageId'))
        print(response.get('MD5OfMessageBody'))
    
    
        print(event)
        
        print(json.dumps(event))
        
        resp_api = {
            "statusCode":201,
            "body":"recevied your post message",
            "headers": {"Content-Type": "application/json"}
        }
    
        return resp_api

