import chromadb
from chromadb.config import Settings

client = chromadb.Client(Settings())

collection = client.create_collection("docs")

def store_embeddings(chunks, embeddings):

    for chunk, emb in zip(chunks, embeddings):

        collection.add(
            documents=[chunk.page_content],
            embeddings=[emb.tolist()],
            ids=[str(hash(chunk.page_content))]
        )