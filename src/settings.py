import os

#default to 1 hour
INTERVAL = os.getenv('COINBASE_KEY',1)
INTERVAL = (INTERVAL * 60) * 60