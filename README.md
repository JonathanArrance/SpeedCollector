# SpeedCollector

The Speedcollector utilizes the Ookla Speedtest utility to measure the upload and download speed from your network on a given interval and track the measurments with Prometheus.

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

```bash
scrape_configs:

  - job_name: 'speedtest'
    metrics_path: /metrics
    scrape_interval: 1h
    static_configs:
      - targets: ['MY_HOST:9030']
```

## Grafana Dashboard