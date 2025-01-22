# **AI Chatbot**

## Project Description
This is a simple AI chatbot built using Python, LangChain, and Chainlit. The chatbot is powered by the Phi-3-Mini-4K-Instruct model, which is exposed through the Hugging Face framework. This chatbot maintains context during a user session making it a stateful conversational AI agent.


## Tech Stack
- Backend: Python, LangChain
- Frontend: Chainlit
- AI Model: Phi-3-Mini-4K-Instruct via Hugging Face
   - Connecting Langchain and Huggingface: [ChatHuggingface class](https://python.langchain.com/api_reference/huggingface/chat_models/langchain_huggingface.chat_models.huggingface.ChatHuggingFace.html)


## Getting Started
Follow the steps below to install dependencies and run the chatbot.

### Prerequisites
Make sure you have the following installed on your system:
- Python 3.x
- Pip (Python package manager)
- Git (optional, for version control)

### Installation
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/ai-chatbot.git
   cd ai-chatbot
   ```

2. Install dependencies:  
   Run the following command to install all necessary dependencies:  
   ```bash
   python3 install_dependencies.py
   ```

### Run the chatbot
After installing dependencies, start the chatbot by running:  

```bash
python3 run.py
```

The chatbot will start and you can interact with it through the provided Chainlit interface.


## Future Improvements
Planned enhancements include:
- Converting this chatbot into a personal assistant by integrating a personal knowledege base to leverage the accuracy of the RAG framework.
- Deploying the chatbot as a web service.  


## Acknowledgements
1. Model used: [Phi-3-Mini-4K-Instruct](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct)
2. Learning and Reference resources
   - [Langchain](https://api.python.langchain.com/en/latest/langchain_api_reference.html)
   - [ChatHuggingFace](https://python.langchain.com/api_reference/huggingface/chat_models/langchain_huggingface.chat_models.huggingface.ChatHuggingFace.html)
   - [Chainlit](https://docs.chainlit.io/get-started/overview)


## Contact  
For questions or suggestions, feel free to reach out to:
Nishtha Pant via nishthapant2024@gmail.com