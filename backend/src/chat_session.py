from langchain_core.messages import HumanMessage, AIMessage

# Maximum messages to keep in chat history
MAX_MESSAGES = 10

# Store the conversation history
chat_history = []


# Return the current chat history
def get_history():
    return chat_history


# Add a user message to the history
def add_user_message(text: str):
    chat_history.append(HumanMessage(content=text))
    trim_history()


# Add an AI message to the history
def add_ai_message(text: str):
    chat_history.append(AIMessage(content=text))
    trim_history()


# Clear the chat history
def clear_history():
    chat_history.clear()


# Keep only the latest messages
def trim_history():
    if len(chat_history) > MAX_MESSAGES:
        del chat_history[:-MAX_MESSAGES]
