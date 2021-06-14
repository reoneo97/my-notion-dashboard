import streamlit as st
from dashboard.config import config
from dashboard.notion import NotionDatabase
import json
import pandas as pd
import dashboard.utils.parse as parse
import dashboard.utils.visualisations as viz

import page1
import page2

db = NotionDatabase(config)

pages = {
    "Properties": page1,
    "Text":page2
}

st.sidebar.title('Navigation')
st.sidebar.write("Why isnt this showing up")
selection = st.sidebar.radio("Page: ", list(pages.keys()))

page = pages[selection]
page.app(db)