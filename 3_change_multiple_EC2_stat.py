import boto3

aws_con = boto3.session.Session(profile_name='default')
ec2_con= aws_con.resource(service_name='ec2', region_name='ap-south-1')

#This one didn't exit even after the instance started!
f1 = {'Name':'instance-state-name', 'Values':['stopped']}
for each_ins in ec2_con.instances.filter(Filters=[f1]):
    each_ins.start()
    print(f"Your instance with id {each_ins.id} is starting. Please be patient")
    while each_ins.state['Name'] == 'pending':
        continue
    print(f"Your instance with id {each_ins.id}, has started")