from src.mcp_server.prompts.multiplication_table_prompt import build_multiplication_table

def test_multiplication_table_default():
    prompt = build_multiplication_table()
    assert "10x10" in prompt
    assert "Starting from: 1" in prompt
    assert "products from 1 to 10" in prompt

def test_multiplication_table_custom():
    prompt = build_multiplication_table(size=5, start=3)
    assert "5x5" in prompt
    assert "Starting from: 3" in prompt
    assert "products from 3 to 7" in prompt

def test_multiplication_table_large():
    prompt = build_multiplication_table(size=12, start=2)
    assert "12x12" in prompt
    assert "Starting from: 2" in prompt
    assert "products from 2 to 13" in prompt

def test_multiplication_table_contains_instructions():
    prompt = build_multiplication_table()
    assert "Create a multiplication table" in prompt
    assert "Format: Well-formatted table" in prompt
    assert "row and column headers" in prompt