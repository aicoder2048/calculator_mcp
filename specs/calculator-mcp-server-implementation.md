# Calculator MCP Server Implementation Plan

## 1. Project Overview

### Objective
Create a fully-featured Calculator MCP Server using FastMCP that provides mathematical operations as tools and includes reusable prompts for common mathematical tasks.

### Key Technologies
- **FastMCP 2.0**: Primary framework for building the MCP server
- **Python 3.10+**: Development language
- **uv**: Package management and dependency isolation
- **pytest**: Testing framework
- **Pydantic**: Input validation and data modeling

### Core Features
1. **Mathematical Tools**: Basic and advanced mathematical operations
2. **MCP Resources**: Access to calculation history and constants
3. **MCP Prompts**: Pre-configured prompts for common calculation patterns
4. **Error Handling**: Robust validation and error messaging
5. **Test Suite**: Comprehensive unit and integration tests

## 2. Project Architecture

### Directory Structure
```
calculator_mcp/
├── src/
│   ├── __init__.py
│   ├── server.py           # Main FastMCP server instance
│   ├── tools/              # Tool implementations
│   │   ├── __init__.py
│   │   ├── basic_ops.py    # Addition, subtraction, multiplication, division
│   │   ├── advanced_ops.py # Power, root, mod operations
│   │   └── statistics.py   # Mean, median, standard deviation
│   ├── resources/          # Resource handlers
│   │   ├── __init__.py
│   │   ├── history.py      # Calculation history tracking
│   │   └── constants.py    # Mathematical constants
│   ├── prompts/            # Prompt templates
│   │   ├── __init__.py
│   │   ├── table_prompts.py   # Multiplication tables, etc.
│   │   └── solver_prompts.py  # Equation solving prompts
│   ├── models/             # Data models
│   │   ├── __init__.py
│   │   └── schemas.py      # Pydantic models for validation
│   └── config/            # Configuration
│       ├── __init__.py
│       └── settings.py     # Server configuration
├── tests/
│   ├── __init__.py
│   ├── test_tools.py
│   ├── test_resources.py
│   ├── test_prompts.py
│   └── test_integration.py
├── pyproject.toml
├── uv.lock
├── fastmcp.json               # MCP server configuration
├── README.md
└── .github/
    └── workflows/
        └── ci.yml             # CI/CD pipeline

```

## 3. Implementation Details

### 3.1 Core Server Implementation

```python
# server.py
from fastmcp import FastMCP, Context
from contextlib import asynccontextmanager
from typing import Dict, Any, AsyncIterator
import logging

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
    version="1.0.0",
    description="A comprehensive mathematical calculation server",
    lifespan=calculator_lifespan
)
```

### 3.2 Tool Implementations

#### Basic Operations
```python
# tools/basic_ops.py
from pydantic import BaseModel, Field
from typing import List, Optional

class CalculationInput(BaseModel):
    a: float = Field(..., description="First operand")
    b: float = Field(..., description="Second operand")

class BatchCalculationInput(BaseModel):
    numbers: List[float] = Field(..., min_items=2, description="List of numbers to operate on")
    operation: str = Field(..., pattern="^(sum|product)$", description="Batch operation type")

@mcp.tool()
def add(input: CalculationInput) -> float:
    """Add two numbers together."""
    result = input.a + input.b
    # Store in history
    return result

@mcp.tool()
def subtract(input: CalculationInput) -> float:
    """Subtract the second number from the first."""
    return input.a - input.b

@mcp.tool()
def multiply(input: CalculationInput) -> float:
    """Multiply two numbers."""
    return input.a * input.b

@mcp.tool()
def divide(input: CalculationInput) -> dict:
    """Divide the first number by the second."""
    if input.b == 0:
        return {
            "error": "Division by zero",
            "status": "failed"
        }
    return {
        "result": input.a / input.b,
        "status": "success"
    }
```

#### Advanced Operations
```python
# tools/advanced_ops.py
from math import sqrt, pow
from pydantic import BaseModel, Field, validator

class PowerInput(BaseModel):
    base: float = Field(..., description="Base number")
    exponent: float = Field(..., description="Power to raise to")

class RootInput(BaseModel):
    number: float = Field(..., ge=0, description="Number to find root of")
    degree: float = Field(2.0, gt=0, description="Degree of root (default: 2 for square root)")

@mcp.tool()
def mod(a: int, b: int) -> int:
    """Calculate remainder (余数) when a is divided by b."""
    if b == 0:
        raise ValueError("Cannot calculate modulo with divisor of zero")
    return a % b

@mcp.tool()
def power(input: PowerInput) -> float:
    """Calculate base raised to the power of exponent (乘方)."""
    return pow(input.base, input.exponent)

@mcp.tool()
def root(input: RootInput) -> float:
    """Calculate the nth root of a number (开方)."""
    if input.number < 0 and input.degree % 2 == 0:
        raise ValueError("Cannot calculate even root of negative number")
    return pow(input.number, 1 / input.degree)

@mcp.tool()
async def factorial(n: int, ctx: Context) -> int:
    """Calculate factorial of n with progress reporting."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n > 20:
        raise ValueError("Factorial too large, maximum supported value is 20")

    result = 1
    for i in range(1, n + 1):
        result *= i
        if n > 10:  # Report progress for larger calculations
            await ctx.report_progress(i, n)

    return result
```

