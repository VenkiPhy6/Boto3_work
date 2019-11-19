import boto3

aws_con = boto3.session.Session(profile_name="venki_admin")
iam_re = aws_con.resource(service_name="iam")
iam_cli = aws_con.client(service_name="iam")

#With resource
for user_obj in iam_re.users.all():
    print(f"User ID: {user_obj.user_id}\nUser name: {user_obj.user_name}")

#With client
for each_user in iam_cli.list_users()['Users']:
    print(f"User ID: {each_user['UserId']}\nUser name: {each_user['UserName']}")

