import pandas as pd
import json
from typing import List, Dict


def parse_database_pages(data: Dict):
    results = data["results"]


def parse_database_properties(data: Dict):
    properties = data["properties"]
    parsed = []
    for k, v in properties.items():
        property_ = {}
        property_["name"] = k
        property_["type"] = v["type"]
        if property_["type"] in ["select", "multi_select"]:
            property_["options"] = [i["name"]
                                    for i in v[property_["type"]]["options"]]
        parsed.append(property_)
    return parsed


def one_hot_encode():
    # Select Properties
    pass


def binary_encode():
    # Multi Select Properties
    pass
