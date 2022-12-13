import boto3
import json
import decimal

# Create a table
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

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

# Load data to the table

table = dynamodb.Table('Movies')

with open("Test/python/aws/moviedata.json") as json_file:
    movies = json.load(json_file, parse_float = decimal.Decimal)
    for movie in movies:
        year = int(movie['year'])
        title = movie['title']
        info = movie['info']

        print("Adding movie:", year, title)

        table.put_item(
           Item={
               'year': year,
               'title': title,
               'info': info,
            }
        )
