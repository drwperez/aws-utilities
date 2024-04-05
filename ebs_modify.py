'''
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
import boto3
import time

# Create a function to query the volumes
def query_ebs():
    try:
        client = boto3.client('ec2')
        response = client.describe_volumes()
        volumes = response['Volumes']
        for volume in volumes:
            volume_id = volume['VolumeId']
            volume_type = volume['VolumeType']
            volume_size = volume['Size']
            print(f"Volume ID: {volume_id}, Type: {volume_type}, Size: {volume_size}")
    except Exception as e:
        print(f"Error querying volumes: {e}")


# Modify the VolumeType from gp2 to gp2 if volumetype is gp2
def modify_ebs():
    try:
        client = boto3.client('ec2')
        response = client.describe_volumes()
        volumes = response['Volumes']
        for volume in volumes:
            volume_id = volume['VolumeId']
            volume_type = volume['VolumeType']
            if volume_type == 'gp2':
                response = client.modify_volume(VolumeId=volume_id, VolumeType='gp3')
                print(f"Volume {volume_id} modified to gp3")
            if volume_type == 'io1':
                response = client.modify_volume(VolumeId=volume_id, VolumeType='gp3')
                print(f"Volume {volume_id} modified to gp3")
    except Exception as e:
        print(f"Error modifying volumes: {e}")

# Call the function to query the volumes
query_ebs()

# Call the function to modify the volumes
modify_ebs()

# Create a delay function while the modify_ebs function is running
print(f"Waiting for the modify_ebs function to complete...")
time.sleep(30)  # Wait for 30 seconds before querying the volumes again to ensure the modify_ebs function has completed

# Call the function to query the volumes again after modifying the volumes.  May not reflect until after 2nd run
print(f"Querying the volumes after modifying the volumes...")
query_ebs()
