# 🎥 YouTube Video Chat Assistant (Chrome Extension + LangChain RAG)

Chat with any YouTube video directly from a Chrome Side Panel using Retrieval-Augmented Generation (RAG).

This project extracts a video's transcript, creates vector embeddings using Google's Gemini Embedding model, stores them in FAISS, and allows users to ask natural language questions about the video without leaving YouTube.

---

## 🚀 Features

- 📺 Process any YouTube video with transcripts
- 💬 Ask questions about the video in natural language
- 🧠 Retrieval-Augmented Generation (RAG)
- ⚡ Chrome Side Panel Extension
- 🔍 LangChain-powered retrieval pipeline
- 📚 FAISS Vector Store
- 🤖 Google Gemini Embeddings
- 💾 Automatic vector store caching (avoids recreating embeddings for previously processed videos)
- 🎯 FastAPI backend
- 🎨 Custom HTML/CSS/JavaScript frontend

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

## 📂 Project Structure

```
youtube-summarizer-chat/
│
├── backend/
│   ├── api.py                    # FastAPI backend and API endpoints
│   ├── src/
│   │   ├── chatbot.py            # Builds the LangChain RAG pipeline
│   │   ├── cache_manager.py      # Manages cached FAISS vector stores
│   │   ├── text_splitter.py      # Splits transcript into chunks
│   │   ├── transcript.py         # Fetches YouTube transcripts
│   │   └── vectorstore.py        # Creates, saves, and loads FAISS vector stores
│   └── vector_store/             # Cached vector stores for processed videos
│
├── extension/
│   ├── manifest.json             # Chrome extension configuration
│   ├── background.js             # Handles extension background events
│   ├── sidepanel.html            # Side panel UI
│   ├── sidepanel.css             # Side panel styling
│   └── sidepanel.js              # Frontend logic and API communication
│
├── images/
│   ├── home.png                  # Home screen screenshot
│   └── chat.png                  # Chat interface screenshot
│
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
└── .gitignore                    # Files ignored by Git
```

---

## 🛠️ Tech Stack

### Backend

- Python
- FastAPI
- LangChain
- Google Gemini API
- FAISS

### Frontend

- HTML
- CSS
- JavaScript
- Chrome Extension API

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/rajjaiswal159/youtube-chat-assistant.git

cd youtube-chat-assistant
```

---

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create a `.env` file in the project root.

```
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

### 5. Start the backend

```bash
cd backend

uvicorn api:app --reload
```

Backend runs on

```
http://127.0.0.1:8000
```

---

### 6. Load the Chrome Extension

1. Open Chrome
2. Go to:

```
chrome://extensions
```

3. Enable **Developer Mode**
4. Click **Load unpacked**
5. Select the `extension` folder

---

## 📸 Screenshots

### Home

![Home](images/home.png)

### Chat

![Chat](images/chat.png)

---

## 💡 How It Works

1. User opens a YouTube video.
2. Clicks **Process**.
3. Transcript is extracted.
4. Transcript is split into chunks.
5. Chunks are converted into embeddings.
6. Embeddings are stored in FAISS.
7. User asks questions.
8. LangChain retrieves relevant chunks.
9. Gemini generates the final answer.

---

## ⚡ Vector Store Caching

To improve performance, processed videos are cached locally.

- Each YouTube video is identified by its unique Video ID.
- Embeddings are generated only once.
- Previously processed videos reuse the existing FAISS index.
- Processing the same video again is almost instantaneous.

---

## 🤝 Contributing

Contributions are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Raj Jaiswal**

GitHub: https://github.com/rajjaiswal159
