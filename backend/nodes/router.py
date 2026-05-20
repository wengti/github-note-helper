from chains.router import RouterOutputFormat, create_router_chain
from states.states import OverallState


def router_node(state: OverallState):
    print("== ROUTER NODE ==")
    user_query = state.user_query

    router_chain = create_router_chain()
    output: RouterOutputFormat = router_chain.invoke({"user_query": user_query})
    return {"should_retrieve": output.should_retrieve}
