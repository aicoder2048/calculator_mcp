def build_multiplication_table(size: int = 10, start: int = 1) -> str:
    """Generate a prompt for creating multiplication tables."""
    return f"""Create a multiplication table with the following specifications:
- Size: {size}x{size}
- Starting from: {start}
- Format: Well-formatted table with row and column headers

Please generate the table showing products from {start} to {start + size - 1}."""