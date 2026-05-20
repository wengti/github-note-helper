from states.states import OverallState
from utils.vector_db import create_vector_store


def retriever_node(state: OverallState):
    print("== RETRIEVER NODE ==")
    user_query = state.user_query
    vector_store = create_vector_store()
    results = vector_store.similarity_search(query=user_query, k=5)
    return {"retrieved_docs": results}  # metadata = {"source": }, page_content