### 3.3 Resource Implementations

```python
# resources/history.py
from typing import List, Dict

@mcp.resource("history://recent")
def get_recent_calculations() -> List[Dict]:
    """Get the last 10 calculations performed."""
    return history_store[-10:]  # Access from lifespan context

@mcp.resource("history://{operation}/last")
def get_last_operation(operation: str) -> Dict:
    """Get the last calculation of a specific operation type."""
    for calc in reversed(history_store):
        if calc["operation"] == operation:
            return calc
    return {"message": f"No {operation} calculations found"}

# resources/constants.py
import math

@mcp.resource("constants://mathematical")
def get_math_constants() -> Dict[str, float]:
    """Get common mathematical constants."""
    return {
        "pi": math.pi,
        "e": math.e,
        "tau": math.tau,
        "golden_ratio": (1 + math.sqrt(5)) / 2,
        "euler_mascheroni": 0.5772156649015329
    }

@mcp.resource("constants://conversion-factors")
def get_conversion_factors() -> Dict[str, Dict[str, float]]:
    """Get common unit conversion factors."""
    return {
        "length": {
            "meter_to_feet": 3.28084,
            "mile_to_km": 1.60934,
            "inch_to_cm": 2.54
        },
        "weight": {
            "kg_to_pounds": 2.20462,
            "ounce_to_grams": 28.3495
        },
        "temperature": {
            "celsius_to_fahrenheit_offset": 32,
            "celsius_to_fahrenheit_factor": 1.8
        }
    }
```

### 3.4 Prompt Implementations

```python
# prompts/table_prompts.py
from fastmcp.prompts import prompt

@mcp.prompt()
def build_multiplication_table(size: int = 10, start: int = 1) -> str:
    """Generate a prompt for creating multiplication tables."""
    return f"""Create a multiplication table with the following specifications:
- Size: {size}x{size}
- Starting from: {start}
- Format: Well-formatted table with row and column headers

Please generate the table showing products from {start} to {start + size - 1}."""

@mcp.prompt()
def list_all_assets() -> str:
    """Generate a prompt to list all available tools and prompts with detailed information."""
    return """Please provide a comprehensive list of all available assets in this MCP server:

## Tools
List all available tools with:
- Tool name (function call name)
- Full function signature with parameter types
- Brief description of what the tool does
- Parameter details (name, type, description, constraints)
- Return type and format
- Example usage

## Prompts
List all available prompts with:
- Prompt name (function call name)
- Function signature with parameters
- Description of the prompt's purpose
- Parameters required
- Expected output format
- Example usage

Please organize the information in a clear, structured format."""

# prompts/solver_prompts.py
from typing import List
from fastmcp.prompts.base import Message, UserMessage, AssistantMessage

@mcp.prompt()
def solve_equation_conversation(equation: str) -> List[Message]:
    """Start a conversation to solve an equation step by step."""
    return [
        UserMessage(f"I need to solve this equation: {equation}"),
        AssistantMessage("I'll help you solve this equation step by step."),
        AssistantMessage("First, let me identify the type of equation and the solving approach."),
        UserMessage("Please show me each step clearly.")
    ]

@mcp.prompt()
def financial_calculation_prompt(principal: float, rate: float, time: int) -> str:
    """Generate a prompt for compound interest calculation."""
    return f"""Calculate compound interest with:
- Principal: ${principal:,.2f}
- Annual rate: {rate}%
- Time period: {time} years

Please calculate:
1. Total amount after the period
2. Total interest earned
3. Monthly equivalent payment
4. Effective annual rate"""
```

### 3.5 Data Models and Validation

