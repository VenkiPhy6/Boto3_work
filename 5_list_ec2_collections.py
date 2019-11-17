import boto3
import pprint

aws_con = boto3.session.Session(profile_name = "default")
ec2_con_re = aws_con.resource(service_name="ec2", region_name = "ap-south-1")
ec2_con_cli = aws_con.client(service_name="ec2", region_name = "ap-south-1")

print("Output using collections")
for each_ins in ec2_con_re.instances.all():
    print(each_ins.id)
print("Output using client dictionary")
#pprint.pprint(ec2_con_cli.describe_instances())    
for ins_list in ec2_con_cli.describe_instances()['Reservations']:
    for each_ins in ins_list['Instances']:
        print(each_ins['InstanceId'])
        
#ec2_con_re.Instance(id="i-04e21e871772cfc03").stop()