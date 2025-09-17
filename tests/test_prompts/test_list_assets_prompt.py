from src.mcp_server.prompts.list_assets_prompt import list_all_assets

def test_list_assets_contains_tools_section():
    prompt = list_all_assets()
    assert "## 🔧 Tools" in prompt or "## Tools" in prompt
    assert "add(a: float, b: float)" in prompt
    assert "subtract" in prompt
    assert "multiply" in prompt
    assert "divide" in prompt
    assert "Example:" in prompt

def test_list_assets_contains_prompts_section():
    prompt = list_all_assets()
    assert "## 📝 Prompts" in prompt or "## Prompts" in prompt
    assert "build_multiplication_table" in prompt
    assert "list_all_assets" in prompt
    assert "solve_equation_conversation" in prompt
    assert "financial_calculation" in prompt

def test_list_assets_comprehensive_request():
    prompt = list_all_assets()
    assert "Calculator MCP Server" in prompt
    assert "Tools" in prompt
    assert "Prompts" in prompt
    assert "Usage Tips" in prompt