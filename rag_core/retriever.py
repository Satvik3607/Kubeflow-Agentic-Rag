def retrieve(query_embedding, collection):

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    return results["documents"]