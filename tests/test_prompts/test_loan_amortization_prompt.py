from src.mcp_server.prompts.loan_amortization_prompt import loan_amortization_prompt

def test_loan_monthly_payment_calculation():
    prompt = loan_amortization_prompt(250000.0, 4.5, 30, "monthly_payment")
    assert "Monthly Payment Analysis" in prompt
    assert "$250,000.00" in prompt
    assert "4.5%" in prompt
    assert "30 years" in prompt
    assert "PRIMARY PURPOSE" in prompt
    assert "Monthly Payment Calculation" in prompt
    assert "PMT = P × [r(1+r)^n] / [(1+r)^n - 1]" in prompt

def test_loan_payment_formula_steps():
    prompt = loan_amortization_prompt(100000.0, 5.0, 15, "payment")
    assert "Convert annual rate to monthly decimal rate" in prompt
    assert "divide(5.0, 100)" in prompt
    assert "divide(annual_decimal, 12)" in prompt
    assert "multiply(15, 12) = 180 payments" in prompt
    assert "power(" in prompt
    assert "compound interest factor" in prompt.lower()

def test_loan_total_cost_analysis():
    prompt = loan_amortization_prompt(200000.0, 3.75, 25, "monthly_payment")
    assert "Total Loan Cost Analysis" in prompt
    assert "multiply(monthly_payment, 300)" in prompt  # 25 * 12 = 300
    assert "subtract(total_payments, 200000.0)" in prompt
    assert "lifetime cost" in prompt.lower()

def test_loan_interest_breakdown():
    prompt = loan_amortization_prompt(300000.0, 4.0, 20, "payment")
    assert "Interest vs Principal Breakdown" in prompt
    assert "First payment breakdown" in prompt
    assert "Interest portion: multiply(300000.0" in prompt
    assert "Early payments have high interest" in prompt
    assert "Interest-to-principal ratio" in prompt

def test_loan_total_interest_calculation():
    prompt = loan_amortization_prompt(150000.0, 6.0, 30, "total_interest")
    assert "Total Interest Calculation" in prompt
    assert "$150,000.00" in prompt
    assert "6.0%" in prompt
    assert "Monthly Payment Derivation" in prompt
    assert "Interest Calculation" in prompt
    assert "subtract(150000.0, total_payments)" in prompt

def test_loan_early_payoff_analysis():
    prompt = loan_amortization_prompt(180000.0, 4.25, 25, "early_payoff")
    assert "Early Payoff Analysis" in prompt
    assert "extra payments" in prompt.lower()
    assert "Prepayment Impact" in prompt
    assert "Interest Savings" in prompt
    assert "Time Savings" in prompt
    assert "add(standard_payment, 100)" in prompt  # Default extra payment

def test_loan_prepayment_scenarios():
    prompt = loan_amortization_prompt(220000.0, 5.5, 30, "prepayment")
    assert "prepayment" in prompt.lower()
    assert "Enhanced payment calculation" in prompt
    assert "Accelerated payoff timeline" in prompt
    assert "Interest savings calculation" in prompt
    assert "fewer months" in prompt.lower()

def test_loan_comparison_analysis():
    prompt = loan_amortization_prompt(400000.0, 3.5, 30, "comparison")
    assert "Payment Method Analysis" in prompt
    assert "Equal Monthly Payment" in prompt
    assert "Equal Principal Payment" in prompt
    assert "EMP Analysis" in prompt
    assert "EPP Analysis" in prompt
    assert "fixed payments" in prompt.lower()
    assert "declining interest" in prompt.lower()

def test_loan_equal_principal_method():
    prompt = loan_amortization_prompt(300000.0, 4.75, 20, "equal_principal")
    assert "Equal Principal Payment Method" in prompt
    assert "divide(300000.0, 240)" in prompt  # 20 * 12 = 240
    assert "declining monthly payment" in prompt.lower()
    assert "Lower total interest than EMP" in prompt

