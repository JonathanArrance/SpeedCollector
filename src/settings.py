import os

#default to 1 hour
INTERVAL = (os.getenv('INTERVAL',60) * 60) * 60
SERVER = os.getenv('SERVER','rdu.ookla.gfsvc.com')
INTERFACE = os.getenv('INTERFACE','eth0')
FORMAT = os.getenv('FORMAT','json')