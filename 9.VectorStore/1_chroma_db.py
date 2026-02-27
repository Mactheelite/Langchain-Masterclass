from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

texts = [
    "Large language models are trained on a diverse range of internet text.",
    "Chroma is an open-source embedding database that allows you to store and query vector embeddings efficiently. It provides a simple interface for adding, retrieving, and managing vector data, making it ideal for applications like semantic search, recommendation systems, and natural language processing tasks.",
    "OpenAI's embedding models, such as the text-embedding-3-small model, are designed to convert text into high-dimensional vector representations. These embeddings capture the semantic meaning of the text, allowing for tasks like similarity search, clustering, and classification. By using OpenAI's embeddings with Chroma, you can create a powerful vector store that enables efficient retrieval of relevant information based on the semantic content of the text."
]