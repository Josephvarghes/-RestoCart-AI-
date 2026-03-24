import chromadb
from chromadb.utils import embedding_functions

CHROMA_PATH = "chroma_db"
COLLECTION_NAME = "products"


def get_chroma_client():
    return chromadb.PersistentClient(path=CHROMA_PATH)


def get_or_create_collection():
    client = get_chroma_client()
    embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=embedding_func,
        metadata={"hnsw:space": "cosine"},
    )
    return collection


def semantic_search(query: str, top_k: int = 3) -> list[dict]:
    collection = get_or_create_collection()
    results = collection.query(query_texts=[query], n_results=top_k)

    docs = []
    for i, _ in enumerate(results["documents"][0]):
        # Reconstruct product-like object from metadata
        meta = results["metadatas"][0][i]
        docs.append(
            {
                "name": meta["name"],
                "description": meta["description"],
                "price": meta["price"],
            }
        )
    return docs
