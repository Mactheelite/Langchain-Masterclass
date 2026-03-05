from dotenv import load_dotenv

load_dotenv() 

# 1. Load your Pdf document
from langchain.chat_models import init_chat_model
from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader("11.RAG/docs/tesla.pdf")
documents = loader.load()

# 2. Split the document into smaller chunks
from langchain_text_splitters import RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300, 
    chunk_overlap=50,
    separators=""
)
split_docs = splitter.split_documents(documents)

# 3. Create embeddings for the document chunks
from langchain_openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")


# 4. Store the embeddings in a vector database
from langchain_chroma import Chroma 
vectorStore = Chroma.from_documents(
    documents=split_docs,
    embedding=embeddings,
    collection_name="tesla_docs"
) 

# 5. Retrieve relevant document chunks based on a query
retriever = vectorStore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 2, "lambda_mult": 0.5}
)

# 6. Initialize your LLM
from langchain.chat_models import init_chat_model
model = init_chat_model(
    model=  "llama-3.3-70b-versatile",
    model_provider="groq",
    temperature=0.7
)

# 7. Create a prompt template
from langchain_core.prompts import ChatPromptTemplate
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant. Use the following context to answer the question. If the answer is not present,"),
        ("human", "{context}\n\nQuestion: {question}")
    ]
)

# 8. Create an output parser
from langchain_core.output_parsers import StrOutputParser
parser = StrOutputParser()

# 9. Create a RAG chain
def format_docs(docs):
    return "\n\n".join([doc.page_content for doc in docs])


rag_chain = (
    {
    "context": retriever | format_docs,
    "question": lambda x: x
} | prompt_template | model | parser

)

# 10 Ask a question
query = "What is this document mainly about?"

response = rag_chain.invoke(query)


print(response)