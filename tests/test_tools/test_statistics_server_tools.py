import pytest
from src.mcp_server.tools.statistics_tool import (
    min_value, max_value, sum_values, count_values, range_values,
    variance, mode, percentile, quartiles, iqr,
    geometric_mean, harmonic_mean
)
from src.mcp_server.models.schemas import StatisticsInput

@pytest.mark.asyncio
async def test_server_min_value():
    input_data = StatisticsInput(data=[5, 2, 8, 1, 9])
    result = await min_value(input_data)
    assert result == 1

@pytest.mark.asyncio
async def test_server_max_value():
    input_data = StatisticsInput(data=[5, 2, 8, 1, 9])
    result = await max_value(input_data)
    assert result == 9

@pytest.mark.asyncio
async def test_server_sum():
    input_data = StatisticsInput(data=[1, 2, 3, 4, 5])
    result = await sum_values(input_data)
    assert result == 15

@pytest.mark.asyncio
async def test_server_count():
    input_data = StatisticsInput(data=[1, 2, 3, 4, 5])
    result = await count_values(input_data)
    assert result == 5

@pytest.mark.asyncio
async def test_server_range_stat():
    input_data = StatisticsInput(data=[1, 5, 3, 9, 2])
    result = await range_values(input_data)
    assert result == 8

@pytest.mark.asyncio
async def test_server_variance():
    input_data = StatisticsInput(data=[1, 2, 3, 4, 5])
    result = await variance(input_data)
    assert result == pytest.approx(2.5)

@pytest.mark.asyncio
async def test_server_variance_error():
    input_data = StatisticsInput(data=[42])
    with pytest.raises(ValueError, match="Variance requires at least 2 data points"):
        await variance(input_data)

@pytest.mark.asyncio
async def test_server_mode_single():
    input_data = StatisticsInput(data=[1, 2, 2, 3, 2, 4])
    result = await mode(input_data)
    assert result == 2

@pytest.mark.asyncio
async def test_server_mode_multiple():
    input_data = StatisticsInput(data=[1, 1, 2, 2, 3])
    result = await mode(input_data)
    # Multiple modes can return first mode or list
    assert result in ([1.0, 2.0], [1, 2], 1.0, 1, 2.0, 2)

@pytest.mark.asyncio
async def test_server_percentile():
    input_data = StatisticsInput(data=[1, 2, 3, 4, 5])
    result = await percentile(input_data, 50)
    assert result == pytest.approx(3.0)

@pytest.mark.asyncio
async def test_server_percentile_edge_cases():
    input_data = StatisticsInput(data=[1, 2, 3, 4, 5])
    # Test 0th percentile
    result = await percentile(input_data, 0)
    assert result == 1
    
    # Test 100th percentile  
    result = await percentile(input_data, 100)
    assert result == 5

@pytest.mark.asyncio
async def test_server_percentile_validation():
    input_data = StatisticsInput(data=[1, 2, 3])
    with pytest.raises(ValueError, match="Percentile must be between 0 and 100"):
        await percentile(input_data, 101)

@pytest.mark.asyncio
async def test_server_quartiles():
    input_data = StatisticsInput(data=[1, 2, 3, 4, 5, 6, 7, 8])
    result = await quartiles(input_data)
    assert "Q1" in result
    assert "Q2" in result 
    assert "Q3" in result
    assert isinstance(result["Q1"], (int, float))
    assert isinstance(result["Q2"], (int, float))
    assert isinstance(result["Q3"], (int, float))

@pytest.mark.asyncio
async def test_server_iqr():
    input_data = StatisticsInput(data=[1, 2, 3, 4, 5, 6, 7, 8])
    result = await iqr(input_data)
    assert isinstance(result, (int, float))
    assert result > 0

@pytest.mark.asyncio
async def test_server_geometric_mean():
    input_data = StatisticsInput(data=[2, 4, 8])
    result = await geometric_mean(input_data)
    assert result == pytest.approx(4.0)

@pytest.mark.asyncio
async def test_server_geometric_mean_validation():
    input_data = StatisticsInput(data=[1, -2, 3])
    with pytest.raises(ValueError, match="Geometric mean requires all positive values"):
        await geometric_mean(input_data)

@pytest.mark.asyncio
async def test_server_harmonic_mean():
    input_data = StatisticsInput(data=[1, 2, 4])
    result = await harmonic_mean(input_data)
    assert result == pytest.approx(1.714285714)

@pytest.mark.asyncio
async def test_server_harmonic_mean_validation():
    input_data = StatisticsInput(data=[1, 0, 3])
    with pytest.raises(ValueError, match="Harmonic mean requires all positive values"):
        await harmonic_mean(input_data)

@pytest.mark.asyncio
async def test_server_tools_with_empty_list():
    # Most tools should reject empty lists due to StatisticsInput validation
    with pytest.raises(ValueError):
        StatisticsInput(data=[])

@pytest.mark.asyncio
async def test_server_tools_with_single_value():
    input_data = StatisticsInput(data=[42])
    # Tools that work with single values
    assert await min_value(input_data) == 42
    assert await max_value(input_data) == 42
    assert await sum_values(input_data) == 42
    assert await count_values(input_data) == 1
    assert await range_values(input_data) == 0
    
    # Tools that should handle single values appropriately
    single_quartiles = await quartiles(input_data)
    assert single_quartiles["Q1"] == 42
    assert single_quartiles["Q2"] == 42  
    assert single_quartiles["Q3"] == 42