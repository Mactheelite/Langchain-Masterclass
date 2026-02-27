from langchain_core.prompts import ChatPromptTemplate , SystemMessagePromptTemplate, HumanMessagePromptTemplate

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that provides information about {topic}."),
    ("human", "Can you tell me something interesting about {topic}?"),
])

# OR

chat_prompt_2 = ChatPromptTemplate.from_messages([
  SystemMessagePromptTemplate.from_template("You are a helpful assistant that provides information about {topic}."),
  HumanMessagePromptTemplate.from_template("Can you tell me something interesting about {topic}?")
])  


prompt_text = chat_prompt.format_messages(topic="AI")
prompt_text_2 = chat_prompt_2.format_messages(topic="Langchain")

print(prompt_text)
print("\n----------------------------------------------------------------------------------\n")
print(prompt_text_2)