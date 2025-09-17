import pytest
from src.mcp_server.tools.power_tool import power
from src.mcp_server.models.schemas import PowerInput

@pytest.mark.parametrize("base,exponent,expected", [
    (2, 3, 8),
    (5, 0, 1),
    (10, -1, 0.1),
    (4, 0.5, 2),
    (-2, 2, 4),
    (-2, 3, -8),
])
@pytest.mark.asyncio
async def test_power_operations(base, exponent, expected):
    input_data = PowerInput(base=base, exponent=exponent)
    result = await power(input_data)
    assert result == pytest.approx(expected)

@pytest.mark.asyncio
async def test_power_zero_base():
    input_data = PowerInput(base=0, exponent=5)
    result = await power(input_data)
    assert result == 0