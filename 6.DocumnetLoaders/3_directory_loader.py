from langchain_community.document_loaders import DirectoryLoader , PyPDFLoader

loader = DirectoryLoader(path="6.DocumnetLoaders/docs", glob="*.pdf" , loader_cls=PyPDFLoader) # The DirectoryLoader is used to load documents from a directory. You can specify the file path and a glob pattern to match specific file types. The loader will read the contents of all matching files in the directory and return them as a list of documents.

documents = loader.load()
print(documents[0].page_content)

    # OR
    
documents_2 = loader.lazy_load()
for doc in documents_2:
    print(doc.page_content)