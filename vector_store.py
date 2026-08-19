from langchain_community.vectorstores import FAISS
from ai.embeddings import embedding_model
import os

VECTOR_DB_PATH = "vector_db"


def build_vector_store(chunks):

    texts = [chunk["text"] for chunk in chunks]

    metadatas = [
        {
            "document_id": chunk["document_id"],
            "page": chunk["page"]
        }
        for chunk in chunks
    ]

    print("\n========== BUILD VECTOR STORE ==========")
    print("Texts:", len(texts))

    vector_store = FAISS.from_texts(
        texts=texts,
        embedding=embedding_model,
        metadatas=metadatas
    )

    vector_store.save_local(VECTOR_DB_PATH)

    print("Vector Store Saved Successfully")


def load_vector_store():

    if not os.path.exists(VECTOR_DB_PATH):
        raise Exception("Vector database not found. Upload a document first.")

    return FAISS.load_local(
        VECTOR_DB_PATH,
        embedding_model,
        allow_dangerous_deserialization=True
    )