import boto3
# Get the service resource
sqs = boto3.resource('sqs')

from datetime import datetime

timestamp = datetime.utcnow().replace(microsecond=0).isoformat()

# # Create the queue. This returns an SQS.Queue instance
# queue = sqs.create_queue(QueueName='test', Attributes={'DelaySeconds': '5'})

# # You can now access identifiers and attributes
# print(queue.url)
# print(queue.attributes.get('DelaySeconds'))

# Get the queue
queue = sqs.get_queue_by_name(QueueName='test')

message = "Manually... The time now is: " + timestamp

# Create a new message
response = queue.send_message(MessageBody=message)

# The response is NOT a resource, but gives you a message ID and MD5
print(response.get('MessageId'))
print(response.get('MD5OfMessageBody'))