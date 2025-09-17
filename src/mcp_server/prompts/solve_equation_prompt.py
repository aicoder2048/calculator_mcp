from typing import List
from fastmcp.prompts import PromptMessage
from mcp.types import TextContent

def solve_equation_conversation(equation: str) -> List[PromptMessage]:
    """Start a conversation to solve an equation step by step."""
    return [
        PromptMessage(role="user", content=TextContent(type="text", text=f"I need to solve this equation: {equation}")),
        PromptMessage(role="assistant", content=TextContent(type="text", text="I'll help you solve this equation step by step.")),
        PromptMessage(role="assistant", content=TextContent(type="text", text="First, let me identify the type of equation and the solving approach.")),
        PromptMessage(role="user", content=TextContent(type="text", text="Please show me each step clearly."))
    ]