  Design and implement a comprehensive Calculator MCP Server that allows LLM clients to perform mathematical operations through the MCP
  protocol. Use FastMCP 2.0, Python 3.10+, and uv for package management.

  Users should be able to:
  - Execute basic and advanced mathematical calculations (add, subtract, multiply, divide, power, root, modulo)
  - Calculate factorial with progress reporting for large numbers
  - Perform statistical analysis on datasets (mean, median, standard deviation)
  - Generate multiplication tables through prompts
  - Solve equations step-by-step with conversation prompts
  - Calculate compound interest and financial metrics
  - List all available tools and prompts with detailed documentation

  Technical architecture requirements:
  - FastMCP 2.0 as the server framework with decorator-based tool registration
  - Modular structure with separate files for each tool and prompt
  - Pydantic models for all input validation and data schemas
  - Async operations with progress reporting for long-running calculations
  - History tracking with persistent state management using lifespan context
  - Proper error handling with descriptive messages and validation
  - Integration tests and unit tests for all components (90%+ coverage)
  - Support for both individual operations and batch calculations
  - Type safety with mypy compliance
  - Claude Desktop and Claude Code compatibility

  Focus on clean code organization, testability, and production-ready quality with proper separation of concerns.
