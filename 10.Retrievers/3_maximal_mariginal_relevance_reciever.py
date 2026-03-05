from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

# step1: Your source document
documents = [
Document(page_content="Langchain makes it easier to work with LLM"),
Document(page_content="Langchain helps developers build LLM applications eaily"),
Document(page_content="Chroma is a vector database optimize for LLM based search."),
Document(page_content="Embeddings convert texts into high-dimensional vectors."),
Document(page_content="MMR helps you get diverse results when doing similarity search."),
Document(page_content="OpenAI provides powerful embedding models"),
]

# step2: Initialize embedding model
embedding = OpenAIEmbeddings(model="text-embedding-3-small")

# step3: Create Chroma vector store in memory
vectorStore = FAISS.from_documents(
documents=documents,
embedding=embedding,
)

# Step 4: Retrieve stored data
retriever = vectorStore.as_retriever(
    search_type="mmr", 
    search_kwargs={"k": 1, "lambda_mult": 0.25}
                )

query = "What is Langchain?"

results = retriever.invoke(query)

print(results)
print("\n-------------------------------\n")
for i, result in enumerate(results):
    print(f"Result {i+1}")
    print(result.page_content)




