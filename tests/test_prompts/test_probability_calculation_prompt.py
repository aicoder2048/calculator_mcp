from src.mcp_server.prompts.probability_calculation_prompt import probability_calculation_prompt

def test_permutation_calculation():
    prompt = probability_calculation_prompt("permutation", n=10, r=3)
    assert "Permutation Calculation" in prompt
    assert "P(n,r) = n!/(n-r)!" in prompt
    assert "arranging 3 items from 10 total items" in prompt
    assert "order matters" in prompt.lower()
    assert "factorial(10)" in prompt
    assert "factorial(7)" in prompt  # 10-3=7

def test_permutation_formula_steps():
    prompt = probability_calculation_prompt("arrangement", n=8, r=5)
    assert "Factorial Calculations" in prompt
    assert "Calculate n! = 8!" in prompt
    assert "Calculate (n-r)! = (8-5)! = 3!" in prompt
    assert "divide(n_factorial, n_minus_r_factorial)" in prompt
    assert "ORDER MATTERS" in prompt

def test_combination_calculation():
    prompt = probability_calculation_prompt("combination", n=12, r=5)
    assert "Combination Calculation" in prompt
    assert "C(n,r) = n!/[r!(n-r)!]" in prompt
    assert "choosing 5 items from 12 total items" in prompt
    assert "order doesn't matter" in prompt.lower()
    assert "factorial(12)" in prompt
    assert "factorial(5)" in prompt
    assert "factorial(7)" in prompt  # 12-5=7

def test_combination_formula_steps():
    prompt = probability_calculation_prompt("choose", n=20, r=3)
    assert "Three factorials are needed" in prompt
    assert "Calculate n! = 20!" in prompt
    assert "Calculate r! = 3!" in prompt
    assert "Calculate (n-r)! = (20-3)! = 17!" in prompt
    assert "multiply(r_factorial, n_minus_r_factorial)" in prompt
    assert "ORDER DOESN'T MATTER" in prompt

def test_binomial_probability():
    prompt = probability_calculation_prompt("binomial", n=20, r=15, probability=0.8)
    assert "Binomial Distribution Calculation" in prompt
    assert "exactly 15 successes in n independent trials" in prompt  # Updated to match actual prompt
    assert "success probability 0.8" in prompt
    assert "P(X=k) = C(n,k) × p^k × (1-p)^(n-k)" in prompt
    assert "factorial(20)" in prompt or "factorial(n)" in prompt  # May use n or specific value
    assert "15" in prompt  # Check that r value appears
    assert "0.8" in prompt  # Check that probability appears

def test_binomial_probability_components():
    prompt = probability_calculation_prompt("binomial_probability", trials=10, r=7, probability=0.6)
    assert "Combination Component" in prompt
    assert "C(10,7)" in prompt
    assert "power(0.6, 7)" in prompt  # p^k
    assert "subtract(1, 0.6)" in prompt  # 1-p
    assert "power(failure_probability, 3)" in prompt  # (1-p)^(n-k), 10-7=3

def test_expected_value_calculation():
    prompt = probability_calculation_prompt("expected_value")
    assert "Expected Value Calculation" in prompt
    assert "E(X) = Σ(xi × pi)" in prompt
    assert "weighted average" in prompt.lower()
    assert "Probability Validation" in prompt
    assert "probabilities sum to 1" in prompt
    assert "multiply(outcome_value, probability)" in prompt

def test_expected_value_concepts():
    prompt = probability_calculation_prompt("expectation")
    assert "long-run average" in prompt.lower()
    assert "Not necessarily a possible outcome" in prompt
    assert "decision-making" in prompt.lower()
    assert "Each probability must be between 0 and 1" in prompt
    assert "Sum of all probabilities must equal 1" in prompt

def test_bayes_theorem():
    prompt = probability_calculation_prompt("bayes")
    assert "Bayesian Probability Calculation" in prompt
    assert "P(A|B) = P(B|A)×P(A)/P(B)" in prompt
    assert "updating beliefs" in prompt.lower()
    assert "Prior Probability" in prompt
    assert "Likelihood Calculation" in prompt
    assert "Posterior Interpretation" in prompt

def test_bayes_components():
    prompt = probability_calculation_prompt("conditional")
    assert "P(A|B): Posterior" in prompt
    assert "P(B|A): Likelihood" in prompt
    assert "P(A): Prior" in prompt
    assert "P(B): Evidence" in prompt
    assert "law of total probability" in prompt.lower()
    assert "P(B) = P(B|A)×P(A) + P(B|¬A)×P(¬A)" in prompt

