import boto3
import os
s3 = boto3.client('s3')
download_dir = os.path.join("/home/ec2-user/environment", "big15.jpeg")
s3.download_file("pingpingbucket-source", "big15.jpeg", download_dir)