import sqlite3
import pandas as pd
from .data.get_api_data import get_all_stations_info
from .data.get_api_data import get_crowding

def write_stations() -> None:
    con = sqlite3.connect("tfl.db")
    cur = con.cursor()

    stations_df = get_all_stations_info()
    stations_df.to_sql("stations", con=con, index=False)

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

    cur.close()

def write_naptan_crowding() -> None:
    con = sqlite3.connect("tfl.db")
    cur = con.cursor()

    cur.execute("CREATE TABLE crowding(naptan, crowding_df)")
    naptans = get_station_naptans()
    naptans = naptans[:50]

    for n in naptans:
        crowd_df = get_crowding(n)

        query = """
            INSERT INTO crowding VALUES
                ('{naptan}', {crowd_df})
        """.format(naptan=n, crowd_df=crowd_df)

        cur.execute(query)

    cur.close()

def delete_crowding_table() -> None:
    con = sqlite3.connect("tfl.db")
    cur = con.cursor()

    cur.execute("DROP TABLE crowding")

    cur.close()