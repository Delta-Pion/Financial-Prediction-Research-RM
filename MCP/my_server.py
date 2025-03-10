from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MyServer")

@mcp.tool()
def greet(name: str) -> str:
    """Greets the person passed in the name parameter"""
    return f"Hello, {name}!"

@mcp.tool()
def add(x: int, y: int) -> int:
    """Adds two numbers together"""
    return x + y

if __name__ == "__main__":
    mcp.run()
