import streamlit as st
from dashboard.config import config
from dashboard.notion import NotionDatabase
import json
import pandas as pd
import dashboard.utils.parse as parse
import dashboard.utils.visualisations as viz


def app(db):
    st.title("Notion Dashboard")

    st.subheader("Setup Instructions:")
    @st.cache
    def load_props():
        properties = db.get_properties()
        parsed_props = parse.parse_database_properties(properties)
        select_prop_names = parse.get_select_properties(parsed_props)
        return properties,parsed_props,select_prop_names
    
    properties,parsed_props,select_prop_names = load_props()

    token = st.text_input("Authentication Token here", "")
    st.markdown(
        (
        "> Your database id can be found from the url provided by notion. "
        "Eg. https://www.notion.so/22f558a3eca64d5a9e16b958d449212f"
        "?v=153b996b9b5d4296818d42320dfac952 \n \n"
        "The database id is **22f558a3eca64d5a9e16b958d449212f** which is 32 chars" 
        )
    )
    st.write(parsed_props)
    st.write(select_prop_names)
    db_id = st.text_input("Database id: ")

    st.header("Dasboard")
    prop_name = st.selectbox("Property:",select_prop_names)
    prop_opts = parsed_props[prop_name]['options']
    #st.write(db.query_property(prop_,"select"))

    fig = viz.time_scatter_select_plot(prop_name,prop_opts,db)
    st.write(fig)
