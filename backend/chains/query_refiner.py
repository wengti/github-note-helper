import os

from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()


# Structured Output
class QueryRefinerOutputFormat(BaseModel):
    user_query: str = Field(
        description="It holds the refined version of the user query from the original raw user query, to facilitate searching for information."
    )


def create_query_refiner_chain():

    # Prompt Template
    system_prompt = """
    You are a helpful AI assistant that is an expert in refining the user query. 
    You should summarize the user query and refine down to the key points behind it and reframe it as a shorter but more precise question.
    You should also refer to the chat history to help you refine the questions.
    Your output will be used to search for information from a vector database or from the web.
    """

    template = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            MessagesPlaceholder("history"),
        ],
    )

    # Initialize Model
    llm_model = init_chat_model(
        model=os.getenv("MODEL_NAME"),
        temperature=0,
    )
    llm_model_with_structured_output = llm_model.with_structured_output(
        QueryRefinerOutputFormat
    )

    # Initialize Chain
    return template | llm_model_with_structured_output
