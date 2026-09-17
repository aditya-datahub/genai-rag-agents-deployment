"""
Minimal MCP server exposing a couple of tools, built with the official
`mcp` Python SDK.

Install:
    pip install mcp

Run:
    python mcp_server_example.py

Any MCP-compatible client (an MCP Inspector, a PydanticAI agent, a CrewAI
agent, etc.) can then connect to this server over stdio and call its tools.
"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("demo-tools-server")


@mcp.tool()
def get_word_count(text: str) -> int:
    """Return the number of words in the given text."""
    return len(text.split())


@mcp.tool()
def reverse_text(text: str) -> str:
    """Return the given text reversed."""
    return text[::-1]


if __name__ == "__main__":
    mcp.run(transport="stdio")
