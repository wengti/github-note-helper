from chains.hallucination_grader import (
    HallucinationGraderOutputFormat,
    create_hallucination_grader_chain,
)
from states.states import OverallState


def hallucination_grader_node(state: OverallState):

    print("== HALLUCINATION GRADER NODE ==")

    filtered_docs = state.filtered_docs
    ai_answer = state.ai_answer
    cur_hallucination_check_count = state.hallucination_check_count

    context = "\n\n".join([doc.page_content for doc in filtered_docs])

    hallucination_grader_chain = create_hallucination_grader_chain()
    output: HallucinationGraderOutputFormat = hallucination_grader_chain.invoke(
        {
            "context": context,
            "answer": ai_answer,
        }
    )

    return {
        "is_hallucinating": output.is_hallucinating,
        "hallucination_check_count": cur_hallucination_check_count + 1,
    }
