import streamlit as st
from document_processor import DocumentProcessor
from vectorstore_builder import VectorStoreBuilder
from rag_system import PermianRAGSystem
from experiment import answer_without_rag

st.title("Чат о Пермском периоде")

if "data_loaded" not in st.session_state:
    st.info("Гружусь...Жди...Прогресс в VS пишется")
    processor = DocumentProcessor("data")
    data = processor.load_and_chunk()

    builder = VectorStoreBuilder(data["chunks"])
    vectorstore = builder.build()

    st.session_state.rag_system = PermianRAGSystem(vectorstore)
    st.session_state.data_loaded = True
    st.success("Прогрузилось")

rag_system = st.session_state.rag_system

if "history" not in st.session_state:
    st.session_state.history = []

user_question = st.text_input("Вопрос:")

if st.button("Задать вопрос") and user_question.strip():
    ans_no_rag = answer_without_rag(user_question)
    ans_rag = rag_system.answer_question(user_question)


    st.session_state.history.append({
        "question": user_question,
        "ans_no_rag": ans_no_rag,
        "ans_rag": ans_rag["answer"],
        "sources": ans_rag["sources"]
    })
    
for entry in reversed(st.session_state.history):
    st.markdown(f"### Вопрос: {entry['question']}")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Ответ без RAG")
        st.write(entry["ans_no_rag"])
    with col2:
        st.subheader("Ответ с RAG")
        st.write(entry["ans_rag"])
    
    with st.expander("Источники"):
        for src in entry["sources"]:
            st.markdown(f"- **{src['title']}**: {src['content'][:300]}...")
    
    st.markdown("---")
