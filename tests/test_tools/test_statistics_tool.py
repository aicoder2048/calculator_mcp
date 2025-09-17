import pytest
from src.mcp_server.tools.statistics_tool import mean, median, stddev
from src.mcp_server.models.schemas import StatisticsInput

@pytest.mark.asyncio
async def test_mean_simple():
    input_data = StatisticsInput(data=[1, 2, 3, 4, 5])
    result = await mean(input_data)
    assert result == 3.0

@pytest.mark.asyncio
async def test_mean_decimals():
    input_data = StatisticsInput(data=[1.5, 2.5, 3.5])
    result = await mean(input_data)
    assert result == pytest.approx(2.5)

@pytest.mark.asyncio
async def test_mean_negative_numbers():
    input_data = StatisticsInput(data=[-1, -2, -3])
    result = await mean(input_data)
    assert result == -2.0

@pytest.mark.asyncio
async def test_median_odd_count():
    input_data = StatisticsInput(data=[1, 3, 2, 5, 4])
    result = await median(input_data)
    assert result == 3

@pytest.mark.asyncio
async def test_median_even_count():
    input_data = StatisticsInput(data=[1, 2, 3, 4])
    result = await median(input_data)
    assert result == 2.5

@pytest.mark.asyncio
async def test_median_single_value():
    input_data = StatisticsInput(data=[42])
    result = await median(input_data)
    assert result == 42

@pytest.mark.asyncio
async def test_stddev_simple():
    input_data = StatisticsInput(data=[1, 2, 3, 4, 5])
    result = await stddev(input_data)
    assert result == pytest.approx(1.5811, rel=1e-4)

@pytest.mark.asyncio
async def test_stddev_identical_values():
    input_data = StatisticsInput(data=[5, 5, 5, 5])
    result = await stddev(input_data)
    assert result == 0.0

@pytest.mark.asyncio
async def test_stddev_single_value_raises_error():
    input_data = StatisticsInput(data=[42])
    with pytest.raises(ValueError, match="Standard deviation requires at least 2 data points"):
        await stddev(input_data)

@pytest.mark.asyncio
async def test_statistics_input_validation():
    # Test empty list is rejected
    with pytest.raises(ValueError):
        StatisticsInput(data=[])