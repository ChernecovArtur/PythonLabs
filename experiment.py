from langchain_community.llms import Ollama
from evaluation import keyword_score
from rag_system import PermianRAGSystem

def answer_without_rag(question):
    llm = Ollama(model="llama3.2")
    return llm.invoke(question)

def answer_with_rag(question: str, vectorstore, llm_model="llama3.2") -> dict:
    # Инициализация RAG-системы
    rag_system = PermianRAGSystem(vectorstore, llm_model=llm_model)
    result = rag_system.answer_question(question)
    return result
