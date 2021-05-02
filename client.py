import os
import json

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

token = os.environ["INFLUXDB_TOKEN"]
org = "test"
bucket = "test"

client = InfluxDBClient(url="http://localhost:8086", token=token, org=org)

write_api = client.write_api(write_options=SYNCHRONOUS)

f = open('test-weather-data.json', 'r')
weather = json.load(f)
weather_hourly = weather["hourly"]
for k in weather_hourly:
    data = f'weather,location=Tokyo temperature={k["temp"] - 273.15} {k["dt"]}000000000'
    print(data)
    write_api.write(bucket, org, data)

query_api = client.query_api()
query = '''from(bucket: "test")
  |> range(start: -48h)
  |> filter(fn: (r) => r["_measurement"] == "weather")
  |> filter(fn: (r) => r["_field"] == "temperature")
  |> filter(fn: (r) => r["location"] == "Tokyo")'''
print(query)  # debug
result = query_api.query(query)
for table in result:
    for record in table.records:
        print('max {0:5} = {1}'.format(record.get_field(), record.get_value()))
