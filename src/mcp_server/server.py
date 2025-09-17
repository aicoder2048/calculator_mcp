from fastmcp import FastMCP, Context
from contextlib import asynccontextmanager
from typing import Dict, Any, AsyncIterator, List
import logging
import sys
import os

# Add parent directory to path for imports when run directly
if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import tool implementations
from mcp_server.tools import add_tool
from mcp_server.tools import subtract_tool
from mcp_server.tools import multiply_tool
from mcp_server.tools import divide_tool
from mcp_server.tools import power_tool
from mcp_server.tools import root_tool
from mcp_server.tools import mod_tool
from mcp_server.tools import factorial_tool
from mcp_server.tools import statistics_tool

# Import prompt implementations
from mcp_server.prompts import multiplication_table_prompt
from mcp_server.prompts import list_assets_prompt
from mcp_server.prompts import solve_equation_prompt
from mcp_server.prompts import financial_calculation_prompt

# Import models
from mcp_server.models.schemas import (
    AddInput,
    SubtractInput,
    MultiplyInput,
    DivideInput,
    PowerInput,
    RootInput,
    ModInput,
    FactorialInput,
    StatisticsInput
)

@asynccontextmanager
async def calculator_lifespan(server: FastMCP) -> AsyncIterator[Dict[str, Any]]:
    """Initialize calculator server with persistent state."""
    # Initialize calculation history
    history_store = []

    # Setup logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("calculator_mcp")

    yield {
        "history": history_store,
        "logger": logger
    }

# Create server instance
mcp = FastMCP(
    name="Calculator MCP Server",
    instructions="A comprehensive mathematical calculation server",
    version="1.0.0",
    lifespan=calculator_lifespan
)

# Register tools with decorators
@mcp.tool()
async def add(a: float, b: float) -> float:
    """Add two numbers together."""
    add_input = AddInput(a=a, b=b)
    return await add_tool.add(add_input)

@mcp.tool()
async def subtract(a: float, b: float) -> float:
    """Subtract the second number from the first."""
    subtract_input = SubtractInput(a=a, b=b)
    return await subtract_tool.subtract(subtract_input)

@mcp.tool()
async def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    multiply_input = MultiplyInput(a=a, b=b)
    return await multiply_tool.multiply(multiply_input)

@mcp.tool()
async def divide(a: float, b: float) -> dict:
    """Divide the first number by the second."""
    divide_input = DivideInput(a=a, b=b)
    return await divide_tool.divide(divide_input)

@mcp.tool()
async def power(base: float, exponent: float) -> float:
    """Calculate base raised to the power of exponent (乘方)."""
    power_input = PowerInput(base=base, exponent=exponent)
    return await power_tool.power(power_input)

@mcp.tool()
async def root(number: float, n: int = 2) -> float:
    """Calculate the nth root of a number (开方)."""
    root_input = RootInput(number=number, n=n)
    return await root_tool.root(root_input)

@mcp.tool()
async def mod(a: int, b: int) -> int:
    """Calculate remainder (余数) when a is divided by b."""
    mod_input = ModInput(a=a, b=b)
    return await mod_tool.mod(mod_input)

@mcp.tool()
async def factorial(n: int, ctx: Context) -> int:
    """Calculate factorial of n with progress reporting."""
    factorial_input = FactorialInput(n=n)
    return await factorial_tool.factorial(factorial_input, ctx)

@mcp.tool()
async def mean(numbers: List[float]) -> float:
    """Calculate the arithmetic mean of a dataset."""
    statistics_input = StatisticsInput(numbers=numbers)
    return await statistics_tool.mean(statistics_input)

@mcp.tool()
async def median(numbers: List[float]) -> float:
    """Calculate the median of a dataset."""
    statistics_input = StatisticsInput(numbers=numbers)
    return await statistics_tool.median(statistics_input)

@mcp.tool()
async def stddev(numbers: List[float]) -> float:
    """Calculate the standard deviation of a dataset."""
    statistics_input = StatisticsInput(numbers=numbers)
    return await statistics_tool.stddev(statistics_input)

# Register prompts with decorators
@mcp.prompt()
def build_multiplication_table(size: int = 10, start: int = 1) -> str:
    """Generate a prompt for creating multiplication tables."""
    return multiplication_table_prompt.build_multiplication_table(size, start)

@mcp.prompt()
def list_all_assets() -> str:
    """Generate a prompt to list all available tools and prompts."""
    return list_assets_prompt.list_all_assets()

@mcp.prompt()
def solve_equation_conversation(equation: str) -> List:
    """Start a conversation to solve an equation step by step."""
    return solve_equation_prompt.solve_equation_conversation(equation)

@mcp.prompt()
def financial_calculation(principal: float, rate: float, time: int) -> str:
    """Generate a prompt for compound interest calculation."""
    return financial_calculation_prompt.financial_calculation_prompt(principal, rate, time)

if __name__ == "__main__":
    mcp.run()
