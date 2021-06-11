import pandas as pd
import json
from typing import List, Dict, Tuple
from pydantic import BaseModel
from datetime import datetime
def parse_database_pages(data: Dict):
    results = data["results"]


def parse_database_properties(data: Dict) -> Dict: 

    properties = data["properties"]
    parsed = {}
    for k, v in properties.items():
        property_ = {}
        property_["type"] = v["type"]
        if property_["type"] in ["select", "multi_select"]:
            property_["options"] = [i["name"]
                                    for i in v[property_["type"]]["options"]]
        parsed[k] = property_
    return parsed

def get_select_properties(parsed):
    """
    Get the database properties which are of the "select" type
    """
    return [k for k,v in parsed.items() if v["type"] == "select"]

def parse_database_for_property(results: List,prop_name: str,
    prop_type:str) -> Tuple[List,List]: 

    timestamps = []
    property_values = []
    for page in results:
        timestamps.append(page["last_edited_time"])
        property_values.append(page["properties"][prop_name][prop_type]["name"])
    timestamps = [datetime.strptime(ts,"%Y-%m-%dT%H:%M:%S.%f%z") for ts in timestamps]
    return timestamps,property_values

def one_hot_encode():
    # Select Properties
    pass


def binary_encode():
    # Multi Select Properties
    pass

def parse_date():
    pass

class Property(BaseModel):
    name: str
    prop_type: str
    options: List[str]
    