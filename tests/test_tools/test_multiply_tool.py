import pytest
from src.mcp_server.tools.multiply_tool import multiply
from src.mcp_server.models.schemas import MultiplyInput

@pytest.mark.asyncio
async def test_multiply_positive_numbers():
    input_data = MultiplyInput(a=5, b=3)
    result = await multiply(input_data)
    assert result == 15

@pytest.mark.asyncio
async def test_multiply_negative_numbers():
    input_data = MultiplyInput(a=-5, b=-3)
    result = await multiply(input_data)
    assert result == 15

@pytest.mark.asyncio
async def test_multiply_mixed_numbers():
    input_data = MultiplyInput(a=5, b=-3)
    result = await multiply(input_data)
    assert result == -15

@pytest.mark.asyncio
async def test_multiply_by_zero():
    input_data = MultiplyInput(a=10, b=0)
    result = await multiply(input_data)
    assert result == 0

@pytest.mark.asyncio
async def test_multiply_decimals():
    input_data = MultiplyInput(a=2.5, b=4.0)
    result = await multiply(input_data)
    assert result == 10.0