```python
# models/schemas.py
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Literal
from datetime import datetime

class CalculationRecord(BaseModel):
    """Model for storing calculation history."""
    id: str
    operation: str
    inputs: dict
    result: float
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    error: Optional[str] = None

class StatisticsInput(BaseModel):
    """Model for statistical calculations."""
    data: List[float] = Field(..., min_items=1, description="Data points")
    operation: Literal["mean", "median", "stddev", "variance", "mode"]

    @validator("data")
    def validate_data(cls, v):
        if not v:
            raise ValueError("Data list cannot be empty")
        return v

class EquationInput(BaseModel):
    """Model for equation solving."""
    equation_type: Literal["linear", "quadratic", "polynomial"]
    coefficients: List[float] = Field(..., description="Equation coefficients")

    @validator("coefficients")
    def validate_coefficients(cls, v, values):
        equation_type = values.get("equation_type")
        if equation_type == "linear" and len(v) != 2:
            raise ValueError("Linear equation requires exactly 2 coefficients")
        elif equation_type == "quadratic" and len(v) != 3:
            raise ValueError("Quadratic equation requires exactly 3 coefficients")
        return v
```

## 4. Testing Strategy

### 4.1 Unit Tests

```python
# tests/test_tools.py
import pytest
from fastmcp import Client
from src.server import mcp

@pytest.fixture
def calculator_client():
    return Client(mcp)

@pytest.mark.asyncio
async def test_basic_addition(calculator_client):
    async with calculator_client as client:
        result = await client.call_tool("add", {"a": 5, "b": 3})
        assert result == 8

@pytest.mark.asyncio
async def test_division_by_zero(calculator_client):
    async with calculator_client as client:
        result = await client.call_tool("divide", {"a": 10, "b": 0})
        assert result["status"] == "failed"
        assert "Division by zero" in result["error"]

@pytest.mark.parametrize("base,exponent,expected", [
    (2, 3, 8),
    (5, 0, 1),
    (10, -1, 0.1),
    (4, 0.5, 2),
])
@pytest.mark.asyncio
async def test_power_operations(calculator_client, base, exponent, expected):
    async with calculator_client as client:
        result = await client.call_tool("power", {"base": base, "exponent": exponent})
        assert result == pytest.approx(expected)
```

### 4.2 Integration Tests

```python
# tests/test_integration.py
import pytest
from fastmcp import Client

@pytest.mark.asyncio
async def test_calculation_workflow():
    """Test a complete calculation workflow with history."""
    async with Client(mcp) as client:
        # Perform several calculations
        await client.call_tool("add", {"a": 10, "b": 20})
        await client.call_tool("multiply", {"a": 5, "b": 6})
        await client.call_tool("power", {"base": 2, "exponent": 10})

        # Check history
        history = await client.read_resource("history://recent")
        assert len(history) >= 3

        # Verify last multiplication
        last_multiply = await client.read_resource("history://multiply/last")
        assert last_multiply["result"] == 30

@pytest.mark.asyncio
async def test_prompt_generation():
    """Test prompt template generation."""
    async with Client(mcp) as client:
        # Get multiplication table prompt
        table_prompt = await client.get_prompt("build_multiplication_table", {"size": 5})
        assert "5x5" in table_prompt

        # Get equation solving conversation
        equation_conv = await client.get_prompt(
            "solve_equation_conversation",
            {"equation": "2x + 5 = 15"}
        )
        assert len(equation_conv) == 4
        assert "2x + 5 = 15" in equation_conv[0].content
```

## 5. Configuration and Deployment

### 5.1 FastMCP Configuration

```json
{
  "name": "calculator-mcp",
  "version": "1.0.0",
  "description": "Mathematical calculation MCP server",
  "main": "src/server.py",
  "dependencies": [
    "fastmcp>=2.0.0",
    "pydantic>=2.0.0",
    "numpy>=1.24.0"
  ],
  "environment": {
    "LOG_LEVEL": "INFO",
    "MAX_HISTORY_SIZE": "1000"
  }
}
```

### 5.2 PyProject Configuration

```toml
[project]
name = "calculator-mcp"
version = "1.0.0"
description = "A comprehensive mathematical calculation MCP server"
requires-python = ">=3.10"
dependencies = [
    "fastmcp[cli]>=2.0.0",
    "pydantic>=2.0.0",
    "numpy>=1.24.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0.0",
    "pytest-asyncio>=0.23.0",
    "pytest-cov>=5.0.0",
    "ruff>=0.4.0",
    "mypy>=1.10.0"
]

[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[tool.pytest.ini_options]
testpaths = ["tests"]
asyncio_mode = "auto"

[tool.ruff]
line-length = 88
target-version = "py310"
```

### 5.3 MCP Client Configuration

```json
{
  "mcpServers": {
    "calculator": {
      "command": "uv",
      "args": ["run", "python", "/path/to/calculator_mcp/src/server.py"],
      "env": {
        "LOG_LEVEL": "INFO"
      }
    }
  }
}
```

