import os

#default to 1 hour
INTERVAL = (os.getenv('INTERVAL',60) * 60) * 60