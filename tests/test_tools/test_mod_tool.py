import pytest
from src.mcp_server.tools.mod_tool import mod
from src.mcp_server.models.schemas import ModInput

@pytest.mark.asyncio
async def test_mod_normal():
    input_data = ModInput(a=10, b=3)
    result = await mod(input_data)
    assert result == 1

@pytest.mark.asyncio
async def test_mod_exact_division():
    input_data = ModInput(a=15, b=5)
    result = await mod(input_data)
    assert result == 0

@pytest.mark.asyncio
async def test_mod_negative_dividend():
    input_data = ModInput(a=-10, b=3)
    result = await mod(input_data)
    assert result == 2  # Python's modulo behavior with negatives

@pytest.mark.asyncio
async def test_mod_negative_divisor():
    input_data = ModInput(a=10, b=-3)
    result = await mod(input_data)
    assert result == -2  # Python's modulo behavior

@pytest.mark.asyncio
async def test_mod_divisor_validation():
    with pytest.raises(ValueError, match="Divisor cannot be zero"):
        ModInput(a=10, b=0)

@pytest.mark.asyncio
async def test_mod_large_numbers():
    input_data = ModInput(a=1000, b=7)
    result = await mod(input_data)
    assert result == 6