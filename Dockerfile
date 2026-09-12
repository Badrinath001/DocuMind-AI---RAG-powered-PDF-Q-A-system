FROM python:3.11-slim
WORKDIR /app
COPY requirements-docker.txt .
RUN pip install -r requirements-docker.txt
COPY . .
ENV HF_HOME=/app/.cache
RUN python -c "from fastembed import TextEmbedding; TextEmbedding('BAAI/bge-small-en-v1.5')"
CMD ["streamlit", "run", "app.py"]