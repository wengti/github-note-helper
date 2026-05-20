from chains.response_generator import (
    ResponseGeneratorOutputFormat,
    create_response_generator_chain,
)
from states.states import OverallState


def response_generator_node(state: OverallState):

    print("== RESPONSE GENERATOR NODE ==")

    user_query = state.user_query
    filtered_docs = state.filtered_docs
    hallucination_check_count = state.hallucination_check_count

    filtered_docs_dict = {}
    for doc in filtered_docs:
        key = doc.metadata["source"]
        if key in filtered_docs_dict:
            new_val = "\n\n".join([filtered_docs_dict[key], doc.page_content])
            filtered_docs_dict[key] = new_val
        else:
            filtered_docs_dict[key] = doc.page_content

    doc_content = "\n\n".join(
        [f"Source: {key} \n Content: {val}" for key, val in filtered_docs_dict.items()]
    )

    counter_hallucination_prompt = (
        f"""
        You have tried to generate content that is not based on the provided context before. 
        Make sure you do not do this in this attempt. Generate solely based on the provided context.
    """
        if hallucination_check_count > 0
        else ""
    )

    response_generator_chain = create_response_generator_chain()
    output: ResponseGeneratorOutputFormat = response_generator_chain.invoke(
        {
            "user_query": user_query,
            "doc_content": doc_content,
            "counter_hallucination_prompt": counter_hallucination_prompt,
        }
    )

    return {"ai_answer": output.ai_answer}
