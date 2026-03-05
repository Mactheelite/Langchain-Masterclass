from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

text = [
    "Cricket is one of the most popular sports played and watched by millions around the world.",
    "The Cricket game is played between two teams with eleven players on each side.",
    "Cricket requires skill, patience, teamwork, and strategic thinking to win matches consistently.",
    "International Cricket tournaments attract massive audiences and showcase extraordinary talent from different countries.",
    "Many young athletes dream of becoming professional players in the competitive world of Cricket.",
    "Test Cricket is known for its long format and intense five-day matches.",
    "T20 Cricket offers fast-paced action and thrilling finishes for fans.",

]


embedding = OpenAIEmbeddings(model="text-embedding-3-small")

vectorstore = FAISS.from_texts(texts=text, embedding=embedding) # The from_texts method is a convenient way to create a FAISS vector store from a list of texts. You need to provide the texts and the embedding model.

query = "What is Cricket?"

results = vectorstore.similarity_search(query=query, k=2) 

# print(result)   uncomment this to see the full raw result

for i , result in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(f"Content: {result.page_content}")


# Make sure you intall faiss-cpu using 
# pin install faiss-cpu or uv add faiss-cpu