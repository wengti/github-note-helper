import os

from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()


# Structured Output
class UsefulnessGraderOutputFormat(BaseModel):
    is_useful: bool = Field(
        description="This value is True if the generated response is useful for answering the user query, otherwise is False"
    )


def create_usefulness_grader_chain():

    # Prompt Template
    system_prompt = """
    You are a helpful AI assistant that is an expert in determining if a response is useful for answering the user query.
    Answer False if you detect the following pattern in the answer:
        - It is ambiguous and lacks of elaboration.
        - It admits the lack of evidence in the provided sources.
        - It answer the user query completely, leaving gap for the user to deduce.
    Otherwise, answer True.
    """

    human_prompt = """
    User Query: {user_query}
    Answer: {answer}
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
        UsefulnessGraderOutputFormat
    )

    # Initialize Chain
    return template | llm_model_with_structured_output
