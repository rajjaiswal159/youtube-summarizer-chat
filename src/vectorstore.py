# Import Google embedding model
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Import FAISS
from langchain_community.vectorstores import FAISS

# Load environment variables
from dotenv import load_dotenv

# Load .env variables
load_dotenv()


# Create and save vector store
def create_vector_store(chunks):

    # Initialize embedding model
    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001"
    )

    # Create FAISS index
    vector_store = FAISS.from_texts(
        texts=chunks,
        embedding=embeddings
    )

    # Save vector store locally
    vector_store.save_local("faiss_index")

    # Return vector store
    return vector_store


# Load existing vector store
def load_vector_store():

    # Initialize embedding model
    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001"
    )

    # Load saved vector store
    vector_store = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    # Return vector store
    return vector_store