from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a:int, b:int)->int:
    """_summary_
    Add two numbers
    """
    return a+b

@mcp.tool()
def multiply(a:int, b:int)->int:
    return a*b 

if __name__ == "__main__":
    mcp.run(transport="stdio")

# stdio works just like cpp standrd input output to receive and respond to tool function calls