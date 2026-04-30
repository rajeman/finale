from agents.mcp.server import MCPServerStreamableHttp

STREAMABLE_HTTP_URL = "https://order-mcp-74afyau24q-uc.a.run.app/mcp"
MCP_HEADERS: dict[str, str] = {}

# Aliases for app/mc.py
CLOUDFLARE_MCP_URL = STREAMABLE_HTTP_URL
CLOUDFLARE_MCP_HEADERS = MCP_HEADERS


def streamable_http_mcp_client() -> MCPServerStreamableHttp:
    """New MCP client per chat session (safe for concurrent requests)."""
    return MCPServerStreamableHttp(
        name="Streamable HTTP Python Server",
        params={
            "url": STREAMABLE_HTTP_URL,
            "headers": MCP_HEADERS,
        },
        client_session_timeout_seconds=60.0,
    )
