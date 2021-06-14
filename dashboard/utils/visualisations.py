import plotly.express as px
from .parse import parse_database_for_property
from dashboard.notion import NotionDatabase
import pandas as pd
from typing import List

def time_scatter_select_plot(prop_name:str, prop_opts: List[str],
    db: NotionDatabase):
    
    results = db.query_property(prop_name,"select")["results"]
    x, values = parse_database_for_property(results,prop_name,"select")
    prop_map = {name:i for i,name in enumerate(prop_opts)}
    #values = [prop_map[name] for name in values]
    df = pd.DataFrame({"timestamp":x,prop_name:values})
    fig = px.scatter(df,x="timestamp",y=prop_name,color=prop_name,
        category_orders={prop_name:prop_opts})
    return fig

def bar_select_plot():
    pass