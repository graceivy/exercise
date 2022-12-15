import boto3
ec2_client = boto3.client('ec2')
ec2_client.create_snapshot(Description='first one', VolumeId='vol-0a709380da53d899b')
# ec2_client.create_volume()