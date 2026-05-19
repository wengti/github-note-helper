import asyncio
import os
from uuid import uuid4

from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from vector_db import create_vector_store

load_dotenv()

# 0. Hyperparameter
SPLIT_CHUNK_SIZE = 1000
SPLIT_CHUNK_OVERLAP = 200
BATCHED_DOCUMENTS_SIZE = 10


async def split_and_store():

    # 1. Load
    document_links = [
        "https://raw.githubusercontent.com/wengti/langchain-tutorial/refs/heads/main/README.md"
    ]

    document_loader = WebBaseLoader(document_links)
    loaded_documents = document_loader.load()

    # 2. Split
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=SPLIT_CHUNK_SIZE,
        chunk_overlap=SPLIT_CHUNK_OVERLAP,
    )
    split_documents = text_splitter.split_documents(loaded_documents)
    batched_split_documents = [
        split_documents[i : i + BATCHED_DOCUMENTS_SIZE]
        for i in range(0, len(split_documents), BATCHED_DOCUMENTS_SIZE)
    ]

    # 3. Embed and Upload
    async def split_and_store_single_batch(batch_idx, batched_documents):
        print(f"Beginning of Batch {batch_idx}")
        vector_store = create_vector_store()
        uuids = [str(uuid4()) for _ in range(len(batched_documents))]
        await vector_store.aadd_documents(documents=batched_documents, ids=uuids)
        print(f"Ending of Batch {batch_idx}")

    tasks = [
        split_and_store_single_batch(idx, doc)
        for idx, doc in enumerate(batched_split_documents)
    ]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(split_and_store())
