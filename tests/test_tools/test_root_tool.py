import pytest
from src.mcp_server.tools.root_tool import root
from src.mcp_server.models.schemas import RootInput

@pytest.mark.asyncio
async def test_square_root():
    input_data = RootInput(number=16, degree=2)
    result = await root(input_data)
    assert result == pytest.approx(4.0)

@pytest.mark.asyncio
async def test_cube_root():
    input_data = RootInput(number=27, degree=3)
    result = await root(input_data)
    assert result == pytest.approx(3.0)

@pytest.mark.asyncio
async def test_default_square_root():
    input_data = RootInput(number=25)  # degree defaults to 2
    result = await root(input_data)
    assert result == pytest.approx(5.0)

@pytest.mark.asyncio
async def test_root_of_one():
    input_data = RootInput(number=1, degree=5)
    result = await root(input_data)
    assert result == pytest.approx(1.0)

@pytest.mark.asyncio
async def test_negative_number_odd_root():
    input_data = RootInput(number=-8, degree=3)
    result = await root(input_data)
    assert result == pytest.approx(-2.0)

@pytest.mark.asyncio
async def test_negative_number_even_root_raises_error():
    input_data = RootInput(number=-4, degree=2)
    with pytest.raises(ValueError, match="Cannot calculate even root of negative number"):
        await root(input_data)