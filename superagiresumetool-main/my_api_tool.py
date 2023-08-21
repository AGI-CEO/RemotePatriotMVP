from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type
import requests

class MyAPITool(BaseTool):
    name: str = "My API Tool"
    args_schema: Type[BaseModel] = BaseModel  # No input parameters needed
    description: str = "Tool to make a GET request and receive a resume"

    def _execute(self):
        endpoint = "https://api.directual.com/good/api/v5/webHook/sendoutresume?appID=9e9c8d9f-fefd-42ad-8225-db9b4d0c871a"
        response = requests.get(endpoint)
        return response.json() if response.status_code == 200 else {"error": "Request failed"}
