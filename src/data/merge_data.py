import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Retrieve database connection details from environment variables
db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

# Create a database connection
engine = create_engine(f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')

# List of CSV file paths
csv_files = ['/Users/pintoza/Desktop/dev/data-science/nyc-taxi-zones/data/raw/2018.csv',
             '/Users/pintoza/Desktop/dev/data-science/nyc-taxi-zones/data/raw/2019.csv',
             '/Users/pintoza/Desktop/dev/data-science/nyc-taxi-zones/data/raw/2020.csv',
             '/Users/pintoza/Desktop/dev/data-science/nyc-taxi-zones/data/raw/2021.csv',
             '/Users/pintoza/Desktop/dev/data-science/nyc-taxi-zones/data/raw/2022.csv']

# Loop through each CSV file and append the data to the database, by chunk
chunk_size = 10000  # You can adjust this size
for file in csv_files:
    for chunk in pd.read_csv(file, chunksize=chunk_size):
        # Reorder columns to match the database table structure
        chunk = chunk[['tpep_pickup_datetime',
                       'tpep_dropoff_datetime',
                       'passenger_count',
                       'trip_distance',
                       'total_amount',
                       'DOLocationID',
                       'PULocationID']]

        chunk.to_sql('taxi_trips', engine, if_exists='append', index=False)

print('Data merge complete!')
