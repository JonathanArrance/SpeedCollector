# SpeedCollector

The Speedcollector utilizes the Ookla Speedtest utility to measure the upload and download speed from your network on a given interval and track the measurments with Prometheus.

## Pre-reqs

**Prometheus**

[Install](https://prometheus.io/docs/prometheus/latest/installation/)

[Configs](https://prometheus.io/docs/prometheus/latest/configuration/configuration/)

[PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/)

**Grafana**

[Install](https://grafana.com/docs/grafana/latest/setup-grafana/installation/docker/)

[Configs](https://grafana.com/docs/grafana/latest/setup-grafana/configure-docker/)

## Standalone container

**Build**

The container can be built from the command line
```bash
docker build --no-cache -t speed-collector ./src/
```

or the build script can be used create a standard container image.
```bash
./build_container.sh
```

**Run**

NOTE: This can be changed to fit your environment.

Run the container with the following parameters
```bash
docker run -d -p 9030:9030 --network MY_CONTAINER_NETWORK --name speed-collector speed-collector:latest

#set -e INTERVAl if you want to take a measurement at a different interval. Default 60 minutes.
```

or use the shell script to run the container.
```bash
./run_container.sh
```

*NOTE:* You may need to change the parameters to work in your environment.

## Prometheus

In order to take measurements we will scrape the collector with Promethus.

Add the following config config to your Prometheus configuration file, or add a config that matches your environment to scrape the container.

NOTE: Make sure to use the same port defined when you deploy.

```bash
scrape_configs:

  - job_name: 'speedtest'
    metrics_path: /metrics
    scrape_interval: 1h
    static_configs:
      - targets: ['MY_HOST:9030']
```

## Grafana Dashboard

Use the Grafana dashboard to visualize the collected data.

<img src="./Images/example_dash.png">

Get the dashboard [here](https://github.com/JonathanArrance/SpeedCollector/tree/main/dashboard)