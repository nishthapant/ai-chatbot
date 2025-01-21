import chainlit as cl
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# AI Chat Implementation
"""
1. Define the HuggingFace endpoint
2. Define the chat model
4. Integrate chat invoking logic in the UI
"""

llm = HuggingFaceEndpoint(
    repo_id="microsoft/Phi-3-mini-4k-instruct",
    task="text-generation",
    max_new_tokens=256,
    do_sample=False,
    repetition_penalty=1.03,
)

chat = ChatHuggingFace(llm=llm, verbose=True)

# UI Implementation
"""
1. Define what the bot should say when the chat starts
2. Define what the bot should say when the chat ends (OPTIONAL)
3. Maintain a user session to store chat history for context
4. Invoke chat, send user prompt, get a response and send it to UI
"""

START_STATEMENT = """
Hello! I am a helpful AI assistant. How can I assist you today?
NOTE: This session will end after 30 second of inactivity.
"""
EXIT_STATEMENT = "The session has ended due to inactivity. New session created."

@cl.on_chat_start
async def handle_chat_start():
    system_prompt = SystemMessage(content="You are a helpful AI assistant.")

    cl.user_session.set("username", "Guest")
    cl.user_session.set("chat_history", [system_prompt])

    await cl.Message(content=START_STATEMENT).send()
# ========================================================
# OPTIONAL
# @cl.on_chat_end
# async def handle_chat_end():
#     cl.user_session.clear()
#     await cl.Message(content=EXIT_STATEMENT).send()
# ========================================================

@cl.on_message
async def handle_user_prompt(message: cl.Message):
    #  convert user prompt into a standardised human message
    user_prompt = HumanMessage(content=message.content)

    # get chat_history for this session
    chat_history = cl.user_session.get("chat_history")
    chat_history.append(user_prompt)

    #  invoke chat and get a response from the ai model
    response = await chat.ainvoke(chat_history)

    # update chat history  
    chat_history.append(AIMessage(content=response.content))
    
    #  send it back to the user through the UI
    await cl.Message(content=response.content).send()


