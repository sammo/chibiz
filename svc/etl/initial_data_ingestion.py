# Import global
import ijson
import psycopg2 as pg

# Import local
from config import (
    INITIAL_DATA_FILE,
    DSN,
    BATCH_SIZE,
)

# DB connection
conn = pg.connect(dsn=DSN)
cur = conn.cursor()

# Commit counter
cnt = 0

# Write json to db table
try:
    with open(INITIAL_DATA_FILE, 'r') as f:
        # Increase counter
        cnt += 1

        # Open ijson streamer
        objects = ijson.items(f, 'item')
        licenses = (o for o in objects)

        # Iterate through json items
        for lic in licenses:
            sql = """INSERT INTO business_license(
                id,
                license_id,
                account_number,
                site_number,
                legal_name,
                doing_business_as_name,
                address,
                city,
                state,
                zip_code,
                ward,
                precinct,
                ward_precinct,
                police_district,
                license_code,
                license_description,
                business_activity_id,
                business_activity,
                license_number,
                application_type,
                application_created_date,
                application_requirements_complete,
                payment_date,
                conditional_approval,
                license_start_date,
                expiration_date,
                license_approved_for_issuance,
                date_issued,
                license_status,
                license_status_change_date,
                ssa,
                latitude,
                longitude,
                business_location
                )

                values(
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s
                );
                """
            # Execute sql insert
            cur.execute(
                sql,
                (
                    lic.get('id'),
                    lic.get('license_id'),
                    lic.get('account_number'),
                    lic.get('site_number'),
                    lic.get('legal_name'),
                    lic.get('doing_business_as_name'),
                    lic.get('address'),
                    lic.get('city'),
                    lic.get('state'),
                    lic.get('zip_code'),
                    lic.get('ward'),
                    lic.get('precinct'),
                    lic.get('ward_precinct'),
                    lic.get('police_district'),
                    lic.get('license_code'),
                    lic.get('license_description'),
                    lic.get('business_activity_id'),
                    lic.get('business_activity'),
                    lic.get('license_number'),
                    lic.get('application_type'),
                    lic.get('application_created_date'),
                    lic.get('application_requirements_complete'),
                    lic.get('payment_date'),
                    lic.get('conditional_approval'),
                    lic.get('license_start_date'),
                    lic.get('expiration_date'),
                    lic.get('license_approved_for_issuance'),
                    lic.get('date_issued'),
                    lic.get('license_status'),
                    lic.get('license_status_change_date'),
                    lic.get('ssa'),
                    lic.get('latitude'),
                    lic.get('longitude'),
                    str(lic.get('location'))
                )
            )

            # Commit every 1000
            if (cnt % BATCH_SIZE == 0):
                conn.commit()

except:
    print(lic)
    cur.close()
    conn.rollback()
    raise

# Commit last inserts
conn.commit()
cur.close()
conn.close()
