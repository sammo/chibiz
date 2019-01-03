# Set up db password file
mv .pgpass ~/
chmod 0600 ~/.pgpass

# Check if db doesn't exist
if ! psql -lqt -h $DBHOST -p $DBPORT -U postgres | grep -i $DBNAME > /dev/null; then
    # Create db
    createdb -E UTF8 -O postgres -h $DBHOST -p $DBPORT -U postgres $DBNAME
    echo "Database" $DBNAME "created."

    # Create db tables
    psql -h $DBHOST -p $DBPORT -d $DBNAME -U postgres -f raw_json.pgsql
    psql -h $DBHOST -p $DBPORT -d $DBNAME -U postgres -f business_license.pgsql
    echo "Tables created."

    # Get initial data
    curl -X GET -H "X-App-Token=$APP_TOKEN" https://$DATA_DOMAIN/resource/$DATA_ID.json?\$limit=$INITIAL_DATA_LIMIT > $INITIAL_DATA_FILE

    # Json injestion into postgres db table
    cat test.json | psql -U postgres -h $DBHOST -p $DBPORT -d $DBNAME -c 'COPY raw_json (json_data) FROM STDIN;'
else
    echo "Database" $DBNAME "already exists."
fi
