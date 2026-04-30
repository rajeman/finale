# app/agents/chat.py

from agents.mcp.server import MCPServer

from app.agents.base import BaseAgent
from app.agents.prompts import CHAT_INSTRUCTIONS


class ChatAgent(BaseAgent):
    def __init__(self, mcp_servers: list[MCPServer] | None = None):
        super().__init__(
            name="Chat Agent",
            instructions=CHAT_INSTRUCTIONS,
            mcp_servers=mcp_servers,
        )
