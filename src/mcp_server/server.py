from fastmcp import FastMCP, Context
from contextlib import asynccontextmanager
from typing import Dict, Any, AsyncIterator, List, Union
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
from mcp_server.prompts import geometry_calculation_prompt
from mcp_server.prompts import unit_conversion_prompt
from mcp_server.prompts import loan_amortization_prompt
from mcp_server.prompts import probability_calculation_prompt
from mcp_server.prompts import fitness_analytics_prompt

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

@mcp.tool()
async def min_value(numbers: List[float]) -> float:
    """Find the minimum value in a dataset."""
    statistics_input = StatisticsInput(numbers=numbers)
    return await statistics_tool.min_value(statistics_input)

@mcp.tool()
async def max_value(numbers: List[float]) -> float:
    """Find the maximum value in a dataset."""
    statistics_input = StatisticsInput(numbers=numbers)
    return await statistics_tool.max_value(statistics_input)

@mcp.tool()
async def sum(numbers: List[float]) -> float:
    """Calculate the sum of all values in a dataset."""
    statistics_input = StatisticsInput(numbers=numbers)
    return await statistics_tool.sum_values(statistics_input)

@mcp.tool()
async def count(numbers: List[float]) -> int:
    """Count the number of values in a dataset."""
    statistics_input = StatisticsInput(numbers=numbers)
    return await statistics_tool.count_values(statistics_input)

@mcp.tool()
async def range_stat(numbers: List[float]) -> float:
    """Calculate the range (max - min) of a dataset."""
    statistics_input = StatisticsInput(numbers=numbers)
    return await statistics_tool.range_values(statistics_input)

@mcp.tool()
async def variance(numbers: List[float]) -> float:
    """Calculate the variance of a dataset."""
    statistics_input = StatisticsInput(numbers=numbers)
    return await statistics_tool.variance(statistics_input)

@mcp.tool()
async def mode(numbers: List[float]) -> Union[float, List[float]]:
    """Find the mode(s) of a dataset."""
    statistics_input = StatisticsInput(numbers=numbers)
    return await statistics_tool.mode(statistics_input)

@mcp.tool()
async def percentile(numbers: List[float], p: float) -> float:
    """Calculate the pth percentile of a dataset."""
    statistics_input = StatisticsInput(numbers=numbers)
    return await statistics_tool.percentile(statistics_input, p)

@mcp.tool()
async def quartiles(numbers: List[float]) -> dict:
    """Calculate the quartiles (Q1, Q2, Q3) of a dataset."""
    statistics_input = StatisticsInput(numbers=numbers)
    return await statistics_tool.quartiles(statistics_input)

@mcp.tool()
async def iqr(numbers: List[float]) -> float:
    """Calculate the interquartile range (Q3 - Q1) of a dataset."""
    statistics_input = StatisticsInput(numbers=numbers)
    return await statistics_tool.iqr(statistics_input)

@mcp.tool()
async def geometric_mean(numbers: List[float]) -> float:
    """Calculate the geometric mean of positive values."""
    statistics_input = StatisticsInput(numbers=numbers)
    return await statistics_tool.geometric_mean(statistics_input)

@mcp.tool()
async def harmonic_mean(numbers: List[float]) -> float:
    """Calculate the harmonic mean of positive values."""
    statistics_input = StatisticsInput(numbers=numbers)
    return await statistics_tool.harmonic_mean(statistics_input)

# Register prompts with decorators
@mcp.prompt()
def build_multiplication_table(size: int = 10, start: int = 1) -> str:
    """Generate a prompt for creating multiplication tables.
    
    Args:
        size: Table dimensions (default: 10)
        start: Starting number (default: 1)
    """
    return multiplication_table_prompt.build_multiplication_table(size, start)

@mcp.prompt()
def list_all_assets() -> str:
    """List all available assets including all the MCP server tools and prompts."""
    return list_assets_prompt.list_all_assets()

@mcp.prompt()
def solve_equation_conversation(equation: str) -> List:
    """Start a conversation to solve an equation step by step.
    
    Args:
        equation: The mathematical equation to solve
    """
    return solve_equation_prompt.solve_equation_conversation(equation)

