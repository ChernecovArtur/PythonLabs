import os
import shutil
from langchain_chroma import Chroma
from langchain_community.embeddings import OllamaEmbeddings

class VectorStoreBuilder:
    def __init__(self, chunks, model="nomic-embed-text", persist_dir="chroma_db"):
        self.chunks = chunks
        self.model = model
        self.persist_dir = persist_dir

    def build(self):
        if os.path.exists(self.persist_dir):
            shutil.rmtree(self.persist_dir)

        embeddings = OllamaEmbeddings(
            model="llama3.2",  # вместо "nomic-embed-text"
            base_url="http://localhost:11434",
            show_progress=True
        )

        vectorstore = Chroma.from_documents(
            documents=self.chunks,
            embedding=embeddings,
            persist_directory=self.persist_dir
        )

        return vectorstore
