# Import global
import os

# Import local
from config import (
    DATA_DOMAIN,
    DATA_ID,
    APP_TOKEN,
    DATA_FILE,
    INITIAL_DATA_LIMIT
)

# Load initial data if not exists
if not os.path.isfile(DATA_FILE):
    curl_cmd = 'curl -X GET -H "X-App-Token={0}" \
        {1}/resource/{2}?$limit={3} > {4}' \
        .format(APP_TOKEN, DATA_DOMAIN, DATA_ID,
                INITIAL_DATA_LIMIT, DATA_FILE)
    os.system(curl_cmd)
