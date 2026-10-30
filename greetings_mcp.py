# python -m pip install "mcp>=2,<3"
# Command: C:\Users\MagoS\anaconda3\python.exe
# Command: C:\Users\MagoS\miniconda3\python.exe
# Args: C:\Users\MagoS\Documents\GitHub\Lates Clone\agenthermes\greetings_mcp.py

import json
from urllib.request import urlopen
from mcp.server.mcpserver import MCPServer as _Server

# Crear servidor MCP
mcp = _Server("greetings")


@mcp.tool()
def greet(name: str) -> str:
    """Say hello to a person."""
    print(f"[MCP] greet() called with name={name}")
    return f"Hello, {name}!"


@mcp.tool()
def ask(name: str) -> str:
    """Ask a person what their plans are for today."""
    print(f"[MCP] ask() called with name={name}")
    return f"Hello, {name}! What is your plan for today?"


@mcp.tool()
def weather() -> str:
    """Get the current temperature in Helsingborg, Sweden."""

    print("[MCP] weather() called")

    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=56.05"
        "&longitude=12.69"
        "&current=temperature_2m"
    )

    with urlopen(url, timeout=10) as response:
        data = json.load(response)

    temperature = data["current"]["temperature_2m"]

    return f"Current temperature in Helsingborg: {temperature} °C"


if __name__ == "__main__":
    print("[MCP] Greetings MCP server started")
    mcp.run(transport="stdio")