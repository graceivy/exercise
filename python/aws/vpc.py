import boto3

client = boto3.client("ec2")

# # Create a VPC
# client.create_vpc(CidrBlock='10.0.0.0/16')

# Describe all the VPCs
obj = client.describe_vpcs()

print(len(obj["Vpcs"]))

for vpc in obj["Vpcs"]:
    print(vpc["VpcId"])
    
print(client.describe_vpcs(VpcIds=["vpc-0cdcf919ce6c16c3c"]))

# Remove VPC
response = client.delete_vpc(VpcId='vpc-0cdcf919ce6c16c3c')
print(response)