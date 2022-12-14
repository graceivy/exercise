import boto3
ec2_resource = boto3.resource("ec2")
ec2_client = boto3.client('ec2')

# # Create an EC2
# ec2_resource.create_instances(ImageId='ami-0b0dcb5067f052a63', InstanceType='t2.micro', MaxCount=1, MinCount=1)

# # Create multiple EC2s
# ec2_resource.create_instances(ImageId='ami-0b0dcb5067f052a63', InstanceType='t2.micro', MaxCount=2, MinCount=2)

# Get all EC2 instances
response = ec2_client.describe_instances()
reservations = response["Reservations"]
# print(len(reservations))
ec2_list = []
for reservation in reservations:
    instances = reservation['Instances']
    # print(instances)
    for instance in instances:
        if (instance['InstanceId'] != 'i-0d2ce2304ab59d302'):
            ec2_list.append(instance['InstanceId'])
        # print(instance['InstanceId'])
print(ec2_list)

# # Terminate instances
# ec2_client.terminate_instances(InstanceIds=ec2_list)

    
# for instance in ec2_resource.instances.all():
#     print(instance.id)
