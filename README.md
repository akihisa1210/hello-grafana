# hello-grafana

Getting started to Grafana

## Start Grafana and InfluxDB

```sh
docker-compose up -d
./setup-influxdb.sh
```

## Get InfluxDB token

1. Open InfluxDB GUI (`localhost:8086`). Username and password is written in `setup-influxdb.sh`.
2. Get token.

## Send data to InfluxDB

```sh
INFLUXDB_TOKEN=(your InfluxDB token)
poetry config virtualenvs.in-project true
poetry install
poetry run python client.py
```

## Integrate InfluxDB with grafana

1. Open Grafana (admin/admin).
2. Add InfluxDB as data source.
   - URL is `http://influxdb:8086`.
   - Query language is "Flux".
   - Specify "Organization", "Token" in InfluxDB Details.
3. Add a dashboard.
4. Add a panel whose data source if InfluxDB.
   - You need to write Flux query to display data. See `client.py`.
