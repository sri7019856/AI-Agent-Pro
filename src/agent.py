from langchain.agents import create_agent
from src.memory.checkpoint import checkpointer
from src.tools.weather_tool import get_weather
from src.tools.web_search_tool import web_search
from src.prompts.system_prompt import SYSTEM_PROMPT
from src.tools.maps_tool import get_route

from src.llm import llm

from src.tools.math_tools import (
    multiply, 
    add, 
    subtract, 
    divide
)

from src.tools.file_tools import (
    read_file,
    find_file
)

from src.tools.system_tools import current_time

def create_chat_agent(checkpointer):

    print("Creating LangGraph Agent...")

    agent = create_agent(
        model=llm,
        tools=[multiply, 
            add, 
            subtract,
            divide, 
            current_time,
            read_file, 
            find_file,
            get_weather,
            web_search,
            get_route
            ],
            system_prompt=SYSTEM_PROMPT,
        checkpointer=checkpointer
    )
    print("Agent Created Successfully")

    return agent
