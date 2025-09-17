async def factorial(input_data, ctx):
    """Calculate factorial of n with progress reporting."""
    result = 1
    for i in range(1, input_data.n + 1):
        result *= i
        if input_data.n > 10:  # Report progress for larger calculations
            await ctx.report_progress(i, input_data.n)

    return result