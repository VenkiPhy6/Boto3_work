import boto3

input_user_name=input("Enter a valid user name: ")
aws_con = boto3.session.Session(profile_name="venki_admin")
iam_re = aws_con.resource(service_name="iam")
user_obj = iam_re.User(name=input_user_name)
#print(dir(user_obj))
print(f"User ID: {user_obj.user_id}\nUser name: {user_obj.user_name}")