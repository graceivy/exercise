import boto3
ec2_client = boto3.client('ec2')

# Create a snapshot
ec2_client.create_snapshot(Description='first one', VolumeId='vol-0a709380da53d899b')

# Create a volume
ec2_client.create_volume(AvailabilityZone='us-east-1c', 
    Encrypted=True, 
    Size =12,
    SnapshotId='snap-0ece1af702d445749', 
    VolumeType='gp2')
    
# Find my own snapshots
response = ec2_client.describe_snapshots(OwnerIds=['self'])

resp = ec2_client.describe_snapshots(SnapshotIds=['snap-0ece1af702d445749'])

#Delete snapshots
for snapshot in response['Snapshots']:
    print(snapshot['SnapshotId'])
    ec2_client.delete_snapshot(SnapshotId=snapshot['SnapshotId'])
    
for snapshot in resp['Snapshots']:
    print(snapshot)

#Delete a volume
ec2_client.delete_volume(VolumeId='vol-0db0fa59153d4ac1e')