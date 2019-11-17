#This script tells you how to run scripts inside an EC2 instance without configuring your EC2 instance with aws config commond.
#This is achieved by attaching an IAM user with an instance. 
#I did that and ran this code inside an SSH terminal of an EC2 instance.

import boto3 

#Since the EC2 instance is attached with a user, there is no need for a custom session.
ec2_re = boto3.resource(service_name="ec2", region_name="ap-south-1")
for each_ins in ec2_re.instances.all():
    print(each_ins.id)