## 6. Development Workflow

### 6.1 Initial Setup
```bash
# Initialize project with uv
uv init calculator_mcp
cd calculator_mcp

# Add dependencies
uv add "fastmcp[cli]>=2.0.0"
uv add pydantic numpy

# Add dev dependencies
uv add --dev pytest pytest-asyncio pytest-cov ruff mypy
```

### 6.2 Development Commands
```bash
# Run server in development mode
uv run python src/server.py

# Run with FastMCP inspector
npx @modelcontextprotocol/inspector uv run python src/server.py

# Run tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=src --cov-report=html

# Format and lint
uv run ruff check --fix src/ tests/
uv run mypy src/
```

### 6.3 Installation in Claude Code/Desktop
```bash
# Generate MCP configuration
fastmcp install src/server.py

# Or manually configure
fastmcp install --claude-code src/server.py
```

## 7. Error Handling and Validation

### Key Validation Points
1. **Input Validation**: All tools use Pydantic models for automatic validation
2. **Mathematical Domain Errors**: Check for division by zero, negative roots, etc.
3. **Range Limits**: Factorial limited to n≤20, array operations check for empty lists
4. **Type Safety**: Strong typing throughout with mypy verification

### Error Response Format
```python
{
    "status": "error",
    "error_type": "validation_error" | "domain_error" | "runtime_error",
    "message": "Human-readable error description",
    "details": {
        "field": "specific field with error",
        "value": "problematic value",
        "constraint": "violated constraint"
    }
}
```

## 8. Performance Considerations

### Optimization Strategies
1. **Async Operations**: Use async for I/O-bound operations and progress reporting
2. **History Management**: Implement circular buffer for history (max 1000 entries)
3. **Caching**: Cache mathematical constants and conversion factors
4. **Batch Operations**: Support batch calculations for efficiency

### Resource Limits
- Maximum array size for statistical operations: 10,000 elements
- Maximum factorial input: 20
- History retention: 1000 most recent calculations
- Progress reporting threshold: Operations taking >0.5 seconds

## 9. Security Considerations

### Input Sanitization
- All inputs validated through Pydantic models
- String inputs restricted to expected patterns
- Numeric inputs bounded to prevent overflow

### Resource Protection
- Rate limiting for expensive operations
- Memory limits for array operations
- Timeout for long-running calculations

## 10. Success Criteria

### Functional Requirements
- ✅ All basic arithmetic operations working correctly
- ✅ Advanced operations (power, root, mod) implemented
- ✅ Statistical functions available
- ✅ Calculation history tracking
- ✅ Mathematical constants exposed as resources
- ✅ Prompt templates for common tasks

### Non-Functional Requirements
- ✅ Response time <100ms for basic operations
- ✅ Test coverage >90%
- ✅ Type safety with mypy passing
- ✅ Documentation for all public APIs
- ✅ Compatible with Claude Code and Claude Desktop

### Deliverables
1. Complete source code with proper structure
2. Comprehensive test suite
3. FastMCP configuration file
4. Installation instructions
5. API documentation
6. Example usage scenarios

## 11. Implementation Timeline

### Phase 1: Core Setup (Day 1)
- Project initialization
- Basic FastMCP server setup
- Directory structure creation
- Development environment configuration

### Phase 2: Tool Implementation (Day 2-3)
- Basic arithmetic operations
- Advanced mathematical operations
- Statistical functions
- Input validation models

### Phase 3: Resources & Prompts (Day 4)
- History tracking implementation
- Mathematical constants resource
- Prompt templates
- Integration with server lifecycle

### Phase 4: Testing & Documentation (Day 5)
- Unit test suite
- Integration tests
- API documentation
- Installation guide

### Phase 5: Deployment & Optimization (Day 6)
- Performance optimization
- Error handling refinement
- Claude Code/Desktop configuration
- Final testing and deployment

## 12. Future Enhancements

### Potential Extensions
1. **Graphing Capabilities**: Generate visual representations of functions
2. **Symbolic Mathematics**: Support for algebraic manipulation
3. **Matrix Operations**: Linear algebra tools
4. **Scientific Functions**: Trigonometry, logarithms, etc.
5. **Unit Conversion Tools**: Comprehensive unit conversion system
6. **Formula Storage**: Save and recall custom formulas
7. **Calculation Scripting**: Support for calculation sequences
8. **Export Capabilities**: Export history to CSV/JSON

This comprehensive plan provides a solid foundation for implementing a production-ready Calculator MCP Server with extensive functionality, proper testing, and seamless integration with MCP clients.
