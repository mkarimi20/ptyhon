import boto3
import json
import os
import time

# Used for global vars
key = ""
volume_id = ''
instanceId = ''
availability_zone = ''
instance_type = ''



def read_yaml_file(file):
    import yaml

    with open(file, 'r') as f:
        specs = yaml.safe_load(f)

    instance_type = specs['server']['instance_type']
    print(f"\nOur specs:\n\ninstance_type: {instance_type}")
    print(10*"===")

    volume_name1 = specs['server']["volumes"][0]['device']
    volume_size1 = specs['server']["volumes"][0]['size_gb']
    volume_mount1 = specs['server']["volumes"][0]['mount']

    print(f"1st_volume_name: {volume_name1}")
    print(f"1st_volume_size: {volume_size1}")
    print(f"1st_volume_mount: {volume_mount1}")
    print(10*"===")


    volume_name2 = specs['server']["volumes"][1]['device']
    volume_size2 = specs['server']["volumes"][1]['size_gb']
    volume_mount2 = specs['server']["volumes"][1]['mount']

    print(f"2nd_volume_name: {volume_name2}")
    print(f"2nd_volume_size: {volume_size2}")
    print(f"2nd_volume_mount: {volume_mount2}")
    print(10*"===")

    user = specs['server']['users'][0]['login']
    print(f"username: {user}\n")        # Read .yaml(specs) file

read_yaml_file('specs.yaml')



print(10*"===")
print("Creating key...")
def create_key(keyname):       # Generating ssh-key and save in a file
    ec2 = boto3.resource('ec2')
    filepath = os.path.join(os.getcwd(), keyname)
    global key
    key += os.path.basename(filepath)
    outfile = open(key,'w')
    key_pair = ec2.create_key_pair(KeyName=keyname)
    keypair = str(key_pair.key_material)
    outfile.write(keypair)
    time.sleep(3)

create_key('boto.pem')


print(10*"===")
print("Creating ec2...")
def create_ec2():           # Creating ec2 in AWS
    ec2 = boto3.resource('ec2')

    # creating user1
    user_data = '''
    #!/bin/bash
    useradd user1
    '''

    ami = 'ami-09d95fab7fff3776c'

    ec2.create_instances(ImageId=ami, InstanceType='t2.micro',
                         MinCount=1, MaxCount=1, SecurityGroupIds=['SSH'],
                         KeyName=key, UserData=user_data
                         )
    time.sleep(30)

create_ec2()




print(10*"===")
print("Attaching tags...")
def create_tags(tagname, tagvalue):         # Adding tag to the created ec2
    ec2 = boto3.client("ec2")

    reservations = ec2.describe_instances(
        Filters=[{'Name': 'instance-state-name',
                  'Values': ['running']}])["Reservations"]
    mytags = [{
        "Key" : tagname,
        "Value" : tagvalue
        }]
    for reservation in reservations :
        for each_instance in reservation["Instances"]:
            ec2.create_tags(
                Resources = [each_instance["InstanceId"] ],
                Tags= mytags
               )
    time.sleep(5)

create_tags('Name', 'boto3')



print(10*"===")
print("Describe instance...")
def describe_ec2():         # Info about ec2
    ec2 = boto3.client("ec2")

    global availability_zone
    global instanceId
    global instance_type

    reservations = ec2.describe_instances(
        Filters=[{'Name': 'instance-state-name',
                  'Values': ['running']}])["Reservations"]

    for reservation in reservations:
        for instances in reservation['Instances']:
            # print(instances)
            root_device_name = instances['RootDeviceName']
            instance_type += instances['InstanceType']
            tags = instances['Tags'][0].get('Value')
            instanceId += instances['InstanceId']
            availability_zone += instances['Placement'].get('AvailabilityZone')
            public_id += instances['NetworkInterfaces'][0].get('Association').get('PublicIp')


            print(f"\tDevice_name: {root_device_name}")
            print(f"\tInstance_type: {instance_type}")
            print(f"\tTag: {tags}")
            print(f"\tInstance ID: {instanceId}")
            print(f"\tAvailabilityZone: {availability_zone}")
            print(f"Public_IP: {public_id}")

    time.sleep(5)

describe_ec2()



print(10*"===")
print("Creating volume...")
def create_volume():            # Creating EBS
    ec2 = boto3.client("ec2")

    global volume_id

    # create an EBS volume, 10G size
    ebs_vol1 = ec2.create_volume(
            Size=10,
            AvailabilityZone=availability_zone
            )
    volume_id += ebs_vol1['VolumeId']

    # create an EBS volume, 100G size
    # ebs_vol2 = ec2.create_volume(
    #         Size=100,
    #         AvailabilityZone=availability_zone
    #         )
    # volume_id += ebs_vol2['VolumeId']

    time.sleep(20)

create_volume()



print(10*"===")
print("Attaching volume...")
def attach_volume():        # attaching EBS volume to our EC2 instance
    ec2 = boto3.client("ec2")

    attach_resp = ec2.attach_volume(
        VolumeId=volume_id,
        InstanceId=instanceId,
        Device='/dev/xvdf'              # Device name can be changed by aws
        )
    time.sleep(5)
    print('Done.')

attach_volume()


















# EOF
