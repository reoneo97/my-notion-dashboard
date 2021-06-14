from dashboard.config import config
from dashboard.notion import NotionDatabase
import json
import pandas as pd
import dashboard.utils.parse as parse
import IPython


db = NotionDatabase(config)

print(db.get_page_ids())
properties = db.get_properties()
parsed_properties = parse.parse_database_properties(properties)
print(parsed_properties)
# with open("properties.json","w+") as f:
#     json.dump(properties,f)

# response  = db.set_property("c330ad46-8b9b-4f1a-bf4c-2674f9649451", 
#                 "Minutes Focused",300)
# # print(curlify.to_curl(response.request))
# print(response.json())
