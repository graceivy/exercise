#!/usr/bin/env python3.7
import boto3
import os
import glob

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.create

aws_resource = boto3.resource("s3")
s3_resource = boto3.client("s3")

# create a bucket
# my_bucket = aws_resource.Bucket("pingpingbucket")
# response = my_bucket.create(
#     ACL='public-read',
#     CreateBucketConfiguration={
#         'LocationConstraint': 'us-east-2'
#     }
# )

# # list the buckets
# list(aws_resource.buckets.all())
# for bucket in aws_resource.buckets.all():
#     print(bucket.name)
    
# # find the creation date
# for bucket in s3_resource.list_buckets()["Buckets"]:
#     print(bucket["Name"])
#     creation_date = bucket["CreationDate"]
#     print(creation_date.strftime("%d%m%y_%H:%M:%s"))

# uplocad single file
# s3_resource.upload_file(Filename="Test/Python/aws/file_read.py", Bucket="pingpingbucket", Key="file_read.py")

# uplocad multiple files
cwd = os.getcwd()
# cwd = cwd + "/Test/Python/aws/"
# files = glob.glob(cwd + "*.py")

# for file in files:
#     s3_resource.upload_file(Filename=file, Bucket="pingpingbucket", Key=file.split("/")[-1])
    
# list objects
objects = s3_resource.list_objects(Bucket="pingpingbucket")["Contents"]

# if len(objects) > 0:
#     for object in objects:
#         print(object["Key"])

# delete single file
s3_resource.delete_object(Bucket="pingpingbucket", Key="s3.py")

# delete multiple files
for object in objects:
    s3_resource.delete_object(Bucket="pingpingbucket", Key=object["Key"])