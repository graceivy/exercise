import requests
import time
import boto3
url = 'https://gplunhy8td.execute-api.us-east-1.amazonaws.com/'

url1 = "https://12dyfeyez4.execute-api.us-east-1.amazonaws.com/Prod/cart/add"
url2 = "https://12dyfeyez4.execute-api.us-east-1.amazonaws.com/Prod/cart/purchase"
url3 = "https://12dyfeyez4.execute-api.us-east-1.amazonaws.com/Prod/products/123456"
# myobj = {'somekey': 'somevalue'}

# while True:
#     # x = requests.post(url)
#     # time.sleep(0.1)
#     # print(x.text)

#     requests.get(url1)
#     requests.get(url2)
#     requests.get(url3)
#     time.sleep(0.01)

r= requests.get('https://api.agify.io?name=bella')
print (r.text)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Flask')