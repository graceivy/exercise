import boto3

# Boto3 documentation for Amazon Translate:
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate.html

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

### Change below this line only ###

kwargs={
    "Text":"I am learning to code in AWS",
    "SourceLanguageCode":"en",
    "TargetLanguageCode":"fr",
    "TerminologyNames":["Amazon_Family"]
    }

def main():
    translate_text(**kwargs)
    # or 
    # translate_text(Text='I am learning to code in AWS',SourceLanguageCode='en',TargetLanguageCode='fr')

if __name__=="__main__":
    main()