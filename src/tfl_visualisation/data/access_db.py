import sqlite3
import pandas as pd
from .get_api_data import get_all_stations_info
from .get_api_data import get_crowding

def write_stations() -> None:
    con = sqlite3.connect("tfl.db")
    cur = con.cursor()

    stations_df = get_all_stations_info()
    stations_df.to_sql("stations", con, index=False)

    con.commit()
    cur.close()

def read_stations() -> None:
    con = sqlite3.connect("tfl.db")
    cur = con.cursor()

    query = "SELECT * FROM stations"

    stations = pd.read_sql(query, con)
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
    con.commit()

    cur.close()

def write_naptan_crowding() -> None:
    con = sqlite3.connect("tfl.db")
    cur = con.cursor()

    naptans = get_station_naptans()

    dfs = []
    for n in naptans:
        not_found, crowd_df = get_crowding(n)
        # Avoid write errors
        if not_found:
            continue

        print(f"Successfully obtained crowding data for NaPTaN: {n}")
        crowd_df["naptan"] = n
        dfs.append(crowd_df)

    stations_crowding_df = pd.concat(dfs, ignore_index=True)
    stations_crowding_df.to_sql("crowding", con, index=False)

    con.commit()
    cur.close()

def delete_crowding_table() -> None:
    con = sqlite3.connect("tfl.db")
    cur = con.cursor()

    cur.execute("DROP TABLE crowding")
    con.commit()

    cur.close()

def read_crowding() -> None:
    con = sqlite3.connect("tfl.db")
    cur = con.cursor()

    query = "SELECT * FROM crowding"
    
    crowding = pd.read_sql(query, con)
    print(crowding)

    cur.close()

def get_tfl_df() -> pd.DataFrame:
    con = sqlite3.connect("tfl.db")
    cur = con.cursor()

    stations = pd.read_sql("SELECT * FROM stations", con)
    crowding = pd.read_sql("SELECT * FROM crowding", con)

    tfl_df = pd.merge(stations, crowding, on="naptan")

    cur.close()

    return tfl_df