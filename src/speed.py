import platform
import time
import settings
import subprocess
import logging
import json
from prom_lib import prometheus as prom

def main():

    pr = prom()
    pr.start_server()
    hostname = platform.node()

    args = None
    while True:
        if platform.processor() == 'aarch64' and platform.system() == 'Linux':
            args = ['/usr/bin/speedtest-arm', '--accept-license', '-p', 'no', '-f', 'json']
        if platform.processor() == 'x86_64' and platform.system() == 'Linux':
            args = ['/usr/bin/speedtest-x86', '--accept-license', '-p', 'no', '-f', 'json']

        try:
            cmd = subprocess.Popen(args, stdout=subprocess.PIPE)
            output = json.loads(cmd.communicate()[0].decode("utf-8").rstrip())
        except Exception as e:
            logging.error("speedtest error: %s"%e)
            output = 'ERROR'
        
        #upload megabytes
        up = ((int(output['upload']['bytes']) * 8) / int(output['upload']['elapsed'])) /1000

        #download megabytes
        down = ((int(output['download']['bytes']) * 8) / int(output['download']['elapsed'])) /1000
        
        upavg_latency = (float(output['upload']['latency']['high']) + float(output['upload']['latency']['low'])) / 2
        downavg_latency = (float(output['download']['latency']['high']) + float(output['download']['latency']['low'])) / 2

        #append the hostname to the returned dict.
        net = {   
                'upload_Mbps':str(up),
                'download_Mbps':str(down),
                'pinglatency':str(output['ping']['latency']),
                'uplatency':str(upavg_latency),
                'downlatency':str(downavg_latency),    
                'packetloss':str(output['packetLoss']),
                'location':str(output['server']['location']),
                'country':str(output['server']['country']),
                'server':str(output['server']['host']),
                'isp':str(output['isp']),
                'providername':str(output['server']['name']),
                'server_ip':str(output['server']['ip']),
                'internal_ip':str(output['interface']['internalIp']),
                'external_ip':str(output['interface']['externalIp']),
                'mac':str(output['interface']['macAddr']),
                'interface':str(output['interface']['name']),
                'hostname':str(hostname)
            }

        pr.current_speed(net)
        time.sleep(settings.INTERVAL)

if __name__ == '__main__':
    main()