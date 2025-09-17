from typing import List
from fastmcp.prompts import PromptMessage
from mcp.types import TextContent

def solve_equation_conversation(equation: str) -> List[PromptMessage]:
    """Start a conversation to solve an equation step by step."""
    return [
        PromptMessage(role="user", content=TextContent(type="text", text=f"I need to solve this equation: {equation}")),
        PromptMessage(role="assistant", content=TextContent(type="text", text="I'll help you solve this equation step by step using MCP calculation tools.")),
        PromptMessage(role="assistant", content=TextContent(type="text", text="""Let me solve this using the available MCP tools:

Available tools for equation solving:
- add(a, b) - Addition
- subtract(a, b) - Subtraction
- multiply(a, b) - Multiplication
- divide(a, b) - Division
- power(base, exponent) - Exponentiation
- root(number, n) - Nth root calculation

I'll identify the equation type and solve it step-by-step, using these tools for ALL calculations.""")),
        PromptMessage(role="user", content=TextContent(type="text", text="""Please show me each step clearly with MCP tool calls. For example:
- For linear equation 2x + 3 = 7:
  Step 1: subtract(7, 3) = 4
  Step 2: divide(4, 2) = 2
  Therefore x = 2

- For quadratic x² - 5x + 6 = 0:
  Step 1: Calculate discriminant using power() and multiply()
  Step 2: Use root() for square root
  Step 3: Use add() and subtract() for solutions

Show all calculations using the MCP tools."""))
    ]
