import boto3
import json
import decimal
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
## Create a table
# table = dynamodb.create_table(
#     TableName='Movies',
#     KeySchema=[
#         {
#             'AttributeName': 'year',
#             'KeyType': 'HASH'  #Partition key
#         },
#         {
#             'AttributeName': 'title',
#             'KeyType': 'RANGE'  #Sort key
#         }
#     ],
#     AttributeDefinitions=[
#         {
#             'AttributeName': 'year',
#             'AttributeType': 'N'
#         },
#         {
#             'AttributeName': 'title',
#             'AttributeType': 'S'
#         },

#     ],
#     ProvisionedThroughput={
#         'ReadCapacityUnits': 10,
#         'WriteCapacityUnits': 10
#     }
# )

# print("Table status:", table.table_status)

# # Load data to the table
# table = dynamodb.Table('Movies')

# with open("Test/python/aws/moviedata.json") as json_file:
#     movies = json.load(json_file, parse_float = decimal.Decimal)
#     for movie in movies:
#         year = int(movie['year'])
#         title = movie['title']
#         info = movie['info']

#         print("Adding movie:", year, title)

#         table.put_item(
#           Item={
#               'year': year,
#               'title': title,
#               'info': info,
#             }
#         )

# Create, Read, Update, and Delete an Item
# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):                # pylint: disable=E0202
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

table = dynamodb.Table('Movies')
title = "The Big New Movie"
year = 2015
        
# # Create a new item
# response = table.put_item(
#   Item={
#         'year': year,
#         'title': title,
#         'info': {
#             'plot':"Nothing happens at all.",
#             'rating': decimal.Decimal(0)
#         }
#     }
# )

# print("PutItem succeeded:")
# print(json.dumps(response, indent=4, cls=DecimalEncoder))

# # Read an Item

# try:
#     response = table.get_item(
#         Key={
#             'year': year,
#             'title': title
#         }
#     )
# except ClientError as e:
#     print(e.response['Error']['Message'])
# else:
#     item = response['Item']
#     print("GetItem succeeded:")
#     print(json.dumps(item, indent=4, cls=DecimalEncoder))

# # Update an Item
# response = table.update_item(
#     Key={
#         'year': year,
#         'title': title
#     },
#     UpdateExpression="set #info_rating=:r, #info_plot=:p, #info_actors=:a",
#     ExpressionAttributeNames={
#         '#info_rating': 'info.rating',
#         '#info_plot': 'info.plot',
#         '#info_actors': 'info.actors'
#     },
#     ExpressionAttributeValues={
#         ':r': decimal.Decimal(5.5),
#         ':p': "Everything happens all at once.",
#         ':a': ["Larry", "Moe", "Curly"]
#     },
#     ReturnValues="UPDATED_NEW"
# )

# print("UpdateItem succeeded:")
# print(json.dumps(response, indent=4, cls=DecimalEncoder))

# # Increment an Atomic Counter
# response = table.update_item(
#     Key={
#         'year': year,
#         'title': title
#     },
#     UpdateExpression="set #info_rating = #info_rating + :val",
#     ExpressionAttributeNames={
#         '#info_rating': 'info.rating',
#     },
#     ExpressionAttributeValues={
#         ':val': decimal.Decimal(1)
#     },
#     ReturnValues="UPDATED_NEW"
# )

# print("UpdateItem succeeded:")
# print(json.dumps(response, indent=4, cls=DecimalEncoder))

# # Update an Item (Conditionally)
# # Conditional update (will fail)
# print("Attempting conditional update...")

# try:
#     response = table.update_item(
#         Key={
#             'year': year,
#             'title': title
#         },
#         UpdateExpression="remove #info_actors[0]",
#         ConditionExpression="size(#info_actors) > :num",
#         ExpressionAttributeNames={
#             '#info_actors': 'info.actors'
#         },
#         ExpressionAttributeValues={
#             ':num': 3
#         },
#         ReturnValues="UPDATED_NEW"
#     )
# except ClientError as e:
#     if e.response['Error']['Code'] == "ConditionalCheckFailedException":
#         print(e.response['Error']['Message'])
#     else:
#         raise
# else:
#     print("UpdateItem succeeded:")
#     print(json.dumps(response, indent=4, cls=DecimalEncoder))

# # Delete an Item
# print("Attempting a conditional delete...")

# try:
#     response = table.delete_item(
#         Key={
#             'year': year,
#             'title': title
#         },
#         ConditionExpression="#info_rating <= :val",
#         ExpressionAttributeNames= {
#             "#info_rating": "info.rating"
#         },
#         ExpressionAttributeValues= {
#             ":val": decimal.Decimal(5)
#         }
#     )
# except ClientError as e:
#     if e.response['Error']['Code'] == "ConditionalCheckFailedException":
#         print(e.response['Error']['Message'])
#     else:
#         raise
# else:
#     print("DeleteItem succeeded:")
#     print(json.dumps(response, indent=4, cls=DecimalEncoder))

# # Query - All Movies Released in a Year
# response = table.query(
#     KeyConditionExpression=Key('year').eq(1985)
# )

# for i in response['Items']:
#     print(i['year'], ":", i['title'])
    
# # Query - All Movies Released in a Year with Certain Titles
# print("Movies from 1992 - titles A-L, with genres and lead actor")

# response = table.query(
#     ProjectionExpression="#yr, title, info.genres, info.actors[0]",
#     ExpressionAttributeNames={ "#yr": "year" }, # Expression Attribute Names for Projection Expression only.
#     KeyConditionExpression=Key('year').eq(1992) & Key('title').between('A', 'L')
# )

# for i in response[u'Items']:
#     print(json.dumps(i, cls=DecimalEncoder))

# # Scan
# fe = Key('year').between(1950, 1959)
# pe = "#yr, title, info.rating"
# # Expression Attribute Names for Projection Expression only.
# ean = { "#yr": "year", }
# esk = None


# response = table.scan(
#     FilterExpression=fe,
#     ProjectionExpression=pe,
#     ExpressionAttributeNames=ean
#     )

# # for i in response:
# #     print(json.dumps(i, cls=DecimalEncoder))

# # LastEvaluatedKey: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Scan.html
# # The scan method returns a subset of the items each time, called a page. 
# # The LastEvaluatedKey value in the response is then passed to the scan method via the ExclusiveStartKey parameter. 
# # When the last page is returned, LastEvaluatedKey is not part of the response.
# # while 'LastEvaluatedKey' in response:
#     response = table.scan(
#         ProjectionExpression=pe,
#         FilterExpression=fe,
#         ExpressionAttributeNames= ean,
#         ExclusiveStartKey=response['LastEvaluatedKey']
#         )
    
#     for i in response['Items']:
#         print(json.dumps(i, cls=DecimalEncoder))

# # Delete the table
# table.delete()