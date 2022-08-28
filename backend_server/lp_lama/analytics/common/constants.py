import os
import time
from pathlib import Path

os.environ['TZ'] = 'GMT'
time.tzset()

DATA_FOLDER = Path("_data")
KEYS_FOLDER = Path("data_account_keys")
DEFAULT_ADDRESS = "default_address"
