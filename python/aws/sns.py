import boto3

client = boto3.client('sns')

# response = client.create_topic(Name='test_sns')
client.subscribe(TopicArn='arn:aws:sns:us-east-1:676490034575:test_sns', Protocol='email', Endpoint='graceivy@gmail.com')