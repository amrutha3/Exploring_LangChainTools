from datetime import date
import langchain
from langchain.agents import tool
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain_community.chat_models import ChatOpenAI
import os

from langchain_community.tools import DuckDuckGoSearchRun


from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

@tool
def search_from_web(query: str) -> str:
    """This functions uses DuckDuckGo Search Engine API to return search results from the web.
    The input should be an input string that can be a question or a topic
    that we would want to search on the web."""
    search = DuckDuckGoSearchRun()
    return search.invoke(query)


@tool
def time(text: str) -> str:
    """Returns todays date, use this for any question related to knowing todays date."""
    return str(date.today())

llm = ChatOpenAI(temperature=0, model="gpt-4.1-mini")

agent= initialize_agent(
    [search_from_web, time], 
    llm, 
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True,
    verbose = True)


# langchain.debug = True
result = agent("Gather reviews from the latest iphone models released in India as per today's date. Then summarise the results so that I can form a decision.") 

print(result)

print("\nFinal Answer:\n")
print(result["output"])