import boto3

aws_con = boto3.session.Session(profile_name = "default")
ec2_con = aws_con.resource(service_name="ec2", region_name = "ap-south-1")
ec2_ins = ec2_con.Instance(id="i-055e5e7a6aac1f0c4")
print(ec2_ins.tags)