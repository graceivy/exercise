import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

# refrenence: https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway-code.html

dynamodb = boto3.resource(
    'dynamodb',
    region_name='us-east-1',
    aws_access_key_id='',
    aws_secret_access_key='',
    )
table = dynamodb.Table('Food')

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):                # pylint: disable=E0202
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

def lambda_handler(event, context):
    headers = {
        "Content-Type": "application/json"
    };
    try:
        if event["routeKey"] == 'GET /items/{name}':
            response = table.get_item(
                Key={
                    'name': event["pathParameters"]["name"]
                }
            )
            item = response['Item']
            statusCode = 200
            body = json.dumps(item, indent=4, cls=DecimalEncoder)
            
        elif event["routeKey"] == 'GET /items':
            response = table.scan()
            data = response['Items']
            while 'LastEvaluatedKey' in response:
                response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
                data.extend(response['Items'])
            statusCode = 200
            body = json.dumps(data, indent=4, cls=DecimalEncoder)
            
        elif event["routeKey"] == 'PUT /items':
            # https://stackoverflow.com/questions/67339656/json-payload-aws-lambda-python-api-gateway
            requestJSON = json.loads("{}".format(event['body']))
            response = table.put_item(
                Item={
                    "name": requestJSON["name"],
                    "type": requestJSON["type"],
                    "rank": requestJSON["rank"]
                }
            )
            statusCode = 204
            body = 'Added the item'
            
        elif event["routeKey"] == 'DELETE /items/{name}':
            response = table.delete_item(
                Key={
                    'name': event["pathParameters"]["name"]
                }
            )
            statusCode = 204
            body = 'Delete the item'
    except ClientError as e:
        body = e.response['Error']['Message']
        statusCode = 400

    return {
    "statusCode":statusCode,
    "body":body,
    "headers": headers
  };