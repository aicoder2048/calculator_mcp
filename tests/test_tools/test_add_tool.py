import pytest
from src.mcp_server.tools.add_tool import add
from src.mcp_server.models.schemas import AddInput

@pytest.mark.asyncio
async def test_add_positive_numbers():
    input_data = AddInput(a=5, b=3)
    result = await add(input_data)
    assert result == 8

@pytest.mark.asyncio
async def test_add_negative_numbers():
    input_data = AddInput(a=-5, b=-3)
    result = await add(input_data)
    assert result == -8

@pytest.mark.asyncio
async def test_add_mixed_numbers():
    input_data = AddInput(a=5.5, b=-2.5)
    result = await add(input_data)
    assert result == 3.0