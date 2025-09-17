import pytest
from src.mcp_server.tools.subtract_tool import subtract
from src.mcp_server.models.schemas import SubtractInput

@pytest.mark.asyncio
async def test_subtract_positive_numbers():
    input_data = SubtractInput(a=10, b=3)
    result = await subtract(input_data)
    assert result == 7

@pytest.mark.asyncio
async def test_subtract_negative_result():
    input_data = SubtractInput(a=3, b=10)
    result = await subtract(input_data)
    assert result == -7

@pytest.mark.asyncio
async def test_subtract_negative_numbers():
    input_data = SubtractInput(a=-5, b=-3)
    result = await subtract(input_data)
    assert result == -2

@pytest.mark.asyncio
async def test_subtract_mixed_numbers():
    input_data = SubtractInput(a=5.5, b=-2.5)
    result = await subtract(input_data)
    assert result == 8.0