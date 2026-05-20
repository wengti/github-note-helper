import os

from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()


# Structured Output
class RetrievalGraderOutputFormat(BaseModel):
    is_relevant: bool = Field(
        description="This value is True if the provided document content is relevant to the user query, otherwise it should be false."
    )


def create_retrieval_grader_chain():

    # Prompt Template
    system_prompt = """
    You are a helpful AI assistant that is an expert in deciding if a provided document is relevant to the user query.
    If the document is relevant to the user query, respond True otherwise respond False.
    """

    human_prompt = """
    User Query: {user_query}
    Document Content: {doc_content}
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
        RetrievalGraderOutputFormat
    )

    # Initialize Chain
    return template | llm_model_with_structured_output
