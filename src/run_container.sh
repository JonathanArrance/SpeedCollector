#!/bin/bash -x
docker run -d -p 9030:9030 \
-e APIVER='beta' \
-e INTERVAL=15 \
--network container_net \
--name speed-collector \
speed-collector:latest