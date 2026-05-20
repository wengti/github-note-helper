import asyncio

from chains.test_history.load_history import (
    load_history_1,
    load_history_2,
    load_history_3,
)
from graphs.graphs import create_graph
from nodes.retriever import retriever_node


async def main():
    print("Hello from backend!")
    graph = create_graph()
    result = await graph.ainvoke({"history": load_history_3()})
    print(result["ai_answer"])


if __name__ == "__main__":
    asyncio.run(main())
