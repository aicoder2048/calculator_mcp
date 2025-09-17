import pytest
from src.mcp_server.tools.factorial_tool import factorial
from src.mcp_server.models.schemas import FactorialInput
from unittest.mock import AsyncMock

@pytest.mark.asyncio
async def test_factorial_small():
    input_data = FactorialInput(n=5)
    ctx = AsyncMock()
    result = await factorial(input_data, ctx)
    assert result == 120
    ctx.report_progress.assert_not_called()

@pytest.mark.asyncio
async def test_factorial_zero():
    input_data = FactorialInput(n=0)
    ctx = AsyncMock()
    result = await factorial(input_data, ctx)
    assert result == 1

@pytest.mark.asyncio
async def test_factorial_one():
    input_data = FactorialInput(n=1)
    ctx = AsyncMock()
    result = await factorial(input_data, ctx)
    assert result == 1

@pytest.mark.asyncio
async def test_factorial_large_with_progress():
    input_data = FactorialInput(n=15)
    ctx = AsyncMock()
    result = await factorial(input_data, ctx)
    assert result == 1307674368000
    # Should report progress for n > 10
    assert ctx.report_progress.call_count == 15

@pytest.mark.asyncio
async def test_factorial_validation_negative():
    # Test that negative numbers are rejected
    with pytest.raises(ValueError):
        FactorialInput(n=-1)

@pytest.mark.asyncio
async def test_factorial_validation_too_large():
    # Test that numbers > 20 are rejected
    with pytest.raises(ValueError):
        FactorialInput(n=21)

@pytest.mark.parametrize("n,expected", [
    (2, 2),
    (3, 6),
    (4, 24),
    (6, 720),
])
@pytest.mark.asyncio
async def test_factorial_values(n, expected):
    input_data = FactorialInput(n=n)
    ctx = AsyncMock()
    result = await factorial(input_data, ctx)
    assert result == expected