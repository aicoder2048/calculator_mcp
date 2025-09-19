def list_all_assets() -> str:
    """Return a comprehensive list of all MCP server capabilities."""

    return """# 🚀 Calculator MCP Server Assets

Display a list of all the assets available in the Calculator MCP Server.

Don't execute or run any of them.

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

### Statistical Operations - Basic
9. **mean(numbers: List[float]) -> float**
   - Calculate the arithmetic mean of a dataset
   - Example: `mean([1, 2, 3, 4, 5])` → `3.0`

10. **median(numbers: List[float]) -> float**
    - Calculate the median of a dataset
    - Example: `median([1, 3, 5, 7, 9])` → `5.0`

11. **stddev(numbers: List[float]) -> float**
    - Calculate the standard deviation of a dataset
    - Example: `stddev([2, 4, 4, 4, 5, 5, 7, 9])` → `2.0`

12. **min_value(numbers: List[float]) -> float**
    - Find the minimum value in a dataset
    - Example: `min_value([5, 2, 8, 1, 9])` → `1`

13. **max_value(numbers: List[float]) -> float**
    - Find the maximum value in a dataset
    - Example: `max_value([5, 2, 8, 1, 9])` → `9`

14. **sum(numbers: List[float]) -> float**
    - Calculate the sum of all values in a dataset
    - Example: `sum([1, 2, 3, 4, 5])` → `15`

15. **count(numbers: List[float]) -> int**
    - Count the number of values in a dataset
    - Example: `count([1, 2, 3, 4, 5])` → `5`

16. **range_stat(numbers: List[float]) -> float**
    - Calculate the range (max - min) of a dataset
    - Example: `range_stat([1, 5, 3, 9, 2])` → `8`

17. **variance(numbers: List[float]) -> float**
    - Calculate the variance of a dataset
    - Example: `variance([1, 2, 3, 4, 5])` → `2.5`

18. **mode(numbers: List[float]) -> Union[float, List[float]]**
    - Find the mode(s) of a dataset
    - Returns single value or list for multiple modes
    - Example: `mode([1, 2, 2, 3, 2])` → `2`

### Statistical Operations - Advanced
19. **percentile(numbers: List[float], p: float) -> float**
    - Calculate the pth percentile of a dataset
    - Parameter `p` must be between 0 and 100
    - Example: `percentile([1, 2, 3, 4, 5], 50)` → `3.0`

20. **quartiles(numbers: List[float]) -> dict**
    - Calculate the quartiles (Q1, Q2, Q3) of a dataset
    - Returns dictionary with Q1, Q2, Q3 values
    - Example: `quartiles([1, 2, 3, 4, 5, 6, 7, 8])` → `{"Q1": 2.25, "Q2": 4.5, "Q3": 6.75}`

21. **iqr(numbers: List[float]) -> float**
    - Calculate the interquartile range (Q3 - Q1)
    - Useful for identifying outliers
    - Example: `iqr([1, 2, 3, 4, 5, 6, 7, 8])` → `4.5`

22. **geometric_mean(numbers: List[float]) -> float**
    - Calculate the geometric mean of positive values
    - Useful for rates and ratios
    - Example: `geometric_mean([2, 4, 8])` → `4.0`

23. **harmonic_mean(numbers: List[float]) -> float**
    - Calculate the harmonic mean of positive values
    - Useful for averaging rates
    - Example: `harmonic_mean([1, 2, 4])` → `1.71`

## 📝 Prompts

1. **list_all_assets() -> str**
   - List all available assets including all the MCP server tools and prompts
   - Returns this comprehensive documentation
   - Use case: Discover server capabilities

2. **build_multiplication_table(size: int = 10, start: int = 1) -> str**
   - Generate a prompt for creating multiplication tables
   - Parameters:
     - `size`: Table dimensions (default: 10)
     - `start`: Starting number (default: 1)
   - Use case: Create formatted multiplication reference tables

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

5. **geometry_calculation(shape: str, dimension1: float, dimension2: float = None, dimension3: float = None) -> str**
   - Generate a prompt for geometric calculations with detailed MCP tool guidance
   - Parameters:
     - `shape`: Shape type (circle, triangle, rectangle, sphere)
     - `dimension1`: First dimension (radius, length, base)
     - `dimension2`: Second dimension (width, height, optional)
     - `dimension3`: Third dimension (triangle third side, optional)
   - Use case: Calculate area, perimeter, volume with step-by-step instructions

6. **unit_conversion(conversion_type: str, value: float, from_unit: str = None, to_unit: str = None) -> str**
   - Generate a prompt for unit conversions with detailed conversion steps
   - Parameters:
     - `conversion_type`: Type (temperature, length, weight, speed, volume)
     - `value`: Value to convert
     - `from_unit`: Source unit (optional for general guidance)
     - `to_unit`: Target unit (optional for general guidance)
   - Use case: Convert between metric/imperial units with formula explanations

7. **loan_amortization(principal: float, annual_rate: float, term_years: int, calculation_type: str = "monthly_payment") -> str**
   - Generate a prompt for loan amortization analysis with detailed financial calculations
   - Parameters:

     - `principal`: Loan amount
     - `annual_rate`: Annual interest rate (percentage)
     - `term_years`: Loan term in years
     - `calculation_type`: Analysis type (monthly_payment, total_interest, early_payoff, comparison)
   - Use case: Loan analysis, payment planning, financial decision making

8. **probability_calculation(calculation_type: str, n: int = None, r: int = None, probability: float = None, trials: int = None) -> str**
   - Generate a prompt for probability and combinatorics calculations with mathematical guidance
   - Parameters:
     - `calculation_type`: Calculation type (permutation, combination, binomial, expected_value, bayes)
     - `n`: Total number or trials (optional)
     - `r`: Selection number or successes (optional)
     - `probability`: Success probability for binomial (optional)
     - `trials`: Number of trials (optional)
   - Use case: Statistical analysis, probability theory, combinatorics problems

## 💡 Usage Tips
- All arithmetic operations support floating-point numbers
- Division returns both quotient and remainder for completeness
- Statistical operations require at least one data point
- Factorial supports values from 0 to 20 for safety
- Financial calculations use compound interest formula
- Equation solver provides step-by-step explanations
- Geometry prompts include detailed MCP tool usage instructions
- Unit conversion prompts provide formula explanations and validation steps
- Loan amortization supports multiple analysis types for comprehensive financial planning
- Probability calculations cover combinatorics, distributions, and Bayesian inference
- All enhanced prompts include purpose/goals explanation and sub-goals breakdown"""
