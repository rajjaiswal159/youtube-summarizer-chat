from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.text_splitter import split_text
from src.chatbot import create_rag_chain
from src.cache_manager import cleanup_vector_store
from src.transcript import get_transcript, extract_video_id
from src.chat_session import (
    clear_history,
    get_history,
    add_user_message,
    add_ai_message,
)
from src.vectorstore import (
    create_vector_store,
    save_vector_store,
    load_vector_store
)

# Create FastAPI application
app = FastAPI(
    title="YouTube Chat API",
    version="1.0.0"
)

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store the currently loaded RAG components
vector_store = None
rag_chain = None
current_video_id = None


# Health check endpoint
@app.get("/")
def home():
    return {"status": "Backend Running"}


# Process a YouTube video
@app.post("/process")
async def process_video(data: dict):

    global vector_store
    global rag_chain
    global current_video_id

    try:

        # Get video URL from the request
        video_url = data["video_url"]

        # Extract the YouTube video ID
        video_id = extract_video_id(video_url)

        # Skip processing if the same video is already loaded
        if current_video_id == video_id:
            return {
                "success": True,
                "message": "Video is already processed."
            }
        
        # Load an existing vector store if available
        vector_store = load_vector_store(video_id)

        # Create a new vector store if one doesn't exist
        if vector_store is None:
            transcript = get_transcript(video_id)
        
            chunks = split_text(transcript)
        
            vector_store = create_vector_store(chunks)
        
            save_vector_store(vector_store, video_id)
            cleanup_vector_store()

        # Initialize the RAG chain
        rag_chain = create_rag_chain(vector_store)

        # Clear previous chat history
        clear_history()

        # Save the current video ID
        current_video_id = video_id

        return {
            "success": True,
            "message": "Video processed successfully!"
        }

    # Handle processing errors
    except Exception as e:

        return {
            "success": False,
            "message": str(e)
        }


# Answer user questions
@app.post("/chat")
async def chat(data: dict):

    global rag_chain

    try:

        # Ensure a video has been processed
        if rag_chain is None:
            return {
                "success": False,
                "message": "Please process a video first."
            }

        # Get the user's question
        question = data["question"]

        # Generate an answer using the RAG chain
        answer = rag_chain.invoke(
            {
                "question": question,
                "chat_history": get_history()
            }
        )

        # Save the conversation history
        add_user_message(question)
        add_ai_message(answer)

        return {
            "success": True,
            "answer": answer
        }

    # Handle chat errors
    except Exception as e:
        error = str(e)

        # Handle API quota limit errors
        if "429" in error or "quota" in error.lower():
            return {
                "success": False,
                "message": "The AI service has reached its usage limit. Please try again later."
            }

        return {
            "success": False,
            "message": str(e)
        }
