import boto3

aws_con = boto3.session.Session(profile_name="venki_admin")
sts_cli = aws_con.client(service_name='sts', region_name='ap-south-1')
print(sts_cli.get_caller_identity()['Account'])