from langchain_core.messages import HumanMessage, AIMessage

MAX_MESSAGES = 10

chat_history = []


def get_history():
    return chat_history


def add_user_message(text: str):
    chat_history.append(HumanMessage(content=text))
    trim_history()


def add_ai_message(text: str):
    chat_history.append(AIMessage(content=text))
    trim_history()


def clear_history():
    chat_history.clear()


def trim_history():
    if len(chat_history) > MAX_MESSAGES:
        del chat_history[:-MAX_MESSAGES]