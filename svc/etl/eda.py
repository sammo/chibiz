# Import global
import ijson
from datetime import datetime
import pandas as pd
import numpy as np
import csv

# Import local
from config import (
    INITIAL_DATA_FILE,
)

# Max vector
mx = [0] * 35

# Read stream from json file
with open(INITIAL_DATA_FILE, 'r') as f:
    objects = ijson.items(f, 'item')
    licenses = (o for o in objects)
    first_few = [licenses.__next__() for i in range(1000)]
    # for l in licenses:
    #     # Get number of characters
    #     x = [
    #         len(str(l.get('id'))),
    #         len(str(l.get('license_id'))),
    #         len(str(l.get('account_number'))),
    #         len(str(l.get('site_number'))),
    #         len(str(l.get('legal_name'))),
    #         len(str(l.get('doing_business_as_name'))),
    #         len(str(l.get('address'))),
    #         len(str(l.get('city'))),
    #         len(str(l.get('state'))),
    #         len(str(l.get('zipcode'))),
    #         len(str(l.get('ward'))),
    #         len(str(l.get('precinct'))),
    #         len(str(l.get('ward_precinct'))),
    #         len(str(l.get('police_district'))),
    #         len(str(l.get('license_code'))),
    #         len(str(l.get('license_description'))),
    #         len(str(l.get('business_activity_id'))),
    #         len(str(l.get('business_activity'))),
    #         len(str(l.get('license_number'))),
    #         len(str(l.get('application_type'))),
    #         len(str(l.get('application_created_date'))),
    #         len(str(l.get('application_requirements_complete'))),
    #         len(str(l.get('payment_date'))),
    #         len(str(l.get('conditional_approval'))),
    #         len(str(l.get('license_term_start_date'))),
    #         len(str(l.get('license_term_expiration_date'))),
    #         len(str(l.get('license_approved_for_issuance'))),
    #         len(str(l.get('date_issued'))),
    #         len(str(l.get('license_status'))),
    #         len(str(l.get('license_status_change_date'))),
    #         len(str(l.get('ssa'))),
    #         len(str(l.get('latitude'))),
    #         len(str(l.get('longitude'))),
    #         len(str(l.get('business_location'))),
    #         len(str(datetime.now()))
    #     ]
    # # Compare to max vector and update
    # mx = list(map(max, x, mx))

# # Dict keys
# keys = [
#         'id',
#         'license_id',
#         'account_number',
#         'site_number',
#         'legal_name',
#         'doing_business_as_name',
#         'address',
#         'city',
#         'state',
#         'zipcode',
#         'ward',
#         'precinct',
#         'ward_precinct',
#         'police_district',
#         'license_code',
#         'license_description',
#         'business_activity_id',
#         'business_activity',
#         'license_number',
#         'application_type',
#         'application_created_date',
#         'application_requirements_complete',
#         'payment_date',
#         'conditional_approval',
#         'license_term_start_date',
#         'license_term_expiration_date',
#         'license_approved_for_issuance',
#         'date_issued',
#         'license_status',
#         'license_status_change_date',
#         'ssa',
#         'latitude',
#         'longitude',
#         'business_location',
#         'datetime'
#         ]
# # Max values
# values = mx
# # Map into dict object
# d = dict(zip(keys, values))
# print(d)

df = pd.DataFrame(first_few)
measurer = np.vectorize(len)
m = measurer(df.values.astype(str)).max(axis=0)
f = csv.writer(open('data_len.csv', 'w'))
for key, val in dict(zip(df.columns, m)).items():
    f.writerow([key, val])
df.describe().to_csv('data_describe.csv')
