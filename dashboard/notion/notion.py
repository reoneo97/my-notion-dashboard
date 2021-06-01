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

    def __str__(self):
        return str({a:v for a,v in self.__dict__.items()})
    
    def notion_headers(self):
        headers = {}
        headers["Authorization"] = self.token
        headers["Content-type"] = "application/json"
        headers["Notion-Version"] = "2021-05-13"
        return headers

    def query_database(self):
        endpoint = f"{self.url}/databases/{self.db}/query"
        headers = self.notion_headers()
        data = requests.post(endpoint,headers=headers)
        return data.json()

    def retrieve_properties(self):
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
        
