from src.vectorstore import load_vector_store

# Load saved FAISS index
vector_store = load_vector_store()

# Search similar chunks
results = vector_store.similarity_search(
    "What is a neural network?",
    k=3
)

# Print results
for i, doc in enumerate(results, start=1):
    print(f"\nResult {i}\n")
    print(doc.page_content[:500])