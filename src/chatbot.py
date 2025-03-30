from langchain.chains import ConversationChain
from langchain_community.llms import HuggingFaceEndpoint
from models.memory import ChatMemory

# Initialize LLM and memory
llm = HuggingFaceEndpoint(repo_id="mistralai/Mistral-7B-Instruct-v0.2", temperature=0.5)
memory = ChatMemory()
chat_chain = ConversationChain(llm=llm, memory=memory.memory)

def get_chat_response(user_input):
    """Handles conversation and memory storage."""
    response = chat_chain.run(user_input)
    memory.save_message(user_input, response)
    return response
