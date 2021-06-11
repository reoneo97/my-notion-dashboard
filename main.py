from dashboard.config import config
from dashboard.notion import NotionDatabase
import json
import pandas as pd
import dashboard.utils as utils

db = NotionDatabase(config)

data=db.query_database()
df = pd.DataFrame.from_dict(data["results"])
df.to_csv("data.csv")
# with open("data.json","w+") as f:
#     json.dump(data,f)

properties = db.retrieve_properties()
parsed_properties = utils.parse_database_properties(properties)
print(parsed_properties)
# with open("properties.json","w+") as f:
#     json.dump(properties,f)

# response  = db.set_property("c330ad46-8b9b-4f1a-bf4c-2674f9649451", 
#                 "Minutes Focused",300)
# # print(curlify.to_curl(response.request))
# print(response.json())
