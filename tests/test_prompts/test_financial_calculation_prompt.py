from src.mcp_server.prompts.financial_calculation_prompt import financial_calculation_prompt

def test_financial_calculation_prompt_content():
    prompt = financial_calculation_prompt(1000.0, 5.0, 3)
    
    assert "$1,000.00" in prompt
    assert "5.0%" in prompt
    assert "3 years" in prompt
    
def test_financial_calculation_prompt_calculations():
    prompt = financial_calculation_prompt(5000.0, 3.5, 5)
    
    assert "Calculate compound interest" in prompt
    assert "Total amount after the period" in prompt
    assert "Total interest earned" in prompt
    assert "Monthly equivalent payment" in prompt
    assert "Effective annual rate" in prompt

def test_financial_calculation_prompt_formatting():
    prompt = financial_calculation_prompt(12345.67, 4.25, 10)
    
    # Check proper currency formatting
    assert "$12,345.67" in prompt
    assert "4.25%" in prompt
    assert "10 years" in prompt

def test_financial_calculation_prompt_structure():
    prompt = financial_calculation_prompt(1500.0, 2.8, 7)
    
    lines = prompt.split('\n')
    # Should have multiple calculation items numbered
    calculation_items = [line for line in lines if line.strip().startswith(('1.', '2.', '3.', '4.'))]
    assert len(calculation_items) == 4