import plotly.express as px
import geopandas as gpd
import os

def plot_map():
    geo_df = gpd.read_file("geojson/london_boroughs.geojson")

    print(geo_df)

    """
    fig = px.scatter_map(geo_df,
                            hover_name="name",
                            zoom=1)
    fig.show()
    """

    return