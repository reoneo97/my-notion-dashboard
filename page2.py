import streamlit as st
from dashboard.config import config
from dashboard.notion import NotionDatabase
import json
import pandas as pd
import dashboard.utils.parse as parse
import dashboard.utils.visualisations as viz
from streamlit.components.v1 import html

def app(db):
    st.title("Notion Dashboard")
    @st.cache
    def load_data():
        page_id_map = db.get_page_ids()
        return page_id_map
    page_id_map = load_data()
    selected_page = st.selectbox("Select Page: ", list(page_id_map.keys()))
    page_id = page_id_map[selected_page]
    page_content = db.get_page_content(page_id)
    st.subheader("Text:")
    st.write(parse.parse_page_text(page_content))
