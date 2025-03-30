from langchain.memory import ConversationBufferMemory

class ChatMemory:
    """Handles conversation memory for the chatbot."""
    
    def __init__(self):
        """Initialize memory storage."""
        self.memory = ConversationBufferMemory()

    def save_message(self, user_message, bot_response):
        """Stores user input and bot response in memory."""
        self.memory.save_context({"input": user_message}, {"output": bot_response})

    def get_memory(self):
        """Retrieves stored conversation memory."""
        return self.memory.buffer

    def clear_memory(self):
        """Clears the stored conversation history."""
        self.memory.clear()
