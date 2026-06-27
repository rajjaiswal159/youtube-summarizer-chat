import os
import shutil

VECTOR_STORE_DIR = "vector_store"
MAX_CACHED_VIDEOS = 20


def cleanup_vector_store():
    if not os.path.exists(VECTOR_STORE_DIR):
        return

    folders = [
        os.path.join(VECTOR_STORE_DIR, folder)
        for folder in os.listdir(VECTOR_STORE_DIR)
        if os.path.isdir(os.path.join(VECTOR_STORE_DIR, folder))
    ]

    if len(folders) <= MAX_CACHED_VIDEOS:
        return

    folders.sort(key=os.path.getmtime)

    while len(folders) > MAX_CACHED_VIDEOS:
        oldest = folders.pop(0)
        shutil.rmtree(oldest)