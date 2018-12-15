# Import global packages
import os

# Define variables
DATA_DOMAIN = os.environ.get('DATA_DOMAIN', 'data.cityofchicago.org')
DATA_ID = os.environ.get('DATA_ID', 'xqx5-8hwx')  # Chi Business licenses
APP_TOKEN = os.environ.get('APP_TOKEN', 'lek1JOcM5NsT29aL97QKF3EvK')

INITIAL_DATA_LIMIT = 2000000
DATA_FILE = 'business_licenses.json'
