import boto3

aws_con = boto3.session.Session(profile_name="venki_admin")
ec2_con = aws_con.client(service_name="ec2", region_name="ap-south-1")
# I can do region operations only with the client

#print(ec2_con.describe_regions()) # checking the output for further coding

regions = []
for each_reg in ec2_con.describe_regions()['Regions']:
    regions.append(each_reg['RegionName'])
    
print(regions)