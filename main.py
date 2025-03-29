!pip install langchain
!pip install huggingface_hub

import streamlit as st
import requests
from langchain_community.llms import HuggingFaceHub
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader

# Load the model from Hugging Face Hub (Using a free model like OpenAssistant)
hf_llm = HuggingFaceHub(repo_id="OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5", model_kwargs={"temperature": 0.6})

# Define the Streamlit UI
st.title("AI-Powered Customer Support Chatbot")
st.sidebar.header("Chatbot Settings")
st.sidebar.write("Handles ride cancellations, refunds, and delays.")

# Load and preprocess sample FAQs
def load_faq():
    data = """
    Q: How do I cancel my ride?\nA: You can cancel your ride from the app before the driver arrives.
    Q: How do I get a refund?\nA: Refunds are processed within 3-5 business days based on the payment method.
    Q: What happens if my ride is delayed?\nA: If your ride is delayed beyond 15 minutes, you can cancel for free.
    """
    return data

# Create vector store for retrieval
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=10)
documents = text_splitter.split_text(load_faq())
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = FAISS.from_texts(documents, embeddings)
retriever = vector_store.as_retriever()

qa_chain = RetrievalQA(llm=hf_llm, retriever=retriever)

# Chatbot UI
user_input = st.text_input("Ask your query about ride-hailing or e-commerce:")
if st.button("Submit"):
    if user_input:
        response = qa_chain.run(user_input)
        st.write("🤖 Chatbot:", response)
    else:
        st.warning("Please enter a question!")
