from src.chatbot import create_chatbot

def test_chatbot():
    chatbot = create_chatbot()
    response = chatbot.run("Hello!")
    assert isinstance(response, str)
