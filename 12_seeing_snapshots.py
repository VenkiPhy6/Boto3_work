import boto3

aws_con=boto3.session.Session(profile_name="venki_admin")
ec2_re=aws_con.resource(service_name="ec2", region_name="ap-south-1")
ec2_cli=aws_con.client(service_name="ec2", region_name="ap-south-1")

##To vomit everything!
#cnt=1
#for each_snap in ec2_re.snapshots.all():
#    print(cnt, each_snap)
#    cnt+=1

sts_cli=aws_con.client(service_name='sts')
AccId=sts_cli.get_caller_identity()['Account']

##Print only those owned by me
#With resource object
for each_snap in ec2_re.snapshots.filter(OwnerIds=[AccId]):
    print(each_snap)

#With client object
for each_snap in ec2_cli.describe_snapshots(OwnerIds=[AccId])['Snapshots']:
    print(each_snap['SnapshotId'])