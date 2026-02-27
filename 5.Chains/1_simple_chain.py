from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)

prompt = PromptTemplate.from_template("Generate 3 facts about {topic}")

parser = StrOutputParser()

chain = prompt | model | parser

response = chain.invoke({"topic":"Computers"})

print(response)

