from langchain_core.prompts import PromptTemplate    


dynamic_prompt = PromptTemplate.from_template("Write a short paragraph about {topic} in a {style} style.")

prompt_text = dynamic_prompt.format(topic="AI", style="informative") # We can change the topic and style dynamically when formatting the prompt.

print(prompt_text)