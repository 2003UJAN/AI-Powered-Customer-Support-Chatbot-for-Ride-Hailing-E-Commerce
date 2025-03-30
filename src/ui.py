import streamlit as st
from src.chatbot import create_chatbot

st.title("Multi-Service AI Support Bot")
st.sidebar.header("Service Selection")

service_type = st.sidebar.radio(
    "Choose Service:",
    ("Ride-Hailing", "E-Commerce")
)

# Chat interface
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How can I help?"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    chatbot = create_chatbot()
    response = chatbot.run(f"[{service_type} Query] {prompt}")

    st.session_state.messages.append({"role": "assistant", "content": response})
