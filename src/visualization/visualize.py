import folium
import pandas as pd
import os
import json

# Load weekly data
weekly_data = pd.read_csv('/Users/pintoza/Desktop/dev/data-science/taxi-demand-forecast/data/processed/weekly_zone_aggregates.csv')
weekly_data['PULocationID'] = weekly_data['PULocationID'].astype(str)  # Convert PULocationID to string for matching

# Create 'year_week' column combining 'year' and 'week'
weekly_data['year_week'] = weekly_data['year'].astype(str) + '-' + weekly_data['week'].astype(str)
weekly_data.sort_values(by='year_week', inplace=True)  # Sort the DataFrame by 'year_week'

# Load GeoJSON data
with open('/Users/pintoza/Desktop/dev/data-science/taxi-demand-forecast/data/external/NYC_Taxi_Zones.geojson') as f:
    geojson_data = json.load(f)

def get_color(passenger_count):
    if passenger_count > 1000:
        return '#ffaf08'
    elif passenger_count > 500:
        return '#f7b731'
    elif passenger_count > 250:
        return '#f5c767'
    elif passenger_count > 100:
        return '#f5d084'
    elif passenger_count > 50:
        return '#f2d8a2'
    elif passenger_count > 25:
        return '#f7e9cb'
    else:
        return '#ffffff'

maps_dir = '/Users/pintoza/Desktop/dev/data-science/taxi-demand-forecast/reports/maps/'
os.makedirs(maps_dir, exist_ok=True)

for year_week in weekly_data['year_week'].unique():
    m = folium.Map(location=[40.7128, -74.0060], zoom_start=11, tiles='Stamen Toner')
    week_data = weekly_data[weekly_data['year_week'] == year_week]

    def style_function(feature):
        location_id = str(feature['properties']['location_id'])
        passenger_count = week_data.loc[week_data['PULocationID'] == location_id, 'total_passengers'].sum()
        return {
            'fillColor': get_color(passenger_count),
            'color': 'black',  # Outline color
            'weight': 1,
            'fillOpacity': 0.7
        }

    folium.GeoJson(geojson_data, style_function=style_function).add_to(m)
    filename = os.path.join(maps_dir, f'week_{year_week}.html')
    m.save(filename)
