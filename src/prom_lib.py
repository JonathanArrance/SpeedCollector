import logging
import pprint

from prometheus_client import start_http_server
from prometheus_client import Gauge

class prometheus():

    def __init__(self):
        """
        DESC: Initialize
        INPUT:
        OUTPUT: None
        """
        logging.info("Starting Prometheus scrape endpoint.")

    def start_server(self):
        start_http_server(9030)

        self.upload_speed = Gauge('upload_Mbps', 'Uplaod speed MB/s',['location','country','server','isp','providername','server_ip','internal_ip','external_ip','hostname','mac','interface'])
        self.download_speed = Gauge('download_Mbps', 'Download speed MB/s',['location','country','server','isp','providername','server_ip','internal_ip','external_ip','hostname','mac','interface'])
        self.ping_latency = Gauge('pinglatency', 'Ping latency in ms',['location','country','server','isp','providername','server_ip','internal_ip','external_ip','hostname','mac','interface'])
        self.upload_latency = Gauge('uplatency', 'Upload latency in ms',['location','country','server','isp','providername','server_ip','internal_ip','external_ip','hostname','mac','interface'])
        self.download_latency = Gauge('downlatency', 'Download latency in ms',['location','country','server','isp','providername','server_ip','internal_ip','external_ip','hostname','mac','interface'])
        self.packet_loss = Gauge('packetloss', 'Packet loss',['location','country','server','isp','providername','server_ip','internal_ip','external_ip','hostname','mac','interface'])
    
    def current_speed(self,input_dict):
        pprint.pprint(input_dict)
        try:
            logging.info("Emitting speedtest metrics.")
            self.upload_speed.labels(input_dict['location'],input_dict['country'],input_dict['server'],input_dict['isp'],input_dict['providername'],input_dict['server_ip'],input_dict['internal_ip'],input_dict['external_ip'],input_dict['hostname'],input_dict['mac'],input_dict['interface']).set(input_dict['upload_Mbps'])
            self.download_speed.labels(input_dict['location'],input_dict['country'],input_dict['server'],input_dict['isp'],input_dict['providername'],input_dict['server_ip'],input_dict['internal_ip'],input_dict['external_ip'],input_dict['hostname'],input_dict['mac'],input_dict['interface']).set(input_dict['download_Mbps'])
            self.ping_latency.labels(input_dict['location'],input_dict['country'],input_dict['server'],input_dict['isp'],input_dict['providername'],input_dict['server_ip'],input_dict['internal_ip'],input_dict['external_ip'],input_dict['hostname'],input_dict['mac'],input_dict['interface']).set(input_dict['pinglatency'])
            self.upload_latency.labels(input_dict['location'],input_dict['country'],input_dict['server'],input_dict['isp'],input_dict['providername'],input_dict['server_ip'],input_dict['internal_ip'],input_dict['external_ip'],input_dict['hostname'],input_dict['mac'],input_dict['interface']).set(input_dict['uplatency'])
            self.download_latency.labels(input_dict['location'],input_dict['country'],input_dict['server'],input_dict['isp'],input_dict['providername'],input_dict['server_ip'],input_dict['internal_ip'],input_dict['external_ip'],input_dict['hostname'],input_dict['mac'],input_dict['interface']).set(input_dict['downlatency'])
            self.packet_loss.labels(input_dict['location'],input_dict['country'],input_dict['server'],input_dict['isp'],input_dict['providername'],input_dict['server_ip'],input_dict['internal_ip'],input_dict['external_ip'],input_dict['hostname'],input_dict['mac'],input_dict['interface']).set(input_dict['packetloss'])
        except Exception as e:
            logging.error(e)
            logging.error("Could not emit speedtest metrics.")