import boto3

session = boto3.Session(profile_name="localstack")
s3 = session.client("s3", endpoint_url="http://localhost:4566")
print(s3.list_buckets())
