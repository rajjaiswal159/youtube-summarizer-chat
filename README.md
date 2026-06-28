# 🎥 YouTube Video Chat Assistant (Chrome Extension)

Chat with any YouTube video's transcript using Retrieval-Augmented Generation (RAG).

This project is a Chrome Extension powered by **LangChain**, **FAISS**, **Google Gemini Embeddings**, and **FastAPI**. It extracts the transcript of the currently opened YouTube video, converts it into embeddings, stores them in a vector database, and answers user questions based only on the video's content.

---

## 🚀 Features

- 📺 Chat with any YouTube video transcript
- 🧠 Retrieval-Augmented Generation (RAG)
- ⚡ FastAPI backend
- 🔍 Semantic search using FAISS
- 🤖 Google Gemini Embeddings
- 🧩 Chrome Side Panel Extension
- 💬 Clean HTML/CSS/JavaScript UI
- 📄 Automatic transcript extraction

---

## 🏗️ Project Architecture

```
YouTube Video
      │
      ▼
Fetch Transcript
      │
      ▼
Text Splitter
      │
      ▼
Gemini Embeddings
      │
      ▼
FAISS Vector Store
      │
      ▼
Retriever
      │
      ▼
Gemini LLM
      │
      ▼
Answer in Chrome Side Panel
```

---


## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- LangChain
- FAISS
- Google Gemini API
- YouTube Transcript API

### Frontend
- HTML
- CSS
- JavaScript
- Chrome Extension API

---

# 📁 Project Structure

```text
youtube-video-chat/
│
├── backend/
│   ├── api.py                     # FastAPI server
│   │
│   ├── src/
│   │   ├── transcript.py          # Fetch YouTube transcript
│   │   ├── text_splitter.py       # Split transcript into chunks
│   │   ├── vectorstore.py         # Create FAISS vector database
│   │   ├── chatbot.py             # LangChain RAG pipeline
│   │   ├── cache_manager.py       # Cache processed videos
│   │   └── chat_session.py        # Maintain chat history
│   │
│   └── vector_store_gm/           # Saved FAISS index
│
├── extension/
│   ├── manifest.json              # Chrome extension configuration
│   ├── background.js              # Background service worker
│   ├── sidepanel.html             # Extension UI
│   ├── sidepanel.css              # Styling
│   └── sidepanel.js               # Frontend logic
│
├── images/
│   ├── home.png                   # Home page screenshot
│   └── chat.png                   # Chat page screenshot
│
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
└── .gitignore                     # Files ignored by Git
```

---

# ⚙️ How It Works

1. User opens a YouTube video.
2. Chrome Extension extracts the video ID.
3. Backend fetches the transcript.
4. Transcript is split into smaller chunks.
5. Chunks are converted into embeddings.
6. Embeddings are stored in a FAISS vector database.
7. User asks a question.
8. Relevant transcript chunks are retrieved.
9. Gemini generates an answer using the retrieved context.

---

## 🖼️ Screenshots

### Home

![Home](images/home.png)

### Chat

![Chat](images/chat.png)

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone https://github.com/rajjaiswal159/youtube-chat-assistant.git

cd youtube-chat-assistant
```

---

## 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Create a .env file

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

## 5. Start FastAPI

```bash
cd backend

uvicorn api:app --reload
```

Server runs at

```
http://127.0.0.1:8000
```

---

## 6. Load Chrome Extension

- Open Chrome
- Go to `chrome://extensions`
- Enable **Developer Mode**
- Click **Load unpacked**
- Select the `extension` folder

---

## 💡 Example Questions

- What is this video about?
- Summarize the key points.
- Explain the main concept.
- What examples were discussed?
- What are the important takeaways?

---

# 📚 Concepts Used

- Retrieval-Augmented Generation (RAG)
- Embeddings
- Vector Databases
- Semantic Search
- Chunking
- Prompt Engineering
- FastAPI
- LangChain
- Chrome Extensions

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

---

# 📄 License

This project is licensed under the MIT License.