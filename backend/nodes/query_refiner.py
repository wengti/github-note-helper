from chains.query_refiner import QueryRefinerOutputFormat, create_query_refiner_chain
from states.states import OverallState


def query_refiner_node(state: OverallState):
    print("== QUERY REFINER NODE ==")
    history = state.history
    query_refiner_chain = create_query_refiner_chain()
    output: QueryRefinerOutputFormat = query_refiner_chain.invoke({"history": history})
    return {"user_query": output.user_query}
