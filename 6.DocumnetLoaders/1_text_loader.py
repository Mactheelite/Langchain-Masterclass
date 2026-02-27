from langchain_community.document_loaders import TextLoader

loader = TextLoader(file_path="6.DocumnetLoaders/tesla.txt" , encoding="utf-8") # The TextLoader is used to load text files. You can specify the file path and encoding. The loader will read the contents of the file and return it as a string.

documents = loader.load()

print(documents[0].page_content)

