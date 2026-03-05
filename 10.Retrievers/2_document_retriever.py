from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

# step1: Your source document
documents = [
Document(page_content="Langchain helps developers build LLM app eaily"),
Document(page_content="Chroma is a vector database optimize for LLM based search"),
Document(page_content="Embeddings convert texts into high-dimensional vectors"),
Document(page_content="OpenAI provides powerful embedding models"),
]

# step2: Initialize embedding model
embedding = OpenAIEmbeddings(model="text-embedding-3-small")

# step3: Create Chroma vector store in memory
vectorStore = Chroma.from_documents(
documents=documents,
embedding=embedding,
collection_name="my_collection"
)

# Step 4: Retrieve stored data
retriever = vectorStore.as_retriever(search_kwargs={"k":1})

query = "What is embeddings used for?"

results = retriever.invoke(query)

print(results)
print("\n-------------------------------\n")
for i, result in enumerate(results):
    print(f"Result {i+1}")
    print(result.page_content)




