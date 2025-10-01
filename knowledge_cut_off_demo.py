from langchain_community.chat_models import ChatOpenAI
import os
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Load local env variables
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())


llm = ChatOpenAI(
    temperature=0,
    model="gpt-4.1-mini",
    max_tokens=1000,
)

# Invoke LLM and get response
response = llm.invoke("Gather reviews from the latest iphone models released in India as per today's date. Then summarise the results so that I can form a decision.")
print(response.content)