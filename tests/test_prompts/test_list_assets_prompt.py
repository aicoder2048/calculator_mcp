from src.mcp_server.prompts.list_assets_prompt import list_all_assets

def test_list_assets_contains_tools_section():
    prompt = list_all_assets()
    assert "## Tools" in prompt
    assert "Tool name (function call name)" in prompt
    assert "Full function signature" in prompt
    assert "Brief description" in prompt
    assert "Parameter details" in prompt
    assert "Return type and format" in prompt
    assert "Example usage" in prompt

def test_list_assets_contains_prompts_section():
    prompt = list_all_assets()
    assert "## Prompts" in prompt
    assert "Prompt name (function call name)" in prompt
    assert "Function signature with parameters" in prompt
    assert "Description of the prompt's purpose" in prompt
    assert "Parameters required" in prompt
    assert "Expected output format" in prompt

def test_list_assets_comprehensive_request():
    prompt = list_all_assets()
    assert "comprehensive list" in prompt
    assert "all available assets" in prompt
    assert "MCP server" in prompt
    assert "clear, structured format" in prompt