import os

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

token = os.environ["INFLUXDB_TOKEN"]
org = "test"
bucket = "test"

client = InfluxDBClient(url="http://localhost:8086", token=token, org=org)

write_api = client.write_api(write_options=SYNCHRONOUS)
p = Point("my_measurement").tag(
    "location", "Prague").field("temperature", 25.3)
write_api.write(bucket=bucket, record=p)

query_api = client.query_api()
query = '''from(bucket: "test")
  |> range(start: -24h)
  |> filter(fn: (r) => r["_measurement"] == "mem")
  |> filter(fn: (r) => r["_field"] == "used_percent")
  |> filter(fn: (r) => r["host"] == "host1")'''
print(query)  # debug
result = query_api.query(query)
for table in result:
    for record in table.records:
        print('max {0:5} = {1}'.format(record.get_field(), record.get_value()))
