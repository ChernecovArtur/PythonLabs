from document_processor import DocumentProcessor
from vectorstore_builder import VectorStoreBuilder
from rag_system import PermianRAGSystem
from experiment import answer_without_rag, answer_with_rag
from questions import QUESTIONS
from evaluation import keyword_score

processor = DocumentProcessor("data")
data = processor.load_and_chunk()

builder = VectorStoreBuilder(data["chunks"])
vectorstore = builder.build()

rag = PermianRAGSystem(vectorstore)

for q in QUESTIONS:
    question = q["question"]
    keywords = q["expected_keywords"]
    print("\n" + "="*80) 
    print(f"Вопрос: {question}") 
    # Ответ без RAG 
    ans_no_rag = answer_without_rag(question) 
    print("\nОтвет без RAG:") 
    print(ans_no_rag) 
    # Ответ с RAG 
    ans_rag = answer_with_rag(question, vectorstore) 
    print("\nОтвет с RAG:") 
    print(ans_rag['answer']) 
    print("Источники:", [src['title'] for src in ans_rag['sources']])
