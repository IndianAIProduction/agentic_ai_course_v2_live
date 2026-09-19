import os
from dotenv import load_dotenv
from rich import print
from langchain.chat_models import init_chat_model
from langchain_groq import ChatGroq

load_dotenv()

MODEL_NAME = "qwen/qwen3.8-27b" #"gpt-5.6-luna"

MODEL_PROVIDER = "gorq" # "openai"
# llm = init_chat_model(model=MODEL_NAME, model_provider=MODEL_PROVIDER)

llm = ChatGroq(model=MODEL_NAME)

response = llm.invoke("Hi there, how are you?")
print(response)
print(response.content)

# user: 
# AI: 

## openai responce: Hi! I’m doing well, thanks for asking. How are you?