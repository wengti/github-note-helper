import asyncio

from chains.retrieval_grader import (
    RetrievalGraderOutputFormat,
    create_retrieval_grader_chain,
)
from states.states import OverallState


async def retriever_grader_node(state: OverallState):

    print("== RETRIEVER GRADER NODE ==")

    user_query = state.user_query
    retrieved_docs = state.retrieved_docs

    filtered_docs = []

    retriever_grader_chain = create_retrieval_grader_chain()

    async def grade_one_doc(doc) -> bool:
        result: RetrievalGraderOutputFormat = await retriever_grader_chain.ainvoke(
            {
                "user_query": user_query,
                "doc_content": doc.page_content,
            }
        )
        if result.is_relevant:
            filtered_docs.append(doc)
            return False  # No need web search
        else:
            return True  # Need to do web search

    tasks = [grade_one_doc(doc) for doc in retrieved_docs]
    should_web_search_list = await asyncio.gather(*tasks)
    should_web_search = any(should_web_search_list)

    return {
        "should_web_search": should_web_search,
        "filtered_retrieved_docs": filtered_docs,
        "filtered_docs": filtered_docs,
    }
