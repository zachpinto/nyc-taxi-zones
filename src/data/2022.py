import requests
import csv
import time

api_endpoint = "https://data.cityofnewyork.us/resource/qp3b-zxtp.csv?$query=SELECT%0A%20%20%60tpep_pickup_datetime%60%2C%0A%20%20%60tpep_dropoff_datetime%60%2C%0A%20%20%60passenger_count%60%2C%0A%20%20%60trip_distance%60%2C%0A%20%20%60pulocationid%60%2C%0A%20%20%60dolocationid%60%2C%0A%20%20%60total_amount%60%0AWHERE%0A%20%20%60tpep_pickup_datetime%60%0A%20%20%20%20BETWEEN%20%222022-01-01T00%3A00%3A00%22%20%3A%3A%20floating_timestamp%0A%20%20%20%20AND%20%222023-01-01T00%3A00%3A00%22%20%3A%3A%20floating_timestamp"

with open('../../data/raw/2022.csv', 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    while True:
        response = requests.get(api_endpoint)
        if response.status_code != 200:
            print("Error fetching data: ", response.status_code)
            break

        data = response.text.splitlines()
        for row in data[1:]:  # Skip header after the first page
            writer.writerow(row.split(','))

    print("Done!")
