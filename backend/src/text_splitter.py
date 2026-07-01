# Import the text splitter
from langchain_text_splitters import RecursiveCharacterTextSplitter


# Split transcript into chunks
def split_text(transcript):

    # Create the text splitter
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    # Split the transcript 
    chunks = splitter.split_text(transcript)

    # Return the chunks 
    return chunks
