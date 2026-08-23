import pandas as pd
from get_api_data import get_all_stations_info

stations = pd.DataFrame.from_dict(get_all_stations_info())

print(stations[0:1])