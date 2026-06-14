# 🧠 DocuMind AI

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13+-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/LangChain-RAG-00C853?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Groq-Llama3.3-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
</p>

</p>

<p align="center">
  <a href="https://intelipdf.streamlit.app/">
    <img src="https://img.shields.io/badge/Live%20Demo-intelipdf.streamlit.app-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  </a>
</p>

<p align="center">

<p align="center">
  <b>An AI-powered PDF Question & Answer System using RAG (Retrieval Augmented Generation)</b>
</p>

---

## 🤔 What is DocuMind AI?

**DocuMind AI** is an intelligent document assistant that lets you upload any PDF and ask questions about it in natural language. It uses **RAG (Retrieval Augmented Generation)** to retrieve relevant information from your document and generate accurate answers using **Llama 3.3** powered by **Groq**.

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 📄 **PDF Upload** | Upload any PDF document instantly |
| 🧩 **Smart Chunking** | Splits document into optimized chunks for better retrieval |
| 🤖 **LLM Powered** | Uses Llama 3.3 (70B) on Groq for ultra-fast responses |
| 💬 **Natural Q&A** | Ask questions in plain English |
| ⚡ **Real-time Answers** | Get instant answers from your documents |
| 🌐 **Web UI** | Clean Streamlit interface — no coding needed |

---

## 🏗️ How RAG Works

```
📄 Upload PDF
      │
      ▼
📝 Split into Chunks (1000 tokens each)
      │
      ▼
🔍 Retrieve Relevant Chunks
      │
      ▼
🤖 Send Context + Question to Groq LLM
      │
      ▼
💬 Get Accurate Answer!
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python 3.13** | Core language |
| **LangChain** | RAG pipeline orchestration |
| **Groq API (Llama 3.3 70B)** | Ultra-fast LLM inference |
| **Streamlit** | Web UI interface |
| **PyPDF** | PDF loading and parsing |
| **ChromaDB** | Vector database for embeddings |

---

## 📁 Project Structure

```
documind-ai/
├── app.py              # Main application
├── .env                # API keys (never push!)
├── .gitignore          # Git ignore rules
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Badrinath001/documind-ai.git
cd documind-ai
```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Groq API Key
Create a `.env` file:
```
GROQ_API_KEY=your_groq_api_key_here
```
Get your free API key at: [console.groq.com](https://console.groq.com)

### 5. Run the App
```bash
streamlit run app.py
```

---

## 🚀 How to Use

1. Open the app in your browser at `localhost:8501`
2. Upload any PDF document
3. Wait for it to process and split into chunks
4. Type your question in the input box
5. Get instant AI-powered answers! 🎉

---

## 📸 Demo

> Upload a PDF → Ask a question → Get accurate answers!

```
Question: "What is this PDF about?"

Answer: "This PDF is about the basics of Java programming,
including its history, features, and core components such as
JDK, JRE, JVM, and bytecode..."
```

---

## 🔮 Roadmap

- [x] PDF upload and processing
- [x] Smart text chunking
- [x] Groq LLM integration
- [x] Streamlit web UI
- [ ] Multiple PDF support
- [ ] Chat history memory
- [ ] Deploy on Streamlit Cloud
- [ ] Support for Word documents
- [ ] Telugu language support 🇮🇳

---

## 🙋 About the Developer

**D Badrinath** — Final Year B.Tech AIML Student | Aspiring AI Engineer

- 🐙 [GitHub](https://github.com/Badrinath001)
- 💼 [LinkedIn](https://linkedin.com/in/badrinath-d-23b652357)
- 📧 badrinathd298@gmail.com

---

## 📄 License

This project is licensed under the MIT License.

---

<p align="center">
  Built with ❤️ by <a href="https://github.com/Badrinath001">Badrinath</a>
</p>
