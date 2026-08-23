from .data.get_api_data import get_all_stations_info
from .data.get_crowding_data import get_crowding
from .data.get_crowding_data import get_all_crowding_info

def main() -> None:

    print(get_all_crowding_info())
    # Data pipeline: Write (to SQLite Table), Process (Aggregate days and wrangle), Read and Visualise (Plotly)
    '''
    # Something like this
    station_df = get_all_station_info()
    
    # SQLite3 database
    con = create_db()
    write_station_schema(con, station_df)

    for day in days:
        
        Make this into one dataframe? 
        crowding_df[day] = get_crowding_info_all_stations(day)

    avg_crowding_df = aggregate_crowding_data(crowding_df)

    write_crowding_schema(con, avg_crowding_df)

    visualisation_object_or_reference = plotly_visualise_data(con)

    write_visualisation_html(visualisation_object_or_reference)
    
    Done!
    '''
    print("wip tfl visualisation")
