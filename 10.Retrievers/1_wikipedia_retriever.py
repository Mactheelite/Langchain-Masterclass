from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(top_k_results=2,lang="en")

query = "Artificial Intelligence"

documents = retriever.invoke(query)

print(len(documents))

for i , doc in enumerate(documents):
    print(f"Document {i+1}\n")
    print(f"Content: {doc.page_content}")


# Make sure you install wikipedia using
# pip install wikipedia or uv add wikipedia