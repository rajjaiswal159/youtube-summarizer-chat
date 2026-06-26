# Import Streamlit
import streamlit as st

# Import project modules
from src.transcript import get_transcript
from src.text_splitter import split_text
from src.vectorstore import create_vector_store
from src.chatbot import create_rag_chain


# Page title
st.title("🎥 YouTube Video Summarizer & Chat")

# Input YouTube URL
video_url = st.text_input(
    "Enter YouTube Video URL"
)

# Process button
if st.button("Process Video"):
    try:
        with st.spinner("Processing Video..."):
            transcript = get_transcript(video_url)
            chunks = split_text(transcript)
            st.session_state.vector_store = create_vector_store(chunks)
            st.session_state.rag_chain = create_rag_chain(
                st.session_state.vector_store
            )

        st.success("Video Processed Successfully!")

    except Exception as e:
        st.error(str(e))

# Question input
question = st.text_input(
    "Ask a Question About the Video"
)

# Ask button
if st.button("Ask"):

    if "vector_store" not in st.session_state:
        st.error("Process a video first!")

    elif not question.strip():
        st.warning("Please enter a question.")

    else:
        try:
            answer = st.session_state.rag_chain.invoke(question)
            st.info(answer)
        
        except Exception as e:
            st.error(str(e))