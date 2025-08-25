# free-ai-chatbot
A free local AI chatbot built with LangChain and Streamlit
# Free AI Chatbot 🤖

A completely free, locally-running AI chatbot built with LangChain and Streamlit, powered by Ollama and open-source LLMs.

## Features

- 💬 Beautiful chat interface with Streamlit
- 🚀 100% free and local - no API costs
- 💾 Conversation memory
- ⚡ Fast responses with streaming
- 🎨 Customizable AI personality

## Installation

1. Install Ollama:
   ```bash
   # Visit https://ollama.ai/ and download Ollama
   ollama pull llama3.2:1b
# or: ollama pull phi3:mini
# or: ollama pull gemma:
2bgit clone https://github.com/your-username/free-ai-chatbot.git
cd free-ai-chatbot
pip install -r requirements.txt
streamlit run chatbot_ui.py
Usage
Open your browser to http://localhost:8501

Start chatting with your AI assistant!

The chat history is maintained during your session

Customization
Change the AI's personality by modifying the system prompt in chatbot_ui.py

Try different models by changing the model parameter

Add your own data with RAG (Retrieval Augmented Generation)

Models
Recommended models for good performance:

llama3.2:1b - Fastest, good for basic chat

phi3:mini - Excellent balance of speed and quality

gemma:2b - Google's efficient model
