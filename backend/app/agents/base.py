from agents import Agent, Runner
from agents.mcp.server import MCPServerStreamableHttp


class BaseAgent:
    def __init__(
        self,
        name: str,
        instructions: str,
        tools=None,
        model: str = "gpt-4o-mini",
        mcp_servers: list[MCPServerStreamableHttp] | None = None,
    ):
        self.agent = Agent(
            name=name,
            instructions=instructions,
            tools=tools or [],
            mcp_servers=mcp_servers or [],
            model=model,
        )
        self.history: list[dict[str, str]] = []

    async def run(self, input_text: str, context: dict | None = None):
        self.history.append({"role": "user", "content": input_text})
        items = [
            {"type": "message", "role": m["role"], "content": m["content"]}
            for m in self.history
        ]
        result = await Runner.run(self.agent, items, context=context or {})
        out = str(result.final_output)
        self.history.append({"role": "assistant", "content": out})
        return out
