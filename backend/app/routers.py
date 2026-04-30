"""HTTP routers for the FastAPI app."""

from uuid import UUID

from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.agents.chat import ChatAgent
from app.streamable_http_mcp import streamable_http_mcp_client

router = APIRouter(tags=["chat"])

chat_agents_by_session_id: dict[str, ChatAgent] = {}


class ChatRequest(BaseModel):
    id: UUID
    message: str = Field(min_length=1)


@router.post("/chat")
async def chat(req: ChatRequest):
    session_id = str(req.id)
    session_agent = chat_agents_by_session_id.get(session_id)
    if not session_agent:
        mcp = streamable_http_mcp_client()
        await mcp.connect()
        session_agent = ChatAgent(mcp_servers=[mcp])
        # session_agent = ChatAgent()

        chat_agents_by_session_id[session_id] = session_agent
    result = await session_agent.run(req.message)
    return {"response": result}
