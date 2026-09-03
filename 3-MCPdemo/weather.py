from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location:str)->str:
    """get weather location"""

    return "always raining in bangalroe"

if __name__ == "__main__":
    mcp.run(transport="streamable-http" )