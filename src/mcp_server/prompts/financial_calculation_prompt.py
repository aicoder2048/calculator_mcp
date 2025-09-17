def financial_calculation_prompt(principal: float, rate: float, time: int) -> str:
    """Generate a prompt for compound interest calculation."""
    return f"""Calculate compound interest with:
- Principal: ${principal:,.2f}
- Annual rate: {rate}%
- Time period: {time} years

Please calculate:
1. Total amount after the period
2. Total interest earned
3. Monthly equivalent payment
4. Effective annual rate"""