import statistics

async def mean(input_data):
    """Calculate the arithmetic mean of a dataset."""
    return statistics.mean(input_data.data)

async def median(input_data):
    """Calculate the median of a dataset."""
    return statistics.median(input_data.data)

async def stddev(input_data):
    """Calculate the standard deviation of a dataset."""
    if len(input_data.data) < 2:
        raise ValueError("Standard deviation requires at least 2 data points")
    return statistics.stdev(input_data.data)