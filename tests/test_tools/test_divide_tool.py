import pytest
from src.mcp_server.tools.divide_tool import divide
from src.mcp_server.models.schemas import DivideInput

@pytest.mark.asyncio
async def test_divide_normal():
    input_data = DivideInput(a=10, b=2)
    result = await divide(input_data)
    assert result["status"] == "success"
    assert result["result"] == 5

@pytest.mark.asyncio
async def test_divide_by_zero():
    input_data = DivideInput(a=10, b=0)
    result = await divide(input_data)
    assert result["status"] == "failed"
    assert "Division by zero" in result["error"]