from math import pow

async def root(input_data):
    """Calculate the nth root of a number (开方)."""
    if input_data.number < 0 and input_data.degree % 2 == 0:
        raise ValueError("Cannot calculate even root of negative number")
    
    # Handle negative numbers with odd roots
    if input_data.number < 0 and input_data.degree % 2 == 1:
        return -pow(-input_data.number, 1 / input_data.degree)
    
    return pow(input_data.number, 1 / input_data.degree)