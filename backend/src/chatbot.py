from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
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
    prompt = ChatPromptTemplate.from_template(
        """
        Answer the question using only the context below.

        Context:
        {context}

        Question:
        {question}

        If the answer is not in the context,
        say "I could not find that information in the video."
        """
    )

    # LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash"
    )

    # LCEL Chain
    chain = (
        {
            "context": retriever | RunnableLambda(format_docs),
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain