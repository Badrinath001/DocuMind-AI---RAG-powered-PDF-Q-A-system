import os
import streamlit as st
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings

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

    # --- NEW: Embed chunks and build a vector store ---
    with st.spinner("🔍 Indexing document for retrieval..."):
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            collection_name="documind_session"
        )
    st.success("✅ Document indexed and ready for questions!")

    # Question input
    question = st.text_input("💬 Ask anything about your PDF!")

    if question:
        # --- NEW: Retrieve only the chunks relevant to THIS question ---
        retrieved_docs = vectorstore.similarity_search(question, k=4)
        context = "\n\n".join([doc.page_content for doc in retrieved_docs])

        llm = ChatGroq(
            api_key=GROQ_API_KEY,
            model_name="llama-3.3-70b-versatile"
        )

        response = llm.invoke(
            f"Answer based on this context:\n{context}\n\nQuestion: {question}"
        )

        st.success("🤖 Answer:")
        st.write(response.content)

        # Optional: show which chunks were retrieved, for transparency/debugging
        with st.expander("📚 Sources used"):
            for i, doc in enumerate(retrieved_docs, 1):
                st.markdown(f"**Chunk {i}** (page {doc.metadata.get('page', '?')})")
                st.text(doc.page_content[:300] + "...")