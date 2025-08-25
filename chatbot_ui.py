# chatbot_ui.py (updated with streaming)
import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.callbacks import BaseCallbackHandler

class StreamHandler(BaseCallbackHandler):
    def __init__(self, container):
        self.container = container
        self.text = ""
    
    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.text += token
        self.container.markdown(self.text + "▌")

# Set up the page
st.set_page_config(page_title="Your Free AI Chatbot", page_icon="🤖")

@st.cache_resource
def load_llm():
    return OllamaLLM(model="llama3.2:1b", callbacks=[])

llm = load_llm()
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Keep answers under 3 sentences."),
    ("human", "{input}")
])

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

st.title("💬 Your Free Chatbot")
st.caption("Now with faster responses! ⚡")

# React to user input
if user_input := st.chat_input("What's on your mind?"):
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Generate AI response with streaming
    with st.chat_message("assistant"):
        stream_handler = StreamHandler(st.empty())
        response = llm.stream(prompt.format(input=user_input), config={"callbacks": [stream_handler]})
        
        full_response = ""
        for chunk in response:
            full_response += chunk
            stream_handler.container.markdown(full_response)
        
        st.session_state.messages.append({"role": "assistant", "content": full_response})