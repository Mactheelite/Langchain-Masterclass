from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-5-nano", temperature=0 )

response = model.invoke("Tell me a short story about 50 words.")

print(response.content)

