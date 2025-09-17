from math import pow

async def power(input_data):
    """Calculate base raised to the power of exponent (乘方)."""
    return pow(input_data.base, input_data.exponent)