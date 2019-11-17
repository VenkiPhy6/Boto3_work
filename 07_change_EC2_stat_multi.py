import boto3

aws_con = boto3.session.Session(profile_name="default")
ec2_con_res = aws_con.resource(service_name="ec2", region_name="ap-south-1")
ec2_con_cli = aws_con.client(service_name='ec2', region_name='ap-south-1')

instance_id_list = []
for each_in in ec2_con_res.instances.all():
    instance_id_list.append(each_in.id)    

#With resource
ec2_con_res.instances.start(instance_id_list)
ec2_con_res.instances.stop(instance_id_list)
#With client    
ec2_con_cli.start_instances(InstanceIds=instance_id_list)
ec2_con_cli.stop_instances(InstanceIds=instance_id_list)

#BUT THE SCRIPT EXITS BEFORE THINGS ACTUALLY STOP OR START.

#Making waiter with the client object
cli_waiter1=ec2_con_cli.get_waiter('instance_running')
ec2_con_cli.start_instances(InstanceIds=instance_id_list)
cli_waiter1.wait(InstanceIds=instance_id_list)

cli_waiter2=ec2_con_cli.get_waiter('instance_stopped')
ec2_con_cli.stop_instances(InstanceIds=instance_id_list)
cli_waiter2.wait(InstanceIds=instance_id_list)
