from langchain_tavily import TavilySearch

from langchain_core.documents import Document

from states.states import OverallState


def web_search_node(state: OverallState):

    print("== WEB SEARCH NODE ==")

    # Variable
    user_query = state.user_query
    filtered_retrieved_docs = state.filtered_retrieved_docs
    usefulness_check_count = state.usefulness_check_count

    new_filtered_docs = filtered_retrieved_docs
    new_error_msg = ""

    # Search tool
    MAX_RESULTS = 10 if usefulness_check_count > 0 else 5
    search_tool = TavilySearch(
        max_results=MAX_RESULTS,
    )

    outputs = search_tool.invoke({"query": user_query})

    if "error" in outputs:
        new_error_msg = str(outputs["error"])
    else:
        # Format result
        for item in outputs["results"]:
            new_filtered_docs.append(
                Document(
                    page_content=item["content"],
                    metadata={
                        "source": item["url"],
                    },
                )
            )

    # Return and update state
    return {
        "filtered_docs": new_filtered_docs,
        "hallucination_check_count": 0,
        "error_msg": new_error_msg,
    }
