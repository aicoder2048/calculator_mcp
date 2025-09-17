from src.mcp_server.prompts.solve_equation_prompt import solve_equation_conversation
from fastmcp.prompts import PromptMessage

def test_solve_equation_conversation_structure():
    equation = "2x + 5 = 15"
    conversation = solve_equation_conversation(equation)
    
    assert len(conversation) == 4
    assert all(isinstance(msg, PromptMessage) for msg in conversation)

def test_solve_equation_conversation_content():
    equation = "x^2 + 3x - 4 = 0"
    conversation = solve_equation_conversation(equation)
    
    # First message should contain the equation
    assert equation in conversation[0].content.text
    assert conversation[0].role == "user"
    
    # Assistant responses should be helpful
    assert "solve this equation step by step" in conversation[1].content.text
    assert conversation[1].role == "assistant"
    
    assert "identify the type of equation" in conversation[2].content.text
    assert conversation[2].role == "assistant"
    
    # Final user message asks for clarity
    assert "show me each step clearly" in conversation[3].content.text
    assert conversation[3].role == "user"

def test_solve_equation_conversation_roles():
    conversation = solve_equation_conversation("y = 2x + 1")
    roles = [msg.role for msg in conversation]
    expected_roles = ["user", "assistant", "assistant", "user"]
    assert roles == expected_roles