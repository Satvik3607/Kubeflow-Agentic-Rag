import os
from langchain_community.document_loaders import TextLoader

def load_documents(data_folder):

    documents = []

    for file in os.listdir(data_folder):

        if file.endswith(".txt"):

            path = os.path.join(data_folder, file)

            loader = TextLoader(path)

            docs = loader.load()

            documents.extend(docs)

    return documents