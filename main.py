# Import libraries
import pandas as pd
import os
from sodapy import Socrata

# Get json data
token = os.environ.get('DATASMARTS')
client = Socrata('data.cityofchicago.org', token)
results = client.get('xqx5-8hwx', limit=10000)

# Load json into pandas dataframe
df = pd.DataFrame(results)
df.head()

# Get list of all datasets
chi_datasets = client.datasets()

# Get set of categories
categories = [i for k, v in enumerate(chi_datasets, 0)
              for i in chi_datasets[k]['classification']['categories']]
categories = set(categories)

# With requests package
import requests

headers = {'X-App-Token': os.environ.get('DATASMARTS'),
           'Accept': 'application/json'}
r = requests.get('https://data.cityofchicago.org/resource/xqx5-8hwx',
                 headers=headers)
results = r.content.decode('utf-8')
results