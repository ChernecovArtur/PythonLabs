from langchain_community.llms import Ollama
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_core.prompts import PromptTemplate

class PermianRAGSystem:
    def __init__(self, vectorstore, llm_model="llama3.2"):
        llm = Ollama(
            model=llm_model,
            base_url="http://localhost:11434",
            temperature=0.3
        )

        template = """
        Ты — эксперт в области палеонтологии и геологической истории Земли.
        Используй ТОЛЬКО информацию из предоставленного контекста
        (статьи Википедии о Пермском периоде).

        Если ответа нет в контексте, напиши:
        "Эта информация отсутствует в предоставленных документах."

        Контекст:
        {context}

        Вопрос: {question}

        Развернутый ответ:
        """

        prompt = PromptTemplate(
            template=template,
            input_variables=["context", "question"]
        )

        self.qa = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=vectorstore.as_retriever(search_kwargs={"k": 4}),
            chain_type_kwargs={"prompt": prompt},
            return_source_documents=True
        )

   # def answer(self, question):
    #    return self.qa({"query": question})
    def answer_question(self, question: str) -> dict:
        result = self.qa({"query": question})

        return {
            "question": question,
            "answer": result["result"],
            "sources": [
                {
                    "title": doc.metadata.get("source", "Unknown"),
                    "content": doc.page_content[:300],
                    "metadata": doc.metadata
                }
                for doc in result["source_documents"]
            ]
        }