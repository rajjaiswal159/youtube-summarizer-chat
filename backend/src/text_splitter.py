# Import recursive text splitter
from langchain_text_splitters import RecursiveCharacterTextSplitter


# Split transcript into chunks
def split_text(transcript):

    # Create text splitter object
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    # Convert transcript into chunks
    chunks = splitter.split_text(transcript)

    # Return chunk list
    return chunks