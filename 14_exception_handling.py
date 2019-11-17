import boto3

input_user_name=input("Enter a valid user name: ")
aws_con = boto3.session.Session(profile_name="venki_admin")
iam_re = aws_con.resource(service_name="iam")
user_obj = iam_re.User(name=input_user_name)
#print(dir(user_obj))
try:
    print(f"User ID: {user_obj.user_id}\nUser name: {user_obj.user_name}")
except Exception as e:
    #print(dir(e)) #STUDY THE EXCEPTION OBJECT FIRST
    #print(e.response) #Look at the output of some useful method
    print(f"{e.response['Error']['Code']}: {e.response['Error']['Message']}")