import boto3
from pprint import pprint

aws_con = boto3.session.Session(profile_name="venki_admin")
iam_re = aws_con.resource(service_name="iam")
iam_cli = aws_con.client(service_name="iam")

#With resource
for group_obj in iam_re.groups.all():
    print(f"Group ID: {group_obj.group_id}\nUser name: {group_obj.group_name}")

#With client
#pprint(iam_cli.list_groups())
for each_group in iam_cli.list_groups()['Groups']:  
    print(f"User ID: {each_group['GroupId']}\nUser name: {each_group['GroupName']}")