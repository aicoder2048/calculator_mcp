from fastmcp import FastMCP, Context
from contextlib import asynccontextmanager
from typing import Dict, Any, AsyncIterator, List
import logging

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
async def add(input_data: AddInput) -> float:
    """Add two numbers together."""
    return await add_tool.add(input_data)

@mcp.tool()
async def subtract(input_data: SubtractInput) -> float:
    """Subtract the second number from the first."""
    return await subtract_tool.subtract(input_data)

@mcp.tool()
async def multiply(input_data: MultiplyInput) -> float:
    """Multiply two numbers."""
    return await multiply_tool.multiply(input_data)

@mcp.tool()
async def divide(input_data: DivideInput) -> dict:
    """Divide the first number by the second."""
    return await divide_tool.divide(input_data)

@mcp.tool()
async def power(input_data: PowerInput) -> float:
    """Calculate base raised to the power of exponent (乘方)."""
    return await power_tool.power(input_data)

@mcp.tool()
async def root(input_data: RootInput) -> float:
    """Calculate the nth root of a number (开方)."""
    return await root_tool.root(input_data)

@mcp.tool()
async def mod(input_data: ModInput) -> int:
    """Calculate remainder (余数) when a is divided by b."""
    return await mod_tool.mod(input_data)

@mcp.tool()
async def factorial(input_data: FactorialInput, ctx: Context) -> int:
    """Calculate factorial of n with progress reporting."""
    return await factorial_tool.factorial(input_data, ctx)

@mcp.tool()
async def mean(input_data: StatisticsInput) -> float:
    """Calculate the arithmetic mean of a dataset."""
    return await statistics_tool.mean(input_data)

@mcp.tool()
async def median(input_data: StatisticsInput) -> float:
    """Calculate the median of a dataset."""
    return await statistics_tool.median(input_data)

@mcp.tool()
async def stddev(input_data: StatisticsInput) -> float:
    """Calculate the standard deviation of a dataset."""
    return await statistics_tool.stddev(input_data)

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
def financial_calculation_prompt(principal: float, rate: float, time: int) -> str:
    """Generate a prompt for compound interest calculation."""
    return financial_calculation_prompt.financial_calculation_prompt(principal, rate, time)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(mcp, host="0.0.0.0", port=8000)