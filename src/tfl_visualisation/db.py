import sqlite3
import pandas as pd
from .data.get_api_data import get_all_stations_info

def write_stations() -> None:
    con = sqlite3.connect("tfl.db")
    cur = con.cursor()

    stations_df = get_all_stations_info()
    stations_df.to_sql("stations", con=con, index=False)

    cur.close()

def read_stations() -> None:
    con = sqlite3.connect("tfl.db")
    cur = con.cursor()

    res = cur.execute("SELECT * FROM stations")
    rows = res.fetchall()

    stations = pd.DataFrame.from_dict(rows)
    print(stations)

    cur.close()

def get_station_naptans() -> list:
    con = sqlite3.connect("tfl.db")
    cur = con.cursor()

    res = cur.execute("SELECT naptan FROM stations")
    rows = res.fetchall()
    naptans = [row[0] for row in rows]

    return naptans

def delete_stations() -> None:
    con = sqlite3.connect("tfl.db")
    cur = con.cursor()

    cur.execute("DROP TABLE stations")

    cur.close()