import requests
import os
from dotenv import load_dotenv
import pandas as pd

API_URL = 'https://api.tfl.gov.uk'
CROWDING_URL = '{API_URL}/crowding/{Naptan}'
STATION_INFO_URL = '{API_URL}/StopPoint/Mode/tube'
load_dotenv(); app_key = os.getenv('PRIMARY_KEY')
DOW = ["TUE", "WED", "THU", "FRI"]

def get_crowding(naptan) -> tuple[bool, pd.DataFrame]:
    # This function could do with a rewrite
    url = CROWDING_URL.format(API_URL=API_URL, Naptan=naptan)
    data = requests.get(url, params={"app_key": app_key})

    if data.status_code != requests.codes.ok:
        return (True, None)

    if not data.json()["isFound"]:
         return (True, None)

    crowding = data.json()["daysOfWeek"]
    crowd_time_bands = []

    # Initialise array
    cwd = None
    for c in crowding:
         if c["dayOfWeek"] == "MON":
              cwd = c
              break

    # Populate dictionary with Monday data
    for band in cwd["timeBands"]:
        crowd_time_bands.append({
                "timeBand": band["timeBand"],
                "crowdingPercentage": 0.2 * band["percentageOfBaseLine"],
        })

    # Populate with day of week average            
    for cwd in crowding:
        if cwd["dayOfWeek"] in DOW:
             for i, band in enumerate(cwd["timeBands"]):
                  crowd_tb = crowd_time_bands[i]
                  crowd_tb["crowdingPercentage"] += 0.2 * band["percentageOfBaseLine"]

    crowding_df = pd.DataFrame.from_dict(crowd_time_bands)              

    return (False, crowding_df)

def get_all_stations_info() -> pd.DataFrame:
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
