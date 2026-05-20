from chains.usefulness_grader import (
    UsefulnessGraderOutputFormat,
    create_usefulness_grader_chain,
)
from states.states import OverallState


def usefulness_grader_node(state: OverallState):

    print("== USEFULNESS GRADER NODE ==")

    user_query = state.user_query
    ai_answer = state.ai_answer
    cur_usefulness_check_count = state.usefulness_check_count

    usefulness_grader_chain = create_usefulness_grader_chain()
    output: UsefulnessGraderOutputFormat = usefulness_grader_chain.invoke(
        {
            "user_query": user_query,
            "answer": ai_answer,
        }
    )

    return {
        "is_useful": output.is_useful,
        "usefulness_check_count": cur_usefulness_check_count + 1,
    }
