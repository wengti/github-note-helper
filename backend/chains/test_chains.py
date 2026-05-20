import pytest

from chains.hallucination_grader import create_hallucination_grader_chain
from chains.retrieval_grader import create_retrieval_grader_chain
from chains.usefulness_grader import create_usefulness_grader_chain

# @pytest.mark.parametrize(
#     ("user_query", "doc_content", "expected_result"),
#     [
#         ("What is LCEL?", "LCEL is LangChain Express Language.", True),
#         ("What is LCEL?", "I like chicken wings.", False),
#     ],
# )
# def test_retrieval_grader_chain(user_query, doc_content, expected_result):
#     retrieval_grader = create_retrieval_grader_chain()
#     output = retrieval_grader.invoke(
#         {
#             "user_query": user_query,
#             "doc_content": doc_content,
#         }
#     )
#     assert output.is_relevant == expected_result


@pytest.mark.parametrize(
    ("context", "answer", "expected_result"),
    [
        (
            "LCEL can be used in building a RAG pipeline.",
            "RAG can be built using LCEL",
            False,
        ),
        (
            "LCEL can be used in building a RAG pipeline.",
            "You need LCEL to learn AI",
            True,
        ),
    ],
)
def test_hallucination_grader_chain(context, answer, expected_result):
    hallucination_grader = create_hallucination_grader_chain()
    output = hallucination_grader.invoke(
        {
            "context": context,
            "answer": answer,
        }
    )
    assert output.is_hallucinating == expected_result


# @pytest.mark.parametrize(
#     ("user_query", "answer", "expected_result"),
#     [
#         (
#             "Can LCEL be used to build a RAG pipeline?",
#             "Yes, LCEL is useful for building multi-step agents workflow, including a RAG pipeline.",
#             True,
#         ),
#         (
#             "Can LCEL be used to build a RAG pipeline?",
#             "LCEL stands for LangChain Express Language.",
#             False,
#         ),
#     ],
# )
# def test_usefulness_grader_chain(user_query, answer, expected_result):
#     usefulness_grader_chain = create_usefulness_grader_chain()
#     output = usefulness_grader_chain.invoke(
#         {"user_query": user_query, "answer": answer}
#     )
#     assert output.is_useful == expected_result
