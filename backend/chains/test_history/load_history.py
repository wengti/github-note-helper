from typing import List

from langchain.messages import AIMessage, HumanMessage
from langchain_core.messages import BaseMessage


def load_history_1() -> List[BaseMessage]:

    human_query_1 = "What is LCEL?"
    ai_response = """
LCEL stands for LangChain Express Language. In the provided tutorial, it is described as a way to build pipelines by connecting `Runnable` components with the `|` pipe operator, so the output of one component becomes the input of the next. [1]

References:
[1] https://raw.githubusercontent.com/wengti/langchain-tutorial/refs/heads/main/README.md
"""
    human_query_2 = "Show me an example of how it is used to create a RAG pipeline."

    return [
        HumanMessage(content=human_query_1),
        AIMessage(content=ai_response),
        HumanMessage(content=human_query_2),
    ]


def load_history_2() -> List[BaseMessage]:

    human_query_1 = "What is Yorushika?"
    ai_response = """
Yorushika is a famous Japense Pop Song duo made up of n-buna and suis [1].

References:
[1] https://en.wikipedia.org/wiki/Yorushika
"""
    human_query_2 = "What is their latest release?"

    return [
        HumanMessage(content=human_query_1),
        AIMessage(content=ai_response),
        HumanMessage(content=human_query_2),
    ]


def load_history_3() -> List[BaseMessage]:

    human_query_1 = "What is LCEL?"
    ai_response = """
LCEL stands for LangChain Express Language. In the provided tutorial, it is described as a way to build pipelines by connecting `Runnable` components with the `|` pipe operator, so the output of one component becomes the input of the next. [1]

References:
[1] https://raw.githubusercontent.com/wengti/langchain-tutorial/refs/heads/main/README.md
"""
    human_query_2 = "Is it a must to learn it in order to get into AI industry?"

    return [
        HumanMessage(content=human_query_1),
        AIMessage(content=ai_response),
        HumanMessage(content=human_query_2),
    ]
