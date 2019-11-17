import boto3

aws_con = boto3.session.Session(profile_name="default")
ec2_con = aws_con.resource(service_name="ec2", region_name="ap-south-1")

f1 = {'Name':'instance-type','Values':['t2.micro']}
f2 = {'Name':'tag:Context2', 'Values':['boto3_course_filter']}
f3 = {'Name':'tag:Context', 'Values':['boto3_course']}
for each_ins in ec2_con.instances.filter(Filters=[f2]):
    print(each_ins.id, each_ins.state)

for each_ins in ec2_con.instances.filter(Filters=[f3], InstanceIds=['i-055e5e7a6aac1f0c4'], DryRun=True):
    print(each_ins.id, each_ins.state)