def test_loan_general_guide():
    prompt = loan_amortization_prompt(500000.0, 4.0, 25, "unknown_type")
    assert "Multiple Analysis Options" in prompt
    assert "$500,000.00" in prompt
    assert "4.0%" in prompt
    assert "25 years" in prompt
    assert "Monthly Payment Calculation" in prompt
    assert "Total Interest Analysis" in prompt
    assert "Early Payoff Analysis" in prompt
    assert "Payment Method Comparison" in prompt

def test_loan_contains_financial_formulas():
    prompt = loan_amortization_prompt(175000.0, 3.25, 15)
    assert "PMT = P × [r(1+r)^n] / [(1+r)^n - 1]" in prompt
    assert "Monthly Interest Rate" in prompt
    assert "Compound factor" in prompt
    assert "Payment factor" in prompt

def test_loan_contains_mcp_instructions():
    prompt = loan_amortization_prompt(350000.0, 5.25, 30)
    assert "MCP tools" in prompt
    assert "add, subtract, multiply, divide, power" in prompt
    assert "Execution Instructions" in prompt
    assert "sequential steps" in prompt.lower()

def test_loan_contains_goals_structure():
    prompt = loan_amortization_prompt(120000.0, 6.5, 10)
    assert "🎯 PRIMARY PURPOSE" in prompt
    assert "📊 MAIN GOALS" in prompt
    assert "🔍 SUB-GOALS AND APPROACH" in prompt
    assert "**Objective**:" in prompt
    assert "**Why**:" in prompt
    assert "Goal 1:" in prompt

def test_loan_verification_steps():
    prompt = loan_amortization_prompt(275000.0, 4.125, 30)
    assert "Verification" in prompt
    assert "Payment Verification" in prompt
    assert "validate" in prompt.lower() or "verify" in prompt.lower()
    assert "Balance should be exactly $0" in prompt

def test_loan_financial_insights():
    prompt = loan_amortization_prompt(200000.0, 4.5, 30)
    assert "Financial Insights" in prompt
    assert "Early Payment Impact" in prompt
    assert "Payment Timing" in prompt
    assert "Refinancing Consideration" in prompt
    assert "budget predictability" in prompt.lower()

def test_loan_contains_practical_context():
    prompt = loan_amortization_prompt(180000.0, 5.0, 20)
    assert "Loan Summary" in prompt
    assert "Principal" in prompt
    assert "Annual Interest Rate" in prompt
    assert "Loan Term" in prompt
    assert "Monthly Interest Rate" in prompt

def test_loan_calculation_precision():
    prompt = loan_amortization_prompt(100000.0, 3.75, 30)
    # Check for precision requirements
    assert "6 decimal places" in prompt
    assert "precision" in prompt.lower()
    assert "maintain" in prompt.lower()

def test_loan_different_calculation_types():
    # Test all supported calculation types
    payment_prompt = loan_amortization_prompt(200000.0, 4.0, 30, "payment")
    assert "Monthly Payment Analysis" in payment_prompt
    
    interest_prompt = loan_amortization_prompt(200000.0, 4.0, 30, "interest")
    assert "Total Interest Calculation" in interest_prompt
    
    payoff_prompt = loan_amortization_prompt(200000.0, 4.0, 30, "early_payoff")
    assert "Early Payoff Analysis" in payoff_prompt
    
    comparison_prompt = loan_amortization_prompt(200000.0, 4.0, 30, "comparison")
    assert "Payment Method Analysis" in comparison_prompt

def test_loan_contains_rate_conversions():
    prompt = loan_amortization_prompt(150000.0, 6.0, 25)
    assert "Convert annual rate to monthly decimal rate" in prompt
    assert "Calculate monthly rate: divide(annual_decimal, 12)" in prompt
    assert "0.005000" in prompt  # 6% / 12 / 100 = 0.005