import pandas as pd
from ..db import get_station_naptans
from .get_api_data import get_crowding

# Requires the population of
def get_all_crowding_info():
    naptans = get_station_naptans()

    for n in naptans:
        get_crowding(n)
        continue
    
    return None
