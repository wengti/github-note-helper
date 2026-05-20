import os

from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()


# Structured Output
class HallucinationGraderOutputFormat(BaseModel):
    is_hallucinating: bool = Field(
        description="This value is True if the answer contains content that are not grounded based on the provided context, otherwise it should be false."
    )


def create_hallucination_grader_chain():

    # Prompt Template
    system_prompt = """
    You are a helpful AI assistant that is an expert in determining whether an answer is based on the provided context.
    If you notice that some part of the answer is not based on the provided context, you should answer True, otherwise answer False.
    """

    human_prompt = """
    Context:
    {context}
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
        HallucinationGraderOutputFormat
    )

    # Initialize Chain
    return template | llm_model_with_structured_output
