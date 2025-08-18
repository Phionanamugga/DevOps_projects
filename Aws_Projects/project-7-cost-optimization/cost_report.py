import boto3
client = boto3.client('ce', region_name='us-east-1')
response = client.get_cost_and_usage(
    TimePeriod={'Start':'2025-08-01','End':'2025-08-31'},
    Granularity='MONTHLY',
    Metrics=['UnblendedCost']
)
print(response)
