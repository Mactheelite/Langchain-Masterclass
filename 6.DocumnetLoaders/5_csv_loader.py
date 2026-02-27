from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="6.DocumnetLoaders/sales_data.csv",encoding="utf-8")

documents = loader.load()

print(documents[0]) # this will print the first row of the csv file as a document. Each document contains the text content of the row.

