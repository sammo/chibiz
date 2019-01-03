# Import global packages
import os

# Define variables
DATA_DOMAIN = os.environ.get('DATA_DOMAIN', 'data.cityofchicago.org')
DATA_ID = os.environ.get('DATA_ID', 'xqx5-8hwx')  # Chi Business licenses
APP_TOKEN = os.environ.get('APP_TOKEN', 'lek1JOcM5NsT29aL97QKF3EvK')

INITIAL_DATA_LIMIT = 100
INITIAL_DATA_FILE = 'business_licenses.json'

DBHOST = os.environ.get('DBHOST', 'chibiz_db_1')
DBPORT = os.environ.get('DBPORT', 5432)
DBNAME = os.environ.get('DBNAME', 'chibizlic')
DBUSER = 'postgres'
DSN = 'host={} port={} dbname={} user={}'.format(DBHOST,
                                                 DBPORT,
                                                 DBNAME,
                                                 DBUSER)

BATCH_SIZE = os.environ.get('BATCH_SIZE', 1000)
