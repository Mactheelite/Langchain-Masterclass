from langchain_core.prompts import PromptTemplate    


static_prompt = PromptTemplate.from_template("Write a short fun fact about AI.")

prompt_text = static_prompt.format()

print(prompt_text)