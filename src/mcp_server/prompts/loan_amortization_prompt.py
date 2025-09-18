def loan_amortization_prompt(principal: float, annual_rate: float, term_years: int, calculation_type: str = "monthly_payment") -> str:
    """Generate a prompt for loan amortization calculations with detailed MCP tool usage."""
    
    calc_type = calculation_type.lower()
    monthly_rate = annual_rate / 12 / 100  # Convert from percentage to monthly decimal
    total_months = term_years * 12
    
    if calc_type == "monthly_payment" or calc_type == "payment":
        return f"""## Loan Calculation Task: Monthly Payment Analysis

### 🎯 PRIMARY PURPOSE
Calculate the monthly payment for a loan of ${principal:,.2f} at {annual_rate}% annual interest rate over {term_years} years, using precise amortization formulas and MCP tools.

### 📊 MAIN GOALS
1. **Payment Calculation** - Determine exact monthly payment amount
2. **Total Cost Analysis** - Calculate lifetime cost of the loan
3. **Interest Breakdown** - Understand total interest paid over loan term
4. **Payment Verification** - Validate calculations using alternative methods

### 🔍 SUB-GOALS AND APPROACH

#### Goal 1: Monthly Payment Calculation
**Objective**: Calculate the fixed monthly payment using the standard loan formula
**Why**: This determines the borrower's monthly financial obligation

**Payment Formula**: PMT = P × [r(1+r)^n] / [(1+r)^n - 1]
Where: P = Principal, r = Monthly interest rate, n = Total payments

**Step 1.1**: Convert annual rate to monthly decimal rate
   - Purpose: Loans are typically paid monthly, requiring rate conversion
   - Calculate annual rate as decimal: divide({annual_rate}, 100) = {annual_rate/100}
   - Calculate monthly rate: divide(annual_decimal, 12) = {monthly_rate:.6f}
   - Expected outcome: Monthly interest rate in decimal form

**Step 1.2**: Calculate total number of payments
   - Purpose: Determine total payment periods for the loan
   - Calculate: multiply({term_years}, 12) = {total_months} payments
   - Significance: This is 'n' in the payment formula

**Step 1.3**: Calculate compound interest factor (1+r)^n
   - Purpose: This represents the total growth factor over the loan term
   - Method: add(1, {monthly_rate:.6f}) = {1 + monthly_rate:.6f}
   - Power calculation: power({1 + monthly_rate:.6f}, {total_months})
   - Expected outcome: Compound factor for {total_months} months
   - Financial meaning: How much $1 grows over the loan term

**Step 1.4**: Calculate numerator [r(1+r)^n]
   - Purpose: Top part of the payment formula
   - Multiply rate by compound factor: multiply({monthly_rate:.6f}, compound_factor)
   - Expected outcome: Numerator for payment calculation

**Step 1.5**: Calculate denominator [(1+r)^n - 1]
   - Purpose: Bottom part of the payment formula
   - Subtract 1 from compound factor: subtract(compound_factor, 1)
   - Expected outcome: Denominator for payment calculation
   - Financial meaning: Total interest growth over loan term

**Step 1.6**: Calculate payment ratio
   - Purpose: Get the payment multiplier per dollar borrowed
   - Divide numerator by denominator: divide(numerator, denominator)
   - Expected outcome: Payment factor per $1 of principal

**Step 1.7**: Calculate final monthly payment
   - Purpose: Determine actual payment amount
   - Multiply principal by payment factor: multiply({principal}, payment_factor)
   - Expected outcome: Fixed monthly payment amount
   - Practical significance: Amount due each month

#### Goal 2: Total Loan Cost Analysis
**Objective**: Calculate the total amount paid over the life of the loan
**Why**: Understanding the full financial commitment of borrowing

**Step 2.1**: Calculate total payments
   - Purpose: Find lifetime cost of the loan
   - Method: multiply(monthly_payment, {total_months})
   - Expected outcome: Total amount paid over {term_years} years
   - Context: This includes both principal and interest

**Step 2.2**: Calculate total interest paid
   - Purpose: Understand the cost of borrowing
   - Method: subtract(total_payments, {principal})
   - Expected outcome: Total interest over loan life
   - Financial impact: Extra cost beyond the borrowed amount

#### Goal 3: Interest vs Principal Breakdown
**Objective**: Understand how payments are allocated between interest and principal
**Why**: Early payments are mostly interest, later payments mostly principal

**Step 3.1**: First payment breakdown
   - Interest portion: multiply({principal}, {monthly_rate:.6f})
   - Principal portion: subtract(monthly_payment, interest_portion)
   - Remaining balance: subtract({principal}, principal_portion)
   - Pattern: Early payments have high interest, low principal

**Step 3.2**: Interest-to-principal ratio
   - Purpose: Show the cost efficiency of the loan
   - Calculate ratio: divide(total_interest, {principal})
   - Interpretation: How many times the principal you pay in interest
   - Example: Ratio of 0.5 means 50% extra cost in interest

#### Goal 4: Verification and Alternative Calculations
**Objective**: Validate results using different approaches
**Why**: Ensure accuracy and provide payment alternatives

**Step 4.1**: Payment verification through amortization
   - Method: Calculate if monthly payment exactly pays off loan in {total_months} months
   - Track remaining balance after each payment
   - Validation: Balance should be exactly $0 after final payment

**Step 4.2**: Interest rate check
   - Calculate effective annual rate: power(add(1, {monthly_rate:.6f}), 12)
   - Subtract 1 and multiply by 100 for percentage
   - Should equal {annual_rate}% annual rate

### 📊 Loan Summary
- **Principal**: ${principal:,.2f}
- **Annual Interest Rate**: {annual_rate}%
- **Loan Term**: {term_years} years ({total_months} payments)
- **Monthly Interest Rate**: {monthly_rate:.6f} ({monthly_rate*100:.4f}%)

### 💡 Financial Insights
- **Early Payment Impact**: Extra principal payments save substantial interest
- **Payment Timing**: Interest is highest in early years, principal in later years
- **Refinancing Consideration**: Lower rates may justify refinancing costs
- **Payment Schedule**: Fixed payments provide budget predictability

### 📐 Formula Reference
- Monthly Payment: PMT = P × [r(1+r)^n] / [(1+r)^n - 1]
- Total Interest: (PMT × n) - P
- Remaining Balance: P × [(1+r)^n - (1+r)^p] / [(1+r)^n - 1]
  (where p = payments made)

### ⚙️ Execution Instructions
Please use MCP tools (add, subtract, multiply, divide, power) for ALL calculations.
Follow the sequential steps, using each result for subsequent calculations.
Maintain precision to at least 6 decimal places for interest rate calculations."""

    elif calc_type == "total_interest" or calc_type == "interest":
        return f"""## Loan Analysis Task: Total Interest Calculation

### 🎯 PRIMARY PURPOSE
Determine the total interest cost for a loan of ${principal:,.2f} at {annual_rate}% annual rate over {term_years} years.

### 📊 MAIN GOALS
1. **Monthly Payment Derivation** - Calculate the monthly payment amount
2. **Interest Calculation** - Determine total interest over loan life
3. **Cost Analysis** - Understand the true cost of borrowing
4. **Comparison Framework** - Provide basis for comparing loan options

### 🔍 SUB-GOALS AND APPROACH

#### Goal 1: Payment Foundation
**Objective**: First calculate the monthly payment (needed for interest calculation)
**Why**: Interest calculation depends on the payment amount

**Step 1.1**: Use payment formula PMT = P × [r(1+r)^n] / [(1+r)^n - 1]
   - Monthly rate: divide({annual_rate}, 12) then divide by 100 = {monthly_rate:.6f}
   - Total payments: multiply({term_years}, 12) = {total_months}
   - Apply formula using MCP tools as detailed above

#### Goal 2: Total Interest Computation
**Objective**: Calculate the lifetime interest cost
**Why**: This is the real cost of borrowing money

**Step 2.1**: Calculate total amount paid
   - Method: multiply(monthly_payment, {total_months})
   - Purpose: Find total cash outflow over loan term

**Step 2.2**: Calculate interest portion
   - Method: subtract({principal}, total_payments)
   - Purpose: Isolate the cost of borrowing
   - Financial meaning: Extra amount paid beyond the loan principal

#### Goal 3: Interest Analysis
**Objective**: Understand the interest cost in context
**Why**: Helps evaluate if the loan terms are reasonable

**Step 3.1**: Interest as percentage of principal
   - Calculate: divide(total_interest, {principal})
   - Express as percentage: multiply(result, 100)
   - Interpretation: Additional cost as % of borrowed amount

**Step 3.2**: Average annual interest payment
   - Calculate: divide(total_interest, {term_years})
   - Purpose: Understand yearly interest burden
   - Context: Average interest cost per year

### ⚙️ Execution Instructions
Please use MCP tools for ALL calculations.
Calculate monthly payment first, then use it to determine total interest."""

    elif calc_type == "early_payoff" or calc_type == "prepayment":
        extra_payment = 100  # Default extra payment amount
        return f"""## Loan Strategy Task: Early Payoff Analysis

### 🎯 PRIMARY PURPOSE
Analyze the impact of extra payments on a ${principal:,.2f} loan at {annual_rate}% for {term_years} years.

### 📊 MAIN GOALS
1. **Baseline Calculation** - Standard loan without extra payments
2. **Prepayment Impact** - Effect of additional principal payments
3. **Interest Savings** - Calculate total interest reduction
4. **Time Savings** - Determine loan term reduction

### 🔍 SUB-GOALS AND APPROACH

#### Goal 1: Standard Loan Analysis
**Objective**: Calculate baseline loan metrics
**Why**: Need comparison point for prepayment benefits

**Step 1.1**: Calculate standard monthly payment
   - Use standard payment formula with MCP tools
   - Calculate total interest without extra payments

#### Goal 2: Prepayment Scenario
**Objective**: Model loan with extra principal payments
**Why**: Show financial benefits of paying more than required

**Step 2.1**: Enhanced payment calculation
   - Assume extra payment: ${extra_payment} per month toward principal
   - New effective payment: add(standard_payment, {extra_payment})
   - Purpose: Reduce principal faster, save interest

**Step 2.2**: Accelerated payoff timeline
   - Calculate months to payoff with extra payments
   - Method: Track remaining balance with enhanced payments
   - Expected outcome: Loan paid off in fewer months

#### Goal 3: Savings Quantification
**Objective**: Calculate financial benefits of prepayment
**Why**: Justify the extra monthly payment

**Step 3.1**: Interest savings calculation
   - Compare total interest: standard vs. prepayment scenario
   - Method: subtract(standard_interest, prepayment_interest)
   - Benefit: Money saved through extra payments

**Step 3.2**: Time savings
   - Calculate months saved: subtract(standard_months, prepayment_months)
   - Convert to years and months for clarity

### ⚙️ Execution Instructions
Model both scenarios using MCP tools.
Compare results to show prepayment benefits."""

    elif calc_type == "comparison" or calc_type == "equal_principal":
        return f"""## Loan Comparison Task: Payment Method Analysis

### 🎯 PRIMARY PURPOSE
Compare Equal Monthly Payment (EMP) vs Equal Principal Payment (EPP) methods for a ${principal:,.2f} loan.

### 📊 MAIN GOALS
1. **EMP Analysis** - Equal monthly payments (standard amortization)
2. **EPP Analysis** - Equal principal payments (declining interest)
3. **Cost Comparison** - Total interest comparison between methods
4. **Cash Flow Analysis** - Monthly payment patterns over time

### 🔍 SUB-GOALS AND APPROACH

#### Goal 1: Equal Monthly Payment Method
**Objective**: Calculate standard loan with fixed payments
**Why**: Most common loan structure - predictable payments

**Step 1.1**: Calculate fixed monthly payment
   - Use standard formula: PMT = P × [r(1+r)^n] / [(1+r)^n - 1]
   - Result: Same payment amount each month

**Step 1.2**: Total cost calculation
   - Method: multiply(monthly_payment, {total_months})
   - Purpose: Total cash outflow with EMP method

#### Goal 2: Equal Principal Payment Method
**Objective**: Calculate loan with fixed principal, declining interest
**Why**: Alternative method - higher initial payments, lower total interest

**Step 2.1**: Calculate fixed principal payment
   - Method: divide({principal}, {total_months})
   - Purpose: Equal principal reduction each month

**Step 2.2**: First month payment calculation
   - Interest: multiply({principal}, {monthly_rate:.6f})
   - Total payment: add(principal_payment, interest_payment)
   - Pattern: Payments decline each month as balance reduces

**Step 2.3**: Total interest with EPP
   - Formula: P × r × (n + 1) / 2
   - Method: Use MCP tools to calculate
   - Result: Lower total interest than EMP

#### Goal 3: Method Comparison
**Objective**: Compare the two payment methods
**Why**: Help borrowers choose the best option

**Step 3.1**: Interest difference
   - Calculate: subtract(EMP_total_interest, EPP_total_interest)
   - Purpose: Show EPP savings

**Step 3.2**: Cash flow analysis
   - EMP: Constant monthly payment
   - EPP: Declining monthly payment
   - Consideration: EPP requires higher initial payments

### ⚙️ Execution Instructions
Calculate both methods using MCP tools.
Compare total interest and payment patterns."""

    else:
        return f"""## Loan Calculation Guide: Multiple Analysis Options

### 🎯 PRIMARY PURPOSE
Provide comprehensive loan analysis for ${principal:,.2f} at {annual_rate}% over {term_years} years.

### 📊 AVAILABLE CALCULATION TYPES

#### 1. Monthly Payment Calculation ("monthly_payment" or "payment")
- Calculate fixed monthly payment amount
- Analyze total loan cost and interest breakdown
- Understand payment allocation over time

#### 2. Total Interest Analysis ("total_interest" or "interest")
- Focus on total interest cost over loan life
- Calculate interest as percentage of principal
- Provide yearly interest burden analysis

#### 3. Early Payoff Analysis ("early_payoff" or "prepayment")
- Model impact of extra principal payments
- Calculate interest and time savings
- Compare standard vs. accelerated payoff

#### 4. Payment Method Comparison ("comparison" or "equal_principal")
- Compare Equal Monthly Payment vs Equal Principal Payment
- Analyze total cost and cash flow differences
- Help choose optimal payment structure

### 🔍 GENERAL LOAN ANALYSIS APPROACH

#### Standard Loan Formula
PMT = P × [r(1+r)^n] / [(1+r)^n - 1]
Where:
- P = Principal amount (${principal:,.2f})
- r = Monthly interest rate ({annual_rate}% ÷ 12 ÷ 100 = {monthly_rate:.6f})
- n = Total payments ({term_years} × 12 = {total_months})

#### Key Calculations Using MCP Tools
1. **Rate conversion**: divide({annual_rate}, 12), then divide by 100
2. **Compound factor**: power(add(1, monthly_rate), {total_months})
3. **Payment calculation**: Use multiply, divide, add, subtract
4. **Interest analysis**: subtract(total_payments, principal)

### 💡 Loan Considerations
- **Interest front-loading**: Early payments are mostly interest
- **Principal acceleration**: Extra payments reduce total interest significantly
- **Rate sensitivity**: Small rate differences have large cost impacts
- **Term effects**: Longer terms mean lower payments but higher total interest

### ⚙️ Execution Instructions
Specify the calculation_type parameter:
- "monthly_payment" for payment calculation
- "total_interest" for interest analysis  
- "early_payoff" for prepayment benefits
- "comparison" for payment method comparison

Please use MCP tools (add, subtract, multiply, divide, power) for ALL calculations."""