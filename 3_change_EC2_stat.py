import boto3

aws_con = boto3.session.Session(profile_name = 'default')
ec2_con = aws_con.resource("ec2", region_name="ap-south-1")

ec2_ins1 = ec2_con.Instance(id = "i-055e5e7a6aac1f0c4")
print(f"Current status of {ec2_ins1.id}:", ec2_ins1.state['Name'])
print(ec2_ins1.reboot())
#if ec2_ins1.state['Name'] == "running":
#    print(ec2_ins1.stop())
#
#if ec2_ins1.state['Name'] == "stopped":
#    print(ec2_ins1.start())


#ec2_ins2 = ec2_con.Instance(id = "i-0906fa316954702e8")
#print(f"Current status of {ec2_ins2.id}:", ec2_ins2.state['Name'])
#print(ec2_ins2.terminate())