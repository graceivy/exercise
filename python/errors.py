import logging
import boto3
from botocore.exceptions import ClientError

kwargs={
    "Text":"I am learning to code in AWS",
    "SourceLanguageCode":"en",
    "TargetLanguageCode":"fr",
    "TerminologyNames":["Amazon_Family"]
    }

try:
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    

except ClientError as e:
    logging.warning("There is something wrong: {}".format(e))