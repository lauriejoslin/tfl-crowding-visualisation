import plotly.express as px
import geopandas as gpd
from ..data.access_db import get_tfl_df

def plot_map():


    df = get_tfl_df()


    fig = px.scatter_map(df, lat="lat", lon="lon",
        hover_name="name", zoom=10, 
        animation_frame="timeBand", size="crowdingPercentage")
    fig.update_layout(
    updatemenus=[{
        "buttons": [{
            "args": [None, {"frame": {"duration": 50, "redraw": True},
                             "transition": {"duration": 50, "easing": "cubic-in-out"}}],
            "method": "animate"
        }]
    }]
)

    fig.show()
    fig.write_html("output/visualisation-widget.html")

    return

    
