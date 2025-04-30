from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = GoogleGenerativeAI(model="gemini-2.0-flash") 

messages = [
    SystemMessage(content="You are an expert in social media content strategy."),
    HumanMessage(content="What are some tips for creating engaging content on Instagram?"),
]

result = llm.invoke(messages)
print(result) 

