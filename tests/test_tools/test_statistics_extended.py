import pytest
from src.mcp_server.tools.statistics_tool import (
    min_value, max_value, sum_values, count_values, range_values,
    variance, mode, percentile, quartiles, iqr, 
    geometric_mean, harmonic_mean
)
from src.mcp_server.models.schemas import StatisticsInput

@pytest.mark.asyncio
async def test_min_value():
    input_data = StatisticsInput(data=[5, 2, 8, 1, 9])
    result = await min_value(input_data)
    assert result == 1

@pytest.mark.asyncio
async def test_max_value():
    input_data = StatisticsInput(data=[5, 2, 8, 1, 9])
    result = await max_value(input_data)
    assert result == 9

@pytest.mark.asyncio
async def test_sum_values():
    input_data = StatisticsInput(data=[1, 2, 3, 4, 5])
    result = await sum_values(input_data)
    assert result == 15

@pytest.mark.asyncio
async def test_count_values():
    input_data = StatisticsInput(data=[1, 2, 3, 4, 5])
    result = await count_values(input_data)
    assert result == 5

@pytest.mark.asyncio
async def test_range_values():
    input_data = StatisticsInput(data=[1, 5, 3, 9, 2])
    result = await range_values(input_data)
    assert result == 8

@pytest.mark.asyncio
async def test_variance():
    input_data = StatisticsInput(data=[1, 2, 3, 4, 5])
    result = await variance(input_data)
    assert result == pytest.approx(2.5)

@pytest.mark.asyncio
async def test_variance_single_value_raises():
    input_data = StatisticsInput(data=[42])
    with pytest.raises(ValueError, match="Variance requires at least 2 data points"):
        await variance(input_data)

@pytest.mark.asyncio
async def test_mode_single_mode():
    input_data = StatisticsInput(data=[1, 2, 2, 3, 2, 4])
    result = await mode(input_data)
    assert result == 2

@pytest.mark.asyncio
async def test_mode_multiple_modes():
    input_data = StatisticsInput(data=[1, 1, 2, 2, 3])
    result = await mode(input_data)
    # Multiple modes should return a list or the first mode
    assert result in ([1.0, 2.0], [1, 2], 1.0, 1)

@pytest.mark.asyncio
async def test_percentile_25th():
    input_data = StatisticsInput(data=[1, 2, 3, 4, 5])
    result = await percentile(input_data, 25)
    assert result == pytest.approx(2.0)

@pytest.mark.asyncio
async def test_percentile_50th():
    input_data = StatisticsInput(data=[1, 2, 3, 4, 5])
    result = await percentile(input_data, 50)
    assert result == pytest.approx(3.0)

@pytest.mark.asyncio
async def test_percentile_75th():
    input_data = StatisticsInput(data=[1, 2, 3, 4, 5])
    result = await percentile(input_data, 75)
    assert result == pytest.approx(4.0)

@pytest.mark.asyncio
async def test_percentile_0th():
    input_data = StatisticsInput(data=[1, 2, 3, 4, 5])
    result = await percentile(input_data, 0)
    assert result == 1

@pytest.mark.asyncio
async def test_percentile_100th():
    input_data = StatisticsInput(data=[1, 2, 3, 4, 5])
    result = await percentile(input_data, 100)
    assert result == 5

@pytest.mark.asyncio
async def test_percentile_invalid_raises():
    input_data = StatisticsInput(data=[1, 2, 3])
    with pytest.raises(ValueError, match="Percentile must be between 0 and 100"):
        await percentile(input_data, 101)

@pytest.mark.asyncio
async def test_quartiles():
    input_data = StatisticsInput(data=[1, 2, 3, 4, 5, 6, 7, 8])
    result = await quartiles(input_data)
    assert "Q1" in result
    assert "Q2" in result
    assert "Q3" in result
    assert result["Q1"] == pytest.approx(2.75)
    assert result["Q2"] == pytest.approx(4.5)
    assert result["Q3"] == pytest.approx(6.25)

@pytest.mark.asyncio
async def test_iqr():
    input_data = StatisticsInput(data=[1, 2, 3, 4, 5, 6, 7, 8])
    result = await iqr(input_data)
    assert result == pytest.approx(3.5)

@pytest.mark.asyncio
async def test_geometric_mean():
    input_data = StatisticsInput(data=[2, 4, 8])
    result = await geometric_mean(input_data)
    assert result == pytest.approx(4.0)

@pytest.mark.asyncio
async def test_geometric_mean_negative_raises():
    input_data = StatisticsInput(data=[1, -2, 3])
    with pytest.raises(ValueError, match="Geometric mean requires all positive values"):
        await geometric_mean(input_data)

@pytest.mark.asyncio
async def test_harmonic_mean():
    input_data = StatisticsInput(data=[1, 2, 4])
    result = await harmonic_mean(input_data)
    assert result == pytest.approx(1.714285714)

@pytest.mark.asyncio
async def test_harmonic_mean_zero_raises():
    input_data = StatisticsInput(data=[1, 0, 3])
    with pytest.raises(ValueError, match="Harmonic mean requires all positive values"):
        await harmonic_mean(input_data)

@pytest.mark.asyncio
async def test_statistics_input_with_numbers_field():
    # Test that StatisticsInput works with 'numbers' field
    input_data = StatisticsInput(numbers=[1, 2, 3])
    assert input_data.data == [1, 2, 3]