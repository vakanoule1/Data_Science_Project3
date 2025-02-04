import requests
import json

import pandas as pd

#  Scraping in Python

URL = "https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=-21.72&longitude=-45.39&start_date=2022-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m,precipitation,surface_pressure"

# Make the GET request to the weather API using the `requests` package
response  = requests.get(URL)

#Convert the response to JSON
data = response.json()

# Check if the request is accepted
print(response.status_code)

# To view the data, we’ll use the response.json() method
data = response.json()
print(response.json())

# Create a json object
# Save this object into the path data/json.
with open("/Users/sa9/Desktop/Data_Science_Project3/weather_api/data/json/weather_api.json" , mode = "w") as file:
    json.dump(data, file, indent=4)

# Remove all meta_data
# Create new data containing time, temperature, relative humidity, precipitation, and surface_pressure
hourly_data = data['hourly']
data = {
    "time": hourly_data['time'],
    "temperature_2m": hourly_data['temperature_2m'],
    "relative_humidity_2m": hourly_data['relative_humidity_2m'],
    "precipitation": hourly_data['precipitation'],
    "surface_pressure": hourly_data['surface_pressure'],
}

# New DataFrame w/o metadata
df = pd.DataFrame(data)

# Convert json file w/0 metadata into CSV file.
df.to_csv('/Users/sa9/Desktop/Data_Science_Project3/weather_api/data/csv/weather_api.csv', index = False)

# Save dataframe in the specified path (/data/CSV/)
df = pd.read_csv("/Users/sa9/Desktop/Data_Science_Project3/weather_api/data/csv/weather_api.csv")
null_counts = df.isnull().sum()
print(null_counts)