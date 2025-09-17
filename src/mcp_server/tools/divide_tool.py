async def divide(input_data):
    """Divide the first number by the second."""
    if input_data.b == 0:
        return {
            "error": "Division by zero",
            "status": "failed"
        }
    return {
        "result": input_data.a / input_data.b,
        "status": "success"
    }