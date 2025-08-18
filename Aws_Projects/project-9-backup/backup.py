import boto3, datetime
ec2 = boto3.client('ec2')
now = datetime.datetime.utcnow().strftime('%Y-%m-%d-%H-%M')
instances = ['i-1234567890abcdef0']
for instance in instances:
    response = ec2.create_snapshot(Description=f"Backup {now}", VolumeId="vol-12345678")
    print(response)
