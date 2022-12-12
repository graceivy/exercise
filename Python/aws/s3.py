#!/usr/bin/env python3.7
import boto3

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.create
aws_resource = boto3.resource("s3")
my_bucket = aws_resource.Bucket("pingpingbucket")
response = my_bucket.create(
    ACL='public-read',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    }
)

list(aws_resource.buckets.all())

for bucket in aws_resource.buckets.all():
    print(bucket.name)
    
s3_resource = boto3.client("s3")

for bucket in s3_resource.list_buckets()["Buckets"]:
    print(bucket["name"])
    creation_date = bucket["CreationDate"]
    print(creation_date.strftime("%d%m%y_%H:%M:%s"))
