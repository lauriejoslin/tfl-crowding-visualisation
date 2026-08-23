import pandas as pd
from ..db import get_station_naptans
from .get_api_data import get_crowding

# Requires the population of
def get_all_crowding_info():
    naptans = get_station_naptans()

    crowding_info_stations = [{"naptan": n, "crowd_df": get_crowding(n)} for n in naptans]
    crowding_stations_df = pd.DataFrame.from_dict(crowding_info_stations)
    
    return crowding_info_stations
