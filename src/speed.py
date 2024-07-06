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

    args = None
    while True:
        if platform.processor() == 'aarch64' and platform.system == 'Linux':
            args = ['/usr/bin/linuxarm/speedtest-arm', '--accept-license','-I', '-p', 'no', '-f', 'json']
        if platform.processor() == 'x86_64' and platform.system == 'Linux':
            args = ['/usr/bin/linux/speedtest-x86', '--accept-license','-I', '-p', 'no', '-f', 'json']
        
        try:
            cmd = subprocess.Popen(args, stdout=subprocess.PIPE)
            output = json.loads(cmd.communicate()[0].decode("utf-8").rstrip())
        except Exception as e:
            logging.error("speedtest error: %s"%e)
            output = 'ERROR'
            
        pr.current_speed(output)
        time.sleep(settings.INTERVAL)

if __name__ == '__main__':
    main()