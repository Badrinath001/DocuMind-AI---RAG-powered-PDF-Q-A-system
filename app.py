import os
import streamlit as st
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_community.embeddings import OllamaEmbeddings

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

st.set_page_config(page_title="DocuMind AI", page_icon="🧠")
st.title("🧠 DocuMind AI")
st.subheader("Upload a PDF and ask anything!")

uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file is not None:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getvalue())
    st.success("✅ PDF uploaded successfully!")

    # Load and split
    loader = PyPDFLoader("temp.pdf")
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = splitter.split_documents(documents)
    st.info(f"📄 Split into {len(chunks)} chunks!")

    # Question input
    question = st.text_input("💬 Ask anything about your PDF!")

    if question:
        # Use Groq LLM directly without embeddings
        llm = ChatGroq(
            api_key=GROQ_API_KEY,
            model_name="llama-3.3-70b-versatile"
        )
        # Combine all chunks as context
        context = "\n".join([c.page_content for c in chunks[:5]])
        response = llm.invoke(
            f"Answer based on this context:\n{context}\n\nQuestion: {question}"
        )
        st.success("🤖 Answer:")
        st.write(response.content)