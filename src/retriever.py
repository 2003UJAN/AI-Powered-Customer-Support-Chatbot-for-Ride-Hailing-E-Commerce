from langchain.retrievers import WikipediaRetriever
from src.chatbot import create_chatbot

def get_rag_response(service_type, prompt):
    retriever = WikipediaRetriever()
    docs = retriever.get_relevant_documents(f"{service_type} customer support")

    chatbot = create_chatbot()
    rag_prompt = f"""Use context to answer {service_type} queries:
    {docs}

    Current conversation:
    {chatbot.memory.buffer}

    User: {prompt}
    Assistant:"""

    return chatbot.run(rag_prompt)

