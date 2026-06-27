# Import Google embedding model
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Import FAISS
from langchain_community.vectorstores import FAISS

# Load environment variables
from dotenv import load_dotenv

import os

# Load .env variables
load_dotenv()


# Create and save vector store
def create_vector_store(chunks):

    try:
        # Initialize embedding model
        embeddings = GoogleGenerativeAIEmbeddings(
            model="gemini-embedding-001"
        )
    
        # Create FAISS index
        vector_store = FAISS.from_texts(
            texts=chunks,
            embedding=embeddings
        )
    
        # Return vector store
        return vector_store
    
    except Exception as e:
        raise RuntimeError(
            f"Failed to create vector store: {e}"
        ) from e
    

def save_vector_store(vector_store, video_id):
    path = os.path.join("vector_store", video_id)
    vector_store.save_local(path)


def load_vector_store(video_id):

    path = os.path.join("vector_store", video_id)

    if not os.path.exists(path):
        return None

    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001"
    )

    return FAISS.load_local(
        path,
        embeddings,
        allow_dangerous_deserialization=True
    )