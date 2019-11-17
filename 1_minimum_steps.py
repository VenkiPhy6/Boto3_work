import boto3

AWS_console = boto3.session.Session()

#ec2
ec2_con = AWS_console.resource(service_name="ec2", region_name="us-east1")
ec2_con = AWS_console.client(service_name="ec2", region_name="us-east1")

#s3
s3_con = AWS_console.resource(service_name="s3", region_name="us-east2")
s3_con = AWS_console.client(service_name="s3", region_name="us-east2")