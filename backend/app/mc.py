import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.streamable_http_mcp import streamable_http_mcp_client


async def main() -> None:
    client = streamable_http_mcp_client()
    async with client as server:
        tools = await server.list_tools()
        for tool in tools:
            print(tool.name)
            print(tool.description)
            print("******************")


if __name__ == "__main__":
    asyncio.run(main())