@mcp.prompt()
def financial_calculation(principal: float, rate: float, time: int) -> str:
    """Generate a prompt for compound interest calculation.
    
    Args:
        principal: Initial investment amount
        rate: Annual interest rate (as decimal, e.g., 0.05 for 5%)
        time: Investment period in years
    """
    return financial_calculation_prompt.financial_calculation_prompt(principal, rate, time)

@mcp.prompt()
def geometry_calculation(shape: str, dimension1: float, dimension2: float = None, dimension3: float = None) -> str:
    """Generate a prompt for geometric calculations.
    
    Args:
        shape: Shape type (circle, triangle, rectangle, sphere)
        dimension1: First dimension (radius for circle/sphere, length for rectangle, base for triangle)
        dimension2: Second dimension (width for rectangle, height for triangle, optional)
        dimension3: Third dimension (third side for triangle, optional)
    """
    return geometry_calculation_prompt.geometry_calculation_prompt(shape, dimension1, dimension2, dimension3)

@mcp.prompt()
def unit_conversion(conversion_type: str, value: float, from_unit: str = None, to_unit: str = None) -> str:
    """Generate a prompt for unit conversions with detailed conversion steps.
    
    Args:
        conversion_type: Type (temperature, length, weight, speed, volume)
        value: Value to convert
        from_unit: Source unit (optional for general guidance)
        to_unit: Target unit (optional for general guidance)
    """
    return unit_conversion_prompt.unit_conversion_prompt(conversion_type, value, from_unit, to_unit)

@mcp.prompt()
def loan_amortization(principal: float, annual_rate: float, term_years: int, calculation_type: str = "monthly_payment") -> str:
    """Generate a prompt for loan amortization analysis with detailed financial calculations.
    
    Args:
        principal: Loan amount
        annual_rate: Annual interest rate (as percentage, e.g., 5.5 for 5.5%)
        term_years: Loan term in years
        calculation_type: Analysis type - options:
            - "monthly_payment": Calculate monthly payment amount
            - "total_interest": Calculate total interest paid
            - "early_payoff": Analyze early payoff scenarios
            - "comparison": Compare different loan terms
    """
    return loan_amortization_prompt.loan_amortization_prompt(principal, annual_rate, term_years, calculation_type)

@mcp.prompt()
def probability_calculation(calculation_type: str, n: int = None, r: int = None, probability: float = None, trials: int = None) -> str:
    """Generate a prompt for probability and combinatorics calculations with mathematical guidance.
    
    Args:
        calculation_type: Calculation type - options:
            - "permutation": Calculate P(n,r) where order matters
            - "combination": Calculate C(n,r) where order doesn't matter
            - "binomial": Binomial probability distribution
            - "expected_value": Calculate expected value E(X)
            - "bayes": Bayes' theorem for conditional probability
        n: Total number of items or trials (optional)
        r: Number of items selected or successes (optional)
        probability: Success probability for binomial (optional, 0-1)
        trials: Number of trials (optional)
    """
    return probability_calculation_prompt.probability_calculation_prompt(calculation_type, n, r, probability, trials)

@mcp.prompt()
def fitness_analytics(metric_type: str, time_period: str = "weekly", goal_type: str = "health_monitoring") -> str:
    """Generate a prompt for fitness and health analytics with detailed statistical analysis.
    
    Args:
        metric_type: Health metric to analyze - options:
            - "steps": Daily step count analysis
            - "calories": Calorie burn analysis
            - "heart_rate": Heart rate and cardiovascular analysis
            - "weight": Weight tracking and progress analysis
            - "blood_pressure": Blood pressure monitoring
        time_period: Analysis period (default: "weekly") - options:
            - "daily": Day-to-day analysis
            - "weekly": Week-over-week trends
            - "monthly": Monthly progress tracking
            - "quarterly": Long-term trend analysis
        goal_type: Fitness goal context (default: "health_monitoring") - options:
            - "weight_loss": Weight reduction goals
            - "fitness_improvement": Cardiovascular and strength goals
            - "health_monitoring": General health tracking
            - "athletic_training": Performance optimization
    """
    return fitness_analytics_prompt.fitness_analytics_prompt(metric_type, time_period, goal_type)

if __name__ == "__main__":
    mcp.run()
