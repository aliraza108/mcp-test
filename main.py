from mcp.server.fastmcp import FastMCP


mcp = FastMCP("DocumentMCP", stateless_http=True)

@mcp.tool()
async def main(city):
    return f"{city} is good"

mcp_app = mcp.streamable_http_app()