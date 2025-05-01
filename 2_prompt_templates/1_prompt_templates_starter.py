from langchain_openai import ChatOpenAI
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate

load_dotenv()

llm = GoogleGenerativeAI(model="gemini-2.0-flash")

template = "Write a {tone} email to {company} expressing my interest in the {position} position, mentoring {skills} as a key strength. Keep it to 4 lines max"

prompt_template = ChatPromptTemplate.from_template(template)

prompt = prompt_template.invoke({
    "tone": "friendly",
    "company": "Google",
    "position": "Software Engineer",
    "skills": "Python, JavaScript, and React"
})

result = llm.invoke(prompt)

print(result)
