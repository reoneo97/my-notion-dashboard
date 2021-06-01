from dashboard.config import config
from dashboard.notion import NotionDatabase
import json

db = NotionDatabase(config)

data=db.query_database()
with open("data.json","w+") as f:
    json.dump(data,f)

