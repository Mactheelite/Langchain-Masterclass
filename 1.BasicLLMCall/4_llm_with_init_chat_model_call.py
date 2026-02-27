from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

# groq =   "llama-3.3-70b-versatile" ,    model_provider="groq"
# openai = "gpt-4.1-mini" , model_provider="openai"
# google = "gemini-2.5-flash" , model_provider="google"

model = init_chat_model(
    model=  "llama-3.3-70b-versatile",
    model_provider="groq",
    temperature=0.7
)


response = model.invoke("Tell me a short story about 50 words.")

print(response.content)