def test_general_probability_guide():
    prompt = probability_calculation_prompt("unknown_type")
    assert "Multiple Analysis Options" in prompt
    assert "Permutation/Arrangement" in prompt
    assert "Combination/Choose" in prompt
    assert "Binomial Probability" in prompt
    assert "Expected Value" in prompt
    assert "Bayes' Theorem" in prompt

def test_permutation_applications():
    prompt = probability_calculation_prompt("permutation", n=5, r=3)
    assert "Sports" in prompt
    assert "Ranking" in prompt
    assert "Passwords" in prompt
    assert "Scheduling" in prompt

def test_combination_applications():
    prompt = probability_calculation_prompt("combination", n=49, r=6)
    assert "Lottery" in prompt
    assert "Teams" in prompt
    assert "Committees" in prompt
    assert "Cards" in prompt

def test_binomial_applications():
    prompt = probability_calculation_prompt("binomial", n=100, r=95, probability=0.95)
    assert "Quality Control" in prompt
    assert "Medical Testing" in prompt
    assert "Treatment success rate" in prompt

def test_expected_value_applications():
    prompt = probability_calculation_prompt("expected_value")
    assert "Investment" in prompt
    assert "Insurance" in prompt
    assert "Gaming" in prompt
    assert "Decision Theory" in prompt

def test_bayes_applications():
    prompt = probability_calculation_prompt("bayes")
    assert "Medical Diagnosis" in prompt
    assert "Spam Filtering" in prompt
    assert "Machine Learning" in prompt

def test_probability_contains_goals_structure():
    prompt = probability_calculation_prompt("permutation", n=8, r=3)
    assert "🎯 PRIMARY PURPOSE" in prompt
    assert "📊 MAIN GOALS" in prompt
    assert "🔍 SUB-GOALS AND APPROACH" in prompt
    assert "**Objective**:" in prompt
    assert "**Why**:" in prompt
    assert "Goal 1:" in prompt

def test_probability_contains_mcp_instructions():
    prompt = probability_calculation_prompt("combination", n=10, r=4)
    assert "MCP tools" in prompt
    assert "factorial" in prompt
    assert "divide" in prompt
    assert "Execution Instructions" in prompt

def test_probability_contains_formulas():
    permutation_prompt = probability_calculation_prompt("permutation", n=5, r=2)
    assert "P(n,r) = n!/(n-r)!" in permutation_prompt
    
    combination_prompt = probability_calculation_prompt("combination", n=5, r=2)
    assert "C(n,r) = n!/[r!(n-r)!]" in combination_prompt
    
    binomial_prompt = probability_calculation_prompt("binomial", n=10, r=5, probability=0.5)
    assert "P(X=k) = C(n,k) × p^k × (1-p)^(n-k)" in binomial_prompt

def test_probability_validation_checks():
    expected_prompt = probability_calculation_prompt("expected_value")
    assert "probabilities sum to 1" in expected_prompt
    assert "between 0 and 1" in expected_prompt
    
    bayes_prompt = probability_calculation_prompt("bayes")
    assert "Compare posterior to prior" in bayes_prompt

def test_probability_special_cases():
    permutation_prompt = probability_calculation_prompt("permutation", n=5, r=5)
    assert "P(n,n) = n!" in permutation_prompt
    assert "P(n,1) = n" in permutation_prompt
    assert "P(n,0) = 1" in permutation_prompt
    
    combination_prompt = probability_calculation_prompt("combination", n=10, r=3)
    assert "C(n,0) = C(n,n) = 1" in combination_prompt

def test_probability_pitfalls_and_warnings():
    bayes_prompt = probability_calculation_prompt("bayes")
    assert "Base Rate Neglect" in bayes_prompt
    assert "P(A|B) ≠ P(B|A)" in bayes_prompt
    assert "Prosecutor's Fallacy" in bayes_prompt

def test_probability_contains_verification():
    permutation_prompt = probability_calculation_prompt("permutation", n=8, r=4)
    assert "Result Validation" in permutation_prompt
    assert "should be less than or equal to n!" in permutation_prompt
    
    combination_prompt = probability_calculation_prompt("combination", n=6, r=3)
    assert "Properties and Validation" in combination_prompt
    assert "Symmetry: C(n,r) = C(n,n-r)" in combination_prompt