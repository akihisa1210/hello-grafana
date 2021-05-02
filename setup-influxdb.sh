#/usr/bin/env bash
set -eu

docker-compose exec influxdb influx setup \
  --org test \
  --bucket test \
  --username admin \
  --password password \
  --force
