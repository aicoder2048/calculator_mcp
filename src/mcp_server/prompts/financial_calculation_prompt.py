def financial_calculation_prompt(principal: float, rate: float, time: int) -> str:
    """Generate a prompt for compound interest calculation."""
    return f"""Calculate compound interest with:
- Principal: ${principal:,.2f}
- Annual rate: {rate}%
- Time period: {time} years

Instructions - Use MCP tools for all calculations:
1. Total amount after the period:
   - Convert rate to decimal: divide({rate}, 100)
   - Calculate (1 + rate): add(1, rate_decimal)
   - Calculate compound factor: power(1_plus_rate, {time})
   - Final amount: multiply({principal}, compound_factor)

2. Total interest earned:
   - Use subtract(final_amount, {principal})

3. Monthly equivalent payment (if investing monthly to reach final amount):
   - Monthly rate: divide(annual_rate, 12)
   - Total months: multiply(12, {time})
   - Use power() and multiply() tools for payment calculation

4. Effective annual rate (if compounded monthly):
   - Monthly rate: divide(annual_rate, 12)
   - Calculate: power(add(1, monthly_rate), 12)
   - Then: subtract(result, 1)
   - Finally: multiply(result, 100) for percentage

Formula reminder: A = P(1 + r)^t
Where: A = final amount, P = principal, r = rate (decimal), t = time

Please use the MCP tools (add, subtract, multiply, divide, power) for ALL calculations."""
