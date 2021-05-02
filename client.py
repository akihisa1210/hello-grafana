from datetime import datetime
import os

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = os.environ["INFLUXDB_TOKEN"]
org = "test"
bucket = "test"

client = InfluxDBClient(url="http://localhost:8086", token=token)

# Write Data
write_api = client.write_api(write_options=SYNCHRONOUS)
data = "mem,host=host1 used_percent=23.43234543"
write_api.write(bucket, org, data)
