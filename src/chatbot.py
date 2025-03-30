from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_community.llms import HuggingFaceEndpoint

def create_chatbot():
    llm = HuggingFaceEndpoint(
        repo_id="mistralai/Mistral-7B-Instruct-v0.2",
        temperature=0.5
    )
    memory = ConversationBufferMemory()
    return ConversationChain(llm=llm, memory=memory)
