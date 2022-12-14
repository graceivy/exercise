import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

# Ask the user to provid the aws_access_key_id and aws_secret_access_key
keyId = input("Please enter your aws_access_key_id: ")
secretAccessKey = input("aws_secret_access_key: ")

dynamodb = boto3.resource(
    'dynamodb',
    region_name='us-east-1',
    aws_access_key_id=keyId,
    aws_secret_access_key=secretAccessKey,
    )

# Create a table
table = dynamodb.create_table(
    TableName='Food',
    KeySchema=[
        {
            'AttributeName': 'name',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'type',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'name',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'type',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

table = dynamodb.Table('Food')

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):                # pylint: disable=E0202
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

# Add 11 items to the table
with open("Test/python/aws/fooddata.json") as json_file:
    foods = json.load(json_file, parse_float = decimal.Decimal)
    for food in foods:
        name = food['name']
        kind = food['type']
        rank = food['rank']

        print("Adding food:", name, kind)

        table.put_item(
          Item={
              'name': name,
              'type': kind,
              'rank': rank
            }
        )

# Scan the table by rank=1
fe = Attr('rank').eq(1)
pe = "#nm, #tp, #rn"
ean = { "#nm": "name", "#tp": "type", "#rn": "rank"}

response = table.scan(
    FilterExpression=fe,
    ProjectionExpression=pe,
    ExpressionAttributeNames=ean
    )

for i in response['Items']:
    print(json.dumps(i,cls=DecimalEncoder))

# The scan method returns a subset of the items each time, called a page. 
while 'LastEvaluatedKey' in response:
    response = table.scan(
        ProjectionExpression=pe,
        FilterExpression=fe,
        ExpressionAttributeNames= ean,
        ExclusiveStartKey=response['LastEvaluatedKey']
        )
    
    for i in response['Items']:
        print(json.dumps(i, cls=DecimalEncoder))
        
# Query the table by name='lobster'
response = table.query(
    KeyConditionExpression=Key('name').eq('lobster')
)

for i in response['Items']:
    print(json.dumps(i, cls=DecimalEncoder))
    
# Remove an item by name='fish'
response = table.delete_item(
    Key={
        'name': 'fish',
        'type': 'seafood'
    }
)

# Add an item
response = table.put_item(
  Item={
        'name': 'scallop',
        'type': 'seafood',
        'rank': 3
    }
)

# Update the item(name='riceroll')'s rank to 3
response = table.update_item(
    Key={
        'name': 'riceroll',
        'type': 'breadfast'
    },
    UpdateExpression="set #rn=:r",
    ExpressionAttributeNames={
        '#rn': 'rank'
    },
    ExpressionAttributeValues={
        ':r': decimal.Decimal(3)
    },
    ReturnValues="UPDATED_NEW"
)

# Read an item
try:
    response = table.get_item(
        Key={
            'name': 'riceroll',
            'type': 'breadfast'
        }
    )
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    item = response['Item']
    print("GetItem succeeded:")
    print(json.dumps(item, indent=4, cls=DecimalEncoder))

# Delete the table
table.delete()