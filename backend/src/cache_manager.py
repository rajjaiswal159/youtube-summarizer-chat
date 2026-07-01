import os
import shutil

# Cache directory path
VECTOR_STORE_DIR = "vector_store"

# Maximum number of cached vector stores
MAX_CACHED_VIDEOS = 20


# Remove old cached vector stores
def cleanup_vector_store():

    # Exit if the cache directory doesn't exist
    if not os.path.exists(VECTOR_STORE_DIR):
        return

    # Get all vector store folders
    folders = [
        os.path.join(VECTOR_STORE_DIR, folder)
        for folder in os.listdir(VECTOR_STORE_DIR)
        if os.path.isdir(os.path.join(VECTOR_STORE_DIR, folder))
    ]

    # Exit if cache size is within the limit
    if len(folders) <= MAX_CACHED_VIDEOS:
        return

    # Sort folders by last modified time
    folders.sort(key=os.path.getmtime)

    # Delete the oldest folders until the limit is reached
    while len(folders) > MAX_CACHED_VIDEOS:
        oldest = folders.pop(0)
        shutil.rmtree(oldest)
