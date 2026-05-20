import os

from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()


# Structured Output
class RouterOutputFormat(BaseModel):
    should_retrieve: bool = Field(
        description="This value is True if the user query is relevant to LangChain, LangGraph, RAG or LCEL."
    )


def create_router_chain():

    # Prompt Template
    system_prompt = """
    You are a helpful AI assistant that is an expert in determining whether you need to search from vector database for information to answer the user query.
    Since you have access to a vector database consisting of knowledge about LangChain, LangGraph, RAG and LCEL, if the user query is relevant to these, answer True.
    Otherwise, answer False.
    """

    human_prompt = """
    User Query: {user_query}
    """

    template = ChatPromptTemplate(
        [
            ("system", system_prompt),
            ("human", human_prompt),
        ],
    )

    # Initialize Model
    llm_model = init_chat_model(
        model=os.getenv("MODEL_NAME"),
        temperature=0,
    )
    llm_model_with_structured_output = llm_model.with_structured_output(
        RouterOutputFormat
    )

    # Initialize Chain
    return template | llm_model_with_structured_output
