import requests
import yaml
from ..config import NotionConfig

class NotionDatabase(object):
    """
    Object to perform queries on the database
    """
    def __init__(self,config: NotionConfig):
        self.url = config.notion_url
        self.db = config.db_id
        self.token = config.integration_token
        self.Notion_Version = config.Notion_Version

    def __str__(self):
        return str({a:v for a,v in self.__dict__.items()})
    
    def notion_headers(self):
        headers = {}
        headers["Authorization"] = self.token
        headers["Content-type"] = "application/json"
        headers["Notion-Version"] = self.Notion_Version
        return headers

    def get_database(self):
        endpoint = f"{self.url}/databases/{self.db}/query"
        headers = self.notion_headers()
        data = requests.post(endpoint,headers=headers)
        return data.json()

    def get_properties(self):
        """Obtain database properties to set up the app

        Returns:
            json: JSON of Database properties
        """
        endpoint = f"{self.url}/databases/{self.db}"
        headers = self.notion_headers()
        data = requests.get(endpoint,headers=headers)
        return data.json()

    def set_property(self,page_id,property_,value):
        endpoint = f"{self.url}/pages/{page_id}"
        headers = self.notion_headers()
        query = {
            "properties":{
                property_: { "number" : value}
            }

        }   
        response = requests.patch(endpoint,json=query,headers=headers)
        return response
        
    def query_property(self,prop_name,prop_type):
        query = {
            "filter":{
                "property": prop_name,
                prop_type:{
                    "is_not_empty":True
                }
            }
        }
        endpoint = f"{self.url}/databases/{self.db}/query"
        headers = self.notion_headers()
        response = requests.post(endpoint,headers=headers,json=query)
        return response.json()
    #Database Queries only provide properties,  
    def get_page_content(self,page_id):
        endpoint = f"{self.url}/blocks/{page_id}/children"
        headers = self.notion_headers()
        data = requests.get(endpoint,headers=headers)
        return data.json()
    
    def get_page_ids(self):
        data = self.get_database()
        id_map = {i["properties"]["Name"]["title"][0]["plain_text"] \
            :i["id"] for i in data["results"]}
        return id_map