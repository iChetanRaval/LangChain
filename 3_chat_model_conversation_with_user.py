from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = GoogleGenerativeAI(model="gemini-2.0-flash") 

chat_history = []  #Use to store chat history

system_message = SystemMessage(content="You are a helpful AI assistant.")
chat_history.append(system_message)

while True:
  query = input("User: ")
  if query.lower() == "exit":
    break
  chat_history.append(HumanMessage(content=query))
  result = llm.invoke(chat_history)
  response = result
  chat_history.append(AIMessage(content=response))
  print(f"AI: {response}")

print("-----Chat history-----")
print(chat_history)