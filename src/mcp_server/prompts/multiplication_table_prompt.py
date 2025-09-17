def build_multiplication_table(size: int = 10, start: int = 1) -> str:
    """Generate a prompt for creating multiplication tables."""
    return f"""Create a multiplication table with the following specifications:
- Size: {size}x{size}
- Starting from: {start}
- Format: Well-formatted table with row and column headers

Instructions:
1. Use the MCP tool multiply(a, b) to calculate each product
2. Generate the table showing products from {start} to {start + size - 1}
3. Each cell should contain the result of multiply(row_number, column_number)

Example for a 3x3 table starting at 1:
- Cell [1,1]: multiply(1, 1) = 1
- Cell [1,2]: multiply(1, 2) = 2
- Cell [2,3]: multiply(2, 3) = 6

Please calculate all products using the multiply tool and format them in a clean table."""
