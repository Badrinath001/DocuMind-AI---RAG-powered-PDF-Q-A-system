# DocuMind AI - Chat with your PDF

RAG app that lets you upload any PDF and ask questions. Built with Streamlit, LangChain, Groq, and FastEmbed.

**Live Demo:** `http://localhost:8501` after `docker run`

### Features
- Upload PDF → auto splits into chunks
- Fast semantic search with BAAI/bge-small-en-v1.5
- Answers with sources using Groq `openai/gpt-oss-20b`
- Fully dockerized, embedding model baked into image for <5s indexing

### Tech Stack
Python, Streamlit, LangChain, ChromaDB, Groq, Docker, FastEmbed

### Run Locally
```bash
# .env file
GROQ_API_KEY=gsk_xxx
GROQ_MODEL=openai/gpt-oss-20b

docker build -t documind .
docker run -p 8501:8501 --env-file .env documind