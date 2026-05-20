from typing import List

from pydantic import BaseModel, Field
from langchain_core.documents import Document
from langchain_core.messages import BaseMessage


class OverallState(BaseModel):
    history: List[BaseMessage] = Field(default_factory=list)
    user_query: str = Field(default="")
    should_retrieve: bool = Field(default=True)
    should_web_search: bool = Field(default=False)
    retrieved_docs: List[Document] = Field(default_factory=list)
    filtered_retrieved_docs: List[Document] = Field(default_factory=list)
    filtered_docs: List[Document] = Field(default_factory=list)
    ai_answer: str = Field(default="")
    is_hallucinating: bool = Field(default=False)
    hallucination_check_count: int = Field(default=0)
    is_useful: bool = Field(default=True)
    usefulness_check_count: int = Field(default=0)
    error_msg: str = Field(default="")
