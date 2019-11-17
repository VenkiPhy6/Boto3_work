import boto3

AWS_con = boto3.session.Session(profile_name="default")
EC2_con = AWS_con.resource("ec2", region_name = "ap-south-1")

#For a single instance
EC2_ins1 = EC2_con.Instance(id = "i-055e5e7a6aac1f0c4")
print(EC2_ins1.id, EC2_ins1.state)

#For all instances
for i in EC2_con.instances.all():
    print(i.id, i.state['Name'])
