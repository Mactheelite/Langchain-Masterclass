from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)

template_1 = PromptTemplate.from_template("Write a detailed report on {topic}")
template_2 = PromptTemplate.from_template("Write a 4 line summary on the following {text}")

parser = StrOutputParser()

# The output of the first model will be a detailed report on the given topic, which will then be passed to the second model to generate a concise summary. The StrOutputParser is used to ensure that the output from the first model is in string format before being passed to the second model.
chain = template_1 | model | parser | template_2 | model | parser

response = chain.invoke({"topic":"Bermuda triangle"})

print(response)

