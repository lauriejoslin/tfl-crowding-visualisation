import requests
import os
from dotenv import load_dotenv
import pandas as pd

API_URL = 'https://api.tfl.gov.uk'
CROWDING_URL = '{API_URL}/crowding/{Naptan}/{DayOfWeek}'
STATION_INFO_URL = '{API_URL}/StopPoint/Mode/tube'
# Via https://techforum.tfl.gov.uk/t/application-id-and-key/3595 - add into query string
load_dotenv(); app_key = os.getenv('PRIMARY_KEY')

def get_crowding(naptan: str, dow: str):
    url = CROWDING_URL.format(API_URL=API_URL, Naptan=naptan, DayOfWeek=dow)
    data = requests.get(url, params=app_key)

    if data.status_code != requests.codes.ok:
        return "ERROR: Failed to fetch data, check query"

    return data

def get_all_stations_info():
    url = STATION_INFO_URL.format(API_URL=API_URL)
    data = requests.get(url, params={"app_key": app_key})

    if data.status_code != requests.codes.ok:
            return "ERROR: Failed to fetch data, check query"

    stops = data.json()["stopPoints"]

    stations = []
    for s in stops:
         if s["stopType"] == "NaptanMetroStation":
              stations.append(
                {
                    "name": s["commonName"],
                    "naptan": s["stationNaptan"],
                    "lat": s["lat"],
                    "lon": s["lon"],
                })

    station_df = pd.DataFrame.from_dict(stations)
    return station_df
