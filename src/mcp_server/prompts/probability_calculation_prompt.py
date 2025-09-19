def probability_calculation_prompt(calculation_type: str, n: int = None, r: int = None, probability: float = None, trials: int = None) -> str:
    """Generate a prompt for probability and combinatorics calculations with detailed MCP tool usage."""
    
    calc_type = calculation_type.lower()
    
    if calc_type == "permutation" or calc_type == "arrangement":
        return f"""## Probability Task: Permutation Calculation

### 🎯 PRIMARY PURPOSE
Calculate the number of permutations P(n,r) = n!/(n-r)! for arranging {r} items from {n} total items, where order matters.

### 📊 MAIN GOALS
1. **Factorial Calculation** - Compute necessary factorial values
2. **Permutation Formula** - Apply P(n,r) = n!/(n-r)!
3. **Result Interpretation** - Understand the meaning of the result
4. **Practical Application** - Relate to real-world scenarios

### 🔍 SUB-GOALS AND APPROACH

#### Goal 1: Understanding Permutations
**Objective**: Clarify what permutations represent
**Why**: Essential to know when to use permutations vs combinations

**Key Concepts**:
- Permutations count arrangements where ORDER MATTERS
- Example: ABC, ACB, BAC are different permutations
- Used for: Rankings, sequences, ordered selections
- Formula: P(n,r) = n!/(n-r)!

#### Goal 2: Factorial Calculations
**Objective**: Calculate the required factorial values
**Why**: Factorials are the building blocks of permutation formulas

**Step 2.1**: Calculate n! = {n}!
   - Purpose: Total arrangements of all {n} items
   - Method: factorial({n})
   - Meaning: If we used all items, this would be the answer
   - Growth rate: Factorials grow extremely fast

**Step 2.2**: Calculate (n-r)! = ({n}-{r})! = {n-r if n and r else 'n-r'}!
   - Purpose: Arrangements of unused items
   - Method: factorial({n-r if n and r else 'n-r'})
   - Why needed: We're selecting only {r} items, not all {n}
   - This removes the arrangements of items we don't select

#### Goal 3: Permutation Calculation
**Objective**: Compute P({n},{r}) using the factorial values
**Why**: This gives us the final count of ordered arrangements

**Step 3.1**: Apply the permutation formula
   - Formula: P(n,r) = n!/(n-r)!
   - Calculate: divide(n_factorial, n_minus_r_factorial)
   - Result: Number of ways to arrange {r} items from {n}
   - Verification: Result should be ≤ n!

**Step 3.2**: Alternative calculation (for understanding)
   - Direct multiplication: n × (n-1) × (n-2) × ... × (n-r+1)
   - This gives the same result but shows the pattern
   - First position: {n} choices
   - Second position: {n}-1 choices
   - Continue for {r} positions

#### Goal 4: Result Validation
**Objective**: Verify the calculation makes sense
**Why**: Catch errors and build intuition

**Validation checks**:
- P(n,r) should be less than or equal to n!
- P(n,n) should equal n!
- P(n,1) should equal n
- P(n,0) should equal 1 (by convention)

### 💡 Common Applications
- **Sports**: Ranking top 3 from 10 competitors
- **Passwords**: Arranging characters without repetition
- **Scheduling**: Ordering tasks or events
- **Elections**: Selecting president, VP, secretary from candidates

### 📐 Formula Reference
- Permutation: P(n,r) = n!/(n-r)!
- Special cases: P(n,n) = n!, P(n,1) = n, P(n,0) = 1
- With repetition: n^r (not covered here)

### ⚙️ Execution Instructions
Please use MCP tools (factorial, divide) for ALL calculations.
Handle large factorials with care - they grow very quickly."""

    elif calc_type == "combination" or calc_type == "choose":
        return f"""## Probability Task: Combination Calculation

### 🎯 PRIMARY PURPOSE
Calculate the number of combinations C(n,r) = n!/[r!(n-r)!] for choosing {r} items from {n} total items, where order doesn't matter.

### 📊 MAIN GOALS
1. **Factorial Computation** - Calculate required factorials
2. **Combination Formula** - Apply C(n,r) = n!/[r!(n-r)!]
3. **Result Understanding** - Interpret the combination count
4. **Practical Context** - Connect to real-world selection problems

### 🔍 SUB-GOALS AND APPROACH

#### Goal 1: Understanding Combinations
**Objective**: Clarify the difference between combinations and permutations
**Why**: Critical to choose the right formula for the problem

**Key Concepts**:
- Combinations count selections where ORDER DOESN'T MATTER
- Example: {{A,B,C}} is the same as {{B,A,C}} or {{C,A,B}}
- Used for: Groups, teams, subsets, selections
- Formula: C(n,r) = n!/[r!(n-r)!] = P(n,r)/r!

#### Goal 2: Factorial Calculations
**Objective**: Compute all necessary factorials
**Why**: Three factorials are needed for the combination formula

**Step 2.1**: Calculate n! = {n}!
   - Purpose: Total arrangements if order mattered
   - Method: factorial({n})
   - This is our starting point (numerator)

**Step 2.2**: Calculate r! = {r}!
   - Purpose: Remove order within selected items
   - Method: factorial({r})
   - Why: Each selection can be arranged r! ways

**Step 2.3**: Calculate (n-r)! = ({n}-{r})! = {n-r if n and r else 'n-r'}!
   - Purpose: Handle unselected items
   - Method: factorial({n-r if n and r else 'n-r'})
   - Why: Accounts for items not chosen

#### Goal 3: Combination Calculation
**Objective**: Compute C({n},{r}) using the factorial values
**Why**: This gives the count of unordered selections

**Step 3.1**: Calculate denominator
   - Purpose: Remove ordering from both selected and unselected items
   - Calculate r! × (n-r)!: multiply(r_factorial, n_minus_r_factorial)
   - This eliminates all internal orderings

**Step 3.2**: Apply combination formula
   - Formula: C(n,r) = n!/[r!(n-r)!]
   - Calculate: divide(n_factorial, denominator)
   - Result: Number of ways to choose {r} items from {n}
   - Note: Also written as "n choose r" or (n r) or nCr

**Step 3.3**: Relationship to permutations
   - C(n,r) = P(n,r)/r!
   - Combinations are permutations divided by r!
   - This removes the r! different orderings of each selection

#### Goal 4: Properties and Validation
**Objective**: Verify result using combination properties
**Why**: Ensures correctness and builds understanding

**Key properties**:
- Symmetry: C(n,r) = C(n,n-r)
- Pascal's Triangle: C(n,r) = C(n-1,r-1) + C(n-1,r)
- Sum property: ΣC(n,r) for r=0 to n equals 2^n
- Boundary: C(n,0) = C(n,n) = 1

### 💡 Common Applications
- **Lottery**: Choosing 6 numbers from 49
- **Teams**: Selecting 5 players from 12
- **Committees**: Forming groups from larger pools
- **Cards**: Poker hands (5 cards from 52)
- **Statistics**: Sampling without replacement

### 📐 Formula Reference
- Combination: C(n,r) = n!/[r!(n-r)!]
- Alternative: C(n,r) = P(n,r)/r!
- Binomial coefficient: Same as C(n,r)
- Special cases: C(n,0) = 1, C(n,1) = n, C(n,n) = 1

### ⚙️ Execution Instructions
Please use MCP tools (factorial, multiply, divide) for ALL calculations.
Be careful with large factorials - consider cancellation when possible."""

    elif calc_type == "binomial" or calc_type == "binomial_probability":
        return f"""## Probability Task: Binomial Distribution Calculation

### 🎯 PRIMARY PURPOSE
Calculate binomial probability P(X=k) for exactly {r if r else 'k'} successes in {trials if trials else 'n'} independent trials with success probability {probability if probability else 'p'}.

### 📊 MAIN GOALS
1. **Combination Calculation** - Count ways to arrange successes
2. **Probability Computation** - Calculate success and failure probabilities
3. **Binomial Formula** - Apply P(X=k) = C(n,k) × p^k × (1-p)^(n-k)
4. **Result Interpretation** - Understand probability meaning

### 🔍 SUB-GOALS AND APPROACH

#### Goal 1: Understanding Binomial Distribution
**Objective**: Clarify when to use binomial distribution
**Why**: Must verify conditions for binomial model

**Binomial conditions**:
1. Fixed number of trials: {trials if trials else 'n'}
2. Each trial has two outcomes: success or failure
3. Constant probability: p = {probability if probability else 'p'} for each trial
4. Independent trials: One outcome doesn't affect another
5. We want exactly {r if r else 'k'} successes

#### Goal 2: Combination Component
**Objective**: Calculate C(n,k) - ways to arrange k successes in n trials
**Why**: Successes can occur in different positions

**Step 2.1**: Calculate C({trials if trials else 'n'},{r if r else 'k'})
   - Purpose: Count different patterns of success
   - Formula: C(n,k) = n!/[k!(n-k)!]
   - Calculate factorials:
     - factorial({trials if trials else 'n'})
     - factorial({r if r else 'k'})
     - factorial({(trials-r) if trials and r else 'n-k'})
   - Apply formula: divide(n_factorial, multiply(k_factorial, n_minus_k_factorial))

#### Goal 3: Probability Components
**Objective**: Calculate probability of specific success/failure pattern
**Why**: Each pattern has the same probability

**Step 3.1**: Calculate success probability p^k
   - Purpose: Probability of k successes occurring
   - Method: power({probability if probability else 'p'}, {r if r else 'k'})
   - Meaning: Each success has probability p, need k of them

**Step 3.2**: Calculate failure probability (1-p)^(n-k)
   - Purpose: Probability of (n-k) failures occurring
   - Calculate 1-p: subtract(1, {probability if probability else 'p'})
   - Method: power(failure_probability, {(trials-r) if trials and r else 'n-k'})
   - Meaning: Each failure has probability (1-p), need (n-k) of them

#### Goal 4: Final Probability Calculation
**Objective**: Combine all components for final probability
**Why**: This gives P(X=k), the probability of exactly k successes

**Step 4.1**: Apply binomial formula
   - Formula: P(X=k) = C(n,k) × p^k × (1-p)^(n-k)
   - Multiply components:
     - First: multiply(combination, p_to_k)
     - Then: multiply(result, failure_probability_to_n_minus_k)
   - Result: Probability of exactly {r if r else 'k'} successes

**Step 4.2**: Interpretation
   - Result is between 0 and 1
   - Can be expressed as percentage: multiply by 100
   - Higher values mean more likely outcome
   - Sum of all P(X=k) for k=0 to n equals 1

### 💡 Common Applications
- **Quality Control**: Defective items in batch
- **Medical Testing**: Treatment success rate
- **Surveys**: Yes/no responses
- **Sports**: Free throw success
- **Gaming**: Coin flips, dice rolls

### 📊 Related Calculations
- **Expected value**: E(X) = n × p
- **Variance**: Var(X) = n × p × (1-p)
- **Standard deviation**: σ = √[n × p × (1-p)]
- **Most likely outcome**: Mode ≈ n × p (rounded)

### 📐 Formula Reference
- Binomial probability: P(X=k) = C(n,k) × p^k × (1-p)^(n-k)
- Combination: C(n,k) = n!/[k!(n-k)!]
- Expected value: μ = np
- Variance: σ² = np(1-p)

### ⚙️ Execution Instructions
Please use MCP tools (factorial, multiply, divide, power, subtract) for ALL calculations.
Maintain precision for probability values (at least 4 decimal places)."""

    elif calc_type == "expected_value" or calc_type == "expectation":
        return f"""## Probability Task: Expected Value Calculation

### 🎯 PRIMARY PURPOSE
Calculate the expected value (mean) of a probability distribution, representing the long-run average outcome.

### 📊 MAIN GOALS
1. **Probability Validation** - Ensure probabilities sum to 1
2. **Weighted Calculation** - Multiply each outcome by its probability
3. **Summation** - Add all weighted values
4. **Interpretation** - Understand practical meaning

### 🔍 SUB-GOALS AND APPROACH

#### Goal 1: Understanding Expected Value
**Objective**: Clarify what expected value represents
**Why**: Often misunderstood as "most likely" value

**Key concepts**:
- Expected value is the weighted average of all outcomes
- Symbol: E(X) or μ (mu)
- Not necessarily a possible outcome
- Represents long-run average over many trials
- Used in decision-making and risk assessment

#### Goal 2: Input Validation
**Objective**: Verify probability distribution is valid
**Why**: Invalid probabilities lead to meaningless results

**Step 2.1**: Check probability constraints
   - Each probability must be between 0 and 1
   - Sum of all probabilities must equal 1
   - Use add() tool to sum probabilities
   - If sum ≠ 1, distribution is invalid

#### Goal 3: Expected Value Calculation
**Objective**: Compute E(X) = Σ(xi × pi)
**Why**: This is the theoretical mean of the distribution

**Step 3.1**: Calculate weighted values
   - For each outcome xi with probability pi:
   - Calculate: multiply(outcome_value, probability)
   - This represents the contribution to the average
   - Store each weighted value

**Step 3.2**: Sum all weighted values
   - Add all products: add(weighted1, add(weighted2, ...))
   - Or iteratively: keep running total
   - Result is the expected value E(X)

#### Goal 4: Variance and Standard Deviation (Optional)
**Objective**: Measure spread around expected value
**Why**: Expected value alone doesn't show risk/variability

**Step 4.1**: Calculate variance
   - Var(X) = E(X²) - [E(X)]²
   - Or: Var(X) = Σ[(xi - μ)² × pi]
   - Shows spread of distribution

**Step 4.2**: Calculate standard deviation
   - σ = √Var(X)
   - Use root(variance, 2)
   - More interpretable than variance

### 💡 Common Applications
- **Investment**: Expected return on portfolio
- **Insurance**: Expected claim amount
- **Gaming**: Casino game payouts
- **Decision Theory**: Comparing alternatives
- **Quality Control**: Expected defects

### 📊 Example Scenarios
1. **Dice roll**: E(X) = (1+2+3+4+5+6)/6 = 3.5
2. **Coin flip**: $1 for heads, $0 for tails: E(X) = 0.5
3. **Investment**: Multiple scenarios with different returns
4. **Lottery**: Very small probability of large payout

### 📐 Formula Reference
- Expected value: E(X) = Σ(xi × pi)
- Variance: Var(X) = E(X²) - [E(X)]²
- Standard deviation: σ = √Var(X)
- For binomial: E(X) = n × p

### ⚙️ Execution Instructions
Please use MCP tools (multiply, add, subtract, power, root) for ALL calculations.
Process each outcome-probability pair systematically."""

    elif calc_type == "bayes" or calc_type == "conditional":
        return f"""## Probability Task: Bayesian Probability Calculation

### 🎯 PRIMARY PURPOSE
Calculate conditional probability P(A|B) using Bayes' Theorem, updating beliefs based on new evidence.

### 📊 MAIN GOALS
1. **Prior Probability** - Establish initial beliefs
2. **Likelihood Calculation** - Process new evidence
3. **Bayes' Formula** - Apply P(A|B) = P(B|A)×P(A)/P(B)
4. **Posterior Interpretation** - Understand updated probability

### 🔍 SUB-GOALS AND APPROACH

#### Goal 1: Understanding Bayes' Theorem
**Objective**: Clarify the components and meaning
**Why**: Essential for correct application

**Components**:
- P(A|B): Posterior - probability of A given B occurred
- P(B|A): Likelihood - probability of B given A is true
- P(A): Prior - initial probability of A
- P(B): Evidence - total probability of B

**Formula**: P(A|B) = [P(B|A) × P(A)] / P(B)

#### Goal 2: Prior and Likelihood
**Objective**: Identify and calculate initial probabilities
**Why**: These are the inputs to Bayes' formula

**Step 2.1**: Establish prior P(A)
   - Initial probability before evidence
   - Often from historical data or base rates
   - Must be between 0 and 1

**Step 2.2**: Determine likelihood P(B|A)
   - Probability of observing evidence given hypothesis
   - Often from test sensitivity/specificity
   - Key to updating beliefs

#### Goal 3: Total Probability Calculation
**Objective**: Calculate P(B) using law of total probability
**Why**: Denominator in Bayes' formula, normalizes result

**Step 3.1**: Apply total probability law
   - P(B) = P(B|A)×P(A) + P(B|¬A)×P(¬A)
   - Calculate P(¬A): subtract(1, P(A))
   - Calculate first term: multiply(P(B|A), P(A))
   - Calculate second term: multiply(P(B|¬A), P(¬A))
   - Sum terms: add(term1, term2)

#### Goal 4: Posterior Calculation
**Objective**: Compute updated probability P(A|B)
**Why**: This is our revised belief after evidence

**Step 4.1**: Apply Bayes' Theorem
   - Numerator: multiply(P(B|A), P(A))
   - Denominator: P(B) from Goal 3
   - Result: divide(numerator, denominator)
   - This is P(A|B), our updated probability

**Step 4.2**: Interpretation
   - Compare posterior to prior
   - If posterior > prior: evidence supports A
   - If posterior < prior: evidence against A
   - Magnitude shows strength of evidence

### 💡 Classic Applications
- **Medical Diagnosis**: Disease probability given positive test
- **Spam Filtering**: Email classification
- **Legal**: Guilt probability given evidence
- **Machine Learning**: Classification algorithms
- **Quality Control**: Defect source identification

### 📊 Common Pitfalls
- **Base Rate Neglect**: Ignoring prior probabilities
- **Confusion**: P(A|B) ≠ P(B|A)
- **Prosecutor's Fallacy**: Confusing P(evidence|guilty) with P(guilty|evidence)

### 📐 Formula Reference
- Bayes' Theorem: P(A|B) = P(B|A)×P(A)/P(B)
- Total Probability: P(B) = Σ P(B|Ai)×P(Ai)
- Complement: P(¬A) = 1 - P(A)
- Independence: P(A|B) = P(A) if independent

### ⚙️ Execution Instructions
Please use MCP tools (multiply, divide, add, subtract) for ALL calculations.
Be precise with probability values - small changes can significantly affect results."""

    else:
        return f"""## Probability Calculation Guide: Multiple Analysis Options

### 🎯 PRIMARY PURPOSE
Provide comprehensive probability and combinatorics calculations using MCP mathematical tools.

### 📊 AVAILABLE CALCULATION TYPES

#### 1. Permutation/Arrangement ("permutation" or "arrangement")
- Calculate P(n,r) = n!/(n-r)!
- Order matters in selection
- Example: Ranking, passwords, sequences
- Parameters: n (total items), r (items to arrange)

#### 2. Combination/Choose ("combination" or "choose")
- Calculate C(n,r) = n!/[r!(n-r)!]
- Order doesn't matter in selection
- Example: Lottery, committees, groups
- Parameters: n (total items), r (items to choose)

#### 3. Binomial Probability ("binomial" or "binomial_probability")
- Calculate P(X=k) for binomial distribution
- Fixed trials with constant success probability
- Example: Quality control, medical trials
- Parameters: n (trials), r (successes), p (probability)

#### 4. Expected Value ("expected_value" or "expectation")
- Calculate E(X) = Σ(xi × pi)
- Weighted average of outcomes
- Example: Investment returns, insurance
- Parameters: outcomes and probabilities

#### 5. Bayes' Theorem ("bayes" or "conditional")
- Calculate P(A|B) conditional probability
- Update probability with new evidence
- Example: Medical diagnosis, spam filtering
- Parameters: prior, likelihood, evidence

### 🔍 GENERAL PROBABILITY APPROACH

#### Choosing the Right Method
1. **Order matters?** → Use Permutation
2. **Order doesn't matter?** → Use Combination
3. **Repeated trials?** → Use Binomial
4. **Average outcome?** → Use Expected Value
5. **Updating belief?** → Use Bayes

#### Key Formulas Using MCP Tools
- **Factorial**: factorial(n)
- **Division**: divide(numerator, denominator)
- **Power**: power(base, exponent)
- **Multiplication**: multiply(a, b)
- **Addition**: add(a, b)

### 💡 Probability Principles
- Probabilities range from 0 to 1
- Sum of all probabilities = 1
- P(A or B) = P(A) + P(B) - P(A and B)
- P(A and B) = P(A) × P(B) if independent
- P(not A) = 1 - P(A)

### 📐 Common Distributions
- **Uniform**: All outcomes equally likely
- **Binomial**: Fixed trials, two outcomes
- **Normal**: Bell curve (approximation for large n)
- **Poisson**: Rare events in time/space

### ⚙️ Execution Instructions
Specify the calculation_type and required parameters:
- For permutation: n and r
- For combination: n and r
- For binomial: n, r (successes), p (probability)
- For expected value: outcomes and probabilities
- For Bayes: prior, likelihood, evidence

Please use MCP tools for ALL calculations.
Maintain precision in probability calculations."""