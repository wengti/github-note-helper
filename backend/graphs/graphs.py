from typing import List

from langgraph.graph import END, START, StateGraph
from langchain_core.documents import Document

from nodes.hallucination_grader import hallucination_grader_node
from nodes.query_refiner import query_refiner_node
from nodes.response_generator import response_generator_node
from nodes.retriever import retriever_node
from nodes.retriever_grader import retriever_grader_node
from nodes.router import router_node
from nodes.usefulness_grader import usefulness_grader_node
from nodes.web_search import web_search_node
from states.states import OverallState


def create_graph():
    builder = StateGraph(OverallState)

    # Node Name
    QUERY_REFINER_NODE = "query_refiner_node"
    RETRIEVER_NODE = "retriever_node"
    RETRIEVER_GRADER_NODE = "retriever_grader_node"
    WEB_SEARCH_NODE = "web_search_node"
    RESPONSE_GENERATOR_NODE = "response_generator_node"
    HALLUCINATION_GRADER_NODE = "hallucination_grader_node"
    USEFULNESS_GRADER_NODE = "usefulness_grader_node"
    ROUTER_NODE = "router_node"

    # Nodes
    builder.add_node(QUERY_REFINER_NODE, query_refiner_node)
    builder.add_node(RETRIEVER_NODE, retriever_node)
    builder.add_node(RETRIEVER_GRADER_NODE, retriever_grader_node)
    builder.add_node(WEB_SEARCH_NODE, web_search_node)
    builder.add_node(RESPONSE_GENERATOR_NODE, response_generator_node)
    builder.add_node(HALLUCINATION_GRADER_NODE, hallucination_grader_node)
    builder.add_node(USEFULNESS_GRADER_NODE, usefulness_grader_node)
    builder.add_node(ROUTER_NODE, router_node)

    # Edges

    def should_retrieve(state: OverallState):
        if state.should_retrieve:
            return RETRIEVER_NODE
        else:
            return WEB_SEARCH_NODE

    def should_web_search(state: OverallState):
        if state.should_web_search:
            return WEB_SEARCH_NODE
        else:
            return RESPONSE_GENERATOR_NODE

    def should_regenerate(state: OverallState):
        if not state.is_hallucinating or state.hallucination_check_count >= 2:
            return USEFULNESS_GRADER_NODE
        elif state.is_hallucinating:
            return RESPONSE_GENERATOR_NODE

    def should_repeat_cycle(state: OverallState):
        if state.is_useful or state.usefulness_check_count >= 2:
            return "end"
        elif not state.is_useful:
            return WEB_SEARCH_NODE

    builder.add_edge(START, QUERY_REFINER_NODE)
    builder.add_edge(QUERY_REFINER_NODE, ROUTER_NODE)
    builder.add_conditional_edges(
        ROUTER_NODE,
        should_retrieve,
        {
            WEB_SEARCH_NODE: WEB_SEARCH_NODE,
            RETRIEVER_NODE: RETRIEVER_NODE,
        },
    )
    builder.add_edge(RETRIEVER_NODE, RETRIEVER_GRADER_NODE)
    builder.add_conditional_edges(
        RETRIEVER_GRADER_NODE,
        should_web_search,
        {
            WEB_SEARCH_NODE: WEB_SEARCH_NODE,
            RESPONSE_GENERATOR_NODE: RESPONSE_GENERATOR_NODE,
        },
    )
    builder.add_edge(WEB_SEARCH_NODE, RESPONSE_GENERATOR_NODE)

    builder.add_edge(RESPONSE_GENERATOR_NODE, HALLUCINATION_GRADER_NODE)
    builder.add_conditional_edges(
        HALLUCINATION_GRADER_NODE,
        should_regenerate,
        {
            USEFULNESS_GRADER_NODE: USEFULNESS_GRADER_NODE,
            RESPONSE_GENERATOR_NODE: RESPONSE_GENERATOR_NODE,
        },
    )

    builder.add_conditional_edges(
        USEFULNESS_GRADER_NODE,
        should_repeat_cycle,
        {
            "end": END,
            WEB_SEARCH_NODE: WEB_SEARCH_NODE,
        },
    )

    # Graph
    graph = builder.compile()

    # Plot Image
    with open("graph.png", "wb") as f:
        f.write(graph.get_graph().draw_mermaid_png())

    return graph
