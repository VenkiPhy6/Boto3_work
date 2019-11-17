import boto3

aws_con = boto3.session.Session(profile_name="venki_admin")
ec2_re = aws_con.resource(service_name="ec2", region_name="ap-south-1")

vol_filter = {'Name':'status', 'Values':['available']}

vols_to_delete = []
for each_vol in ec2_re.volumes.filter(Filters=[vol_filter]):
    vols_to_delete.append(each_vol.id)
    ######CAREFUL here!
    #ec2_re.Volume(each_vol.id).delete() 

vol_del_waiter=aws_con.client("ec2", "ap-south-1").get_waiter('volume_deleted')
vol_del_waiter.wait(VolumeIds=vols_to_delete)
print(f"Successfully deleted the following volumes with status 'available':\n{vols_to_delete}")