# Import global
import pandas as pd
from sodapy import Socrata
import ijson

# Import local
from config import (
    DATA_DOMAIN,
    DATA_ID,
    APP_TOKEN,
    DATA_FILE,
)

# Load initial data
df = list()
with open(DATA_FILE, 'r') as d:
    while True:
        line = d.readline()
        if not line:
            break
        import pdb
        pdb.set_trace()
        df.append(line)

# Load initial json data
with open(DATA_FILE, 'r') as f:
    d = f.readline(1000)

# Get json data
client = Socrata(DATA_DOMAIN, APP_TOKEN)
results = client.get(DATA_ID, limit=10000)

# Load json into pandas dataframe
df = pd.DataFrame(results)
df.head()

# Get list of all datasets
chi_datasets = client.datasets()

# Get set of categories
categories = [i for k, v in enumerate(chi_datasets, 0)
              for i in chi_datasets[k]['classification']['categories']]
categories = set(categories)

d_list = list()
with open('test.json', 'r') as f:
    businesses = ijson.items(f, 'item')
    for business in businesses:
        d_list.append(business)
