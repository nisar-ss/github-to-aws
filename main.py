import requests
import pandas as pd
import boto3
import os
from io import StringIO

#API URL
url="https://jsonplaceholder.typicode.com/users"

#Fetch data
response = requests.get(url)
data = response.json()

#Convert to DataFrame
df = pd.DataFrame(data)

#Convert to CSV
csv_buffer=StringIO()
df.to_csv(csv_buffer,index=False)

#Upload to s3
s3 = boto3.client(
     's3',
     aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
     aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"]
)

s3.put_object(
    Bucket='s3bucket-demo-2\bronze',
    Key='data_customer.csv',
    Body=csv_buffer.getvalue()
)

print("File uploaded successfully")
