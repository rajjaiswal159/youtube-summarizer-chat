from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables import RunnableLambda


# Convert documents into a single string
def format_docs(docs):
    return "\n\n".join(
        doc.page_content for doc in docs
    )

def create_rag_chain(vector_store):

    # Create retriever
    retriever = vector_store.as_retriever(
        search_kwargs={"k": 2}
    )

    # Prompt
    prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are an AI assistant that answers questions about a YouTube video.
            
            Use ONLY the provided transcript context to answer the user's question.
            
            If the answer is not in the transcript, reply:
            "I couldn't find that information in the video transcript."
            
            Be accurate, concise, and clear.
            Use Markdown formatting and bullet points when helpful.
            Do not make up information.
            
            Transcript Context:
            {context}
            """
        ),

        MessagesPlaceholder(variable_name="chat_history"),

        (
            "human",
            "{question}"
        )
    ]
    )

    # LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash"
    )

    # LCEL Chain
    chain = (
        {
            "context": (
                RunnableLambda(lambda x: x["question"])
                | retriever
                | RunnableLambda(format_docs)
            ),
            "question": RunnableLambda(lambda x: x["question"]),
            "chat_history": RunnableLambda(lambda x: x["chat_history"]),
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain