# async def main():
#     print("Hello from backend!")
#     graph = create_graph()
#     result = await graph.ainvoke({"history": load_history_3()})
#     print(result["ai_answer"])

import asyncio
import os
from typing import List, Literal
import re

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain.messages import HumanMessage, AIMessage

from graphs.graphs import create_graph

load_dotenv()


class ChatMessage(BaseModel):
    role: Literal["human", "ai"]
    text: str


app = FastAPI()

origins = [os.getenv("FRONTEND_URL")]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/chat", response_class=StreamingResponse)
async def chat_with_agents(chat_history: List[ChatMessage]):
    try:

        if (
            len(chat_history) == 0
            or chat_history[-1].role != "human"
            or not chat_history[-1].text
        ):
            raise HTTPException(
                status_code=422,
                detail="Invalid input.",
            )

        history = [
            (
                AIMessage(content=chat.text)
                if chat.role == "ai"
                else HumanMessage(content=chat.text)
            )
            for chat in chat_history
        ]

        graph = create_graph()
        result = await graph.ainvoke({"history": history})

        if result["error_msg"]:
            raise HTTPException(status_code=500, detail=result["error_msg"])

        for token in re.split(r"(\s+)", result["ai_answer"]):
            if token:
                yield token
                await asyncio.sleep(0.02)

    except HTTPException as error:
        raise

    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
