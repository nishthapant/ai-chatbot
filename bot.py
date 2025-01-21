import chainlit as cl
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# AI Chat Implementation
"""
1. Define the HuggingFace endpoint
2. Define the chat model
3. Define chat log
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

chat_log = [
    SystemMessage(content="You are an AI assistant."),
]


# UI Implementation
"""
1. Define what the bot should say when the chat starts
2. Define what the bot should say when the chat ends (OPTIONAL)
4. Define the logic to be run when input is received from the .
    - Need to connect the model here.
"""

START_STATEMENT = "Hello! How can I assist you today?"
EXIT_STATEMENT = "Bye now!"

exit_tokens = ["bye", "exit", "finish", "end"]

@cl.on_chat_start
async def handle_chat_start():
    await cl.Message(content=START_STATEMENT).send()

# @cl.on_chat_end
# async def handle_chat_end():
#     await cl.Message(content=EXIT_STATEMENT).send()

@cl.on_message
async def handle_user_prompt(message: cl.Message):
    #  convert user prompt into a standardised human message
    user_prompt = HumanMessage(content=message.content)

    # if user_prompt.content.lower() in exit_tokens:
        # await handle_chat_end()

    chat_log.append(user_prompt)

    #  add logic to send the message to the model
    #  get a response from the ai model
    response = await chat.ainvoke(chat_log)

    # update chat log  
    chat_log.append(AIMessage(content=response.content))
    
    #  send it back to the user through the UI
    await cl.Message(content=response.content).send()


