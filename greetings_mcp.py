# python -m pip install "mcp>=2,<3"
# Command: C:\Users\ditt_konto\anaconda3\python.exe
# Args: C:\utv_25_ai\greetings_mcp\greetings_mcp.py

import json
from urllib.request import urlopen
from mcp.server.mcpserver import MCPServer as _Server

mcp = _Server("greetings")

@mcp.tool()
def greet(name: str) -> str:
    """Say hello to a person."""
    return f"Hello, {name}!"

@mcp.tool()
def ask(name: str) -> str:
    """Ask a person what their plans are for today."""
    return f"Hello, {name}! What is your plan for today?"

# Prompt: Use the weather tool on the local Greetings MCP server to tell me the current temperature in Helsingborg.
@mcp.tool()
def weather() -> str:
    """Get the current temperature in Helsingborg, Sweden."""

    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=56.05&longitude=12.69"
        "&current=temperature_2m"
    )

    with urlopen(url, timeout=10) as response:
        data = json.load(response)

    temperature = data["current"]["temperature_2m"]

    return f"Current temperature in Helsingborg: {temperature} °C"

if __name__ == "__main__":
    mcp.run(transport="stdio")