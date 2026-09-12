import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_community.embeddings import FastEmbedEmbeddings

load_dotenv()


def get_groq_api_key() -> str:
    try:
        if "GROQ_API_KEY" in st.secrets:
            return st.secrets["GROQ_API_KEY"]
    except Exception:
        pass
    return os.getenv("GROQ_API_KEY", "")


def get_groq_model() -> str:
    try:
        if "GROQ_MODEL" in st.secrets:
            return st.secrets["GROQ_MODEL"]
    except Exception:
        pass
    return os.getenv("GROQ_MODEL", "openai/gpt-oss-20b")


GROQ_API_KEY = get_groq_api_key()
GROQ_MODEL = get_groq_model()


@st.cache_resource
def get_vector_store(chunks):
    embeddings = FastEmbedEmbeddings(model_name="BAAI/bge-small-en-v1.5")
    return Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name="documind_session",
    )


@st.cache_resource
@st.cache_resource
def get_llm(api_key: str, model: str):
    return ChatGroq(
        api_key=api_key,
        model=model,
    )


st.set_page_config(page_title="DocuMind AI", page_icon="🧠")
st.title("🧠 DocuMind AI")
st.subheader("Upload a PDF and ask anything!")

if not GROQ_API_KEY:
    st.warning(
        "GROQ_API_KEY is missing. Add it in Streamlit Cloud secrets or your local .env file before using the app."
    )
    st.stop()

uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file is not None:
    temp_pdf = Path("temp.pdf")
    with temp_pdf.open("wb") as f:
        f.write(uploaded_file.getvalue())
    st.success("✅ PDF uploaded successfully!")

    try:
        loader = PyPDFLoader(str(temp_pdf))
        documents = loader.load()
        if not documents:
            st.error("❌ No readable pages were found in the uploaded PDF.")
            st.stop()

        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = splitter.split_documents(documents)
        st.info(f"📄 Split into {len(chunks)} chunks!")

        with st.spinner("🔍 Indexing document for retrieval..."):
            vectorstore = get_vector_store(chunks)
        st.success("✅ Document indexed and ready for questions!")

        question = st.text_input("💬 Ask anything about your PDF!")

        if question:
            retrieved_docs = vectorstore.similarity_search(question, k=4)
            context = "\n\n".join([doc.page_content for doc in retrieved_docs])

            llm = get_llm(GROQ_API_KEY, GROQ_MODEL)
            response = llm.invoke(
                f"Answer based on this context:\n{context}\n\nQuestion: {question}"
            )

            st.success("🤖 Answer:")
            st.write(response.content)

            with st.expander("📚 Sources used"):
                for i, doc in enumerate(retrieved_docs, 1):
                    st.markdown(f"**Chunk {i}** (page {doc.metadata.get('page', '?')})")
                    st.text(doc.page_content[:300] + "...")
    except Exception as exc:
        st.error(f"❌ Failed to process the PDF: {exc}")
        st.stop()