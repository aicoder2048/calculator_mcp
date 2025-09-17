def list_all_assets() -> str:
    """Return a comprehensive list of all MCP server capabilities."""

    return """# 🚀 Calculator MCP Server Assets

## 🔧 Tools

### Basic Arithmetic Operations
1. **add(a: float, b: float) -> float**
   - Add two numbers together
   - Example: `add(5.5, 3.2)` → `8.7`

2. **subtract(a: float, b: float) -> float**
   - Subtract the second number from the first
   - Example: `subtract(10, 3)` → `7`

3. **multiply(a: float, b: float) -> float**
   - Multiply two numbers
   - Example: `multiply(4, 7)` → `28`

4. **divide(a: float, b: float) -> dict**
   - Divide the first number by the second
   - Returns quotient and remainder
   - Example: `divide(10, 3)` → `{"quotient": 3.33..., "remainder": 1}`

### Advanced Mathematical Operations
5. **power(base: float, exponent: float) -> float**
   - Calculate base raised to the power of exponent (乘方)
   - Example: `power(2, 8)` → `256`

6. **root(number: float, n: int = 2) -> float**
   - Calculate the nth root of a number (开方)
   - Default is square root (n=2)
   - Example: `root(16, 2)` → `4`

7. **mod(a: int, b: int) -> int**
   - Calculate remainder (余数) when a is divided by b
   - Example: `mod(10, 3)` → `1`

8. **factorial(n: int) -> int**
   - Calculate factorial of n with progress reporting
   - Supports n from 0 to 20
   - Example: `factorial(5)` → `120`

### Statistical Operations
9. **mean(numbers: List[float]) -> float**
   - Calculate the arithmetic mean of a dataset
   - Example: `mean([1, 2, 3, 4, 5])` → `3.0`

10. **median(numbers: List[float]) -> float**
    - Calculate the median of a dataset
    - Example: `median([1, 3, 5, 7, 9])` → `5.0`

11. **stddev(numbers: List[float]) -> float**
    - Calculate the standard deviation of a dataset
    - Example: `stddev([2, 4, 4, 4, 5, 5, 7, 9])` → `2.0`

## 📝 Prompts

1. **build_multiplication_table(size: int = 10, start: int = 1) -> str**
   - Generate a prompt for creating multiplication tables
   - Parameters:
     - `size`: Table dimensions (default: 10)
     - `start`: Starting number (default: 1)
   - Use case: Create formatted multiplication reference tables

2. **list_all_assets() -> str**
   - Generate a prompt to list all available tools and prompts
   - Returns this comprehensive documentation
   - Use case: Discover server capabilities

3. **solve_equation_conversation(equation: str) -> List**
   - Start a conversation to solve an equation step by step
   - Parameter: `equation` - The mathematical equation to solve
   - Use case: Interactive equation solving with detailed steps

4. **financial_calculation_prompt(principal: float, rate: float, time: int) -> str**
   - Generate a prompt for compound interest calculation
   - Parameters:
     - `principal`: Initial investment amount
     - `rate`: Annual interest rate (as decimal)
     - `time`: Investment period in years
   - Use case: Financial planning and investment calculations

## 💡 Usage Tips
- All arithmetic operations support floating-point numbers
- Division returns both quotient and remainder for completeness
- Statistical operations require at least one data point
- Factorial supports values from 0 to 20 for safety
- Financial calculations use compound interest formula
- Equation solver provides step-by-step explanations"""
