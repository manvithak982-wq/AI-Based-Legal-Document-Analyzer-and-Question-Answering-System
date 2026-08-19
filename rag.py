# ==========================================
# rag.py
# FAISS + Gemini RAG Pipeline
# ==========================================

from ai.vector_store import load_vector_store
from ai.groq_ai import ask_groq


# ------------------------------------------
# Load FAISS database
# ------------------------------------------

vector_store = None


def get_vector_store():

    global vector_store

    if vector_store is None:
        vector_store = load_vector_store()

    return vector_store


# ------------------------------------------
# Retrieve relevant chunks
# ------------------------------------------
def retrieve_chunks(question, document_id, k=8):

    db = get_vector_store()

    # Retrieve more chunks initially
    results = db.similarity_search(
    question,
    k=50
)
    print("\n========== SEARCH RESULTS ==========")
    print("Question:", question)
    print("Document ID:", document_id)

    chunks = []

    for i, doc in enumerate(results):

        print(f"\nResult {i+1}")
        print("Metadata:", doc.metadata)
        print("Text:", doc.page_content[:250])

        if str(doc.metadata.get("document_id")) == str(document_id):

            chunks.append(doc.page_content)

            if len(chunks) >= k:
                break

    print("\nMatched Chunks:", len(chunks))

    return chunks


# ------------------------------------------
# Generate AI Answer
# ------------------------------------------

def generate_answer(question, document_id):

    chunks = retrieve_chunks(question, document_id)

    if len(chunks) == 0:
        return "No relevant information found in this document."

    context = "\n\n".join(chunks)

    print("\n========== CONTEXT SENT TO AI ==========")
    print(context[:3000])

    prompt = f"""
You are an expert Legal AI Assistant.

Use ONLY the information provided below.

If the answer exists, explain it clearly.

If the answer contains dates, amounts, obligations or parties,
include them.

Do NOT invent information.

Context:
{context}

Question:
{question}

Answer:
"""

    answer = ask_groq(prompt)

    return answer

# ------------------------------------------
# Flask Function
# ------------------------------------------

def ask_question(question, document_id):

    return generate_answer(question, document_id)