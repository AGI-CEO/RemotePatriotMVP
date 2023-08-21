from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
from my_api_tool import MyAPITool  # Import the MyAPITool class from the my_api_tool.py file

class MyToolkit(BaseToolkit):
    name: str = "My Toolkit"
    description: str = "Toolkit containing my custom tools"

    def get_tools(self) -> List[BaseTool]:
        return [MyAPITool()]

    def get_env_keys(self) -> List[str]:
        return []
