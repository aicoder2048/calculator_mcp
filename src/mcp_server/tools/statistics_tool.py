import statistics
from typing import List, Optional, Union
from collections import Counter

# 基础描述性统计
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

async def min_value(input_data):
    """Find the minimum value in a dataset."""
    return min(input_data.data)

async def max_value(input_data):
    """Find the maximum value in a dataset."""
    return max(input_data.data)

async def sum_values(input_data):
    """Calculate the sum of all values in a dataset."""
    return sum(input_data.data)

async def count_values(input_data):
    """Count the number of values in a dataset."""
    return len(input_data.data)

async def range_values(input_data):
    """Calculate the range (max - min) of a dataset."""
    return max(input_data.data) - min(input_data.data)

async def variance(input_data):
    """Calculate the variance of a dataset."""
    if len(input_data.data) < 2:
        raise ValueError("Variance requires at least 2 data points")
    return statistics.variance(input_data.data)

async def mode(input_data):
    """Find the mode(s) of a dataset. Returns a list for multiple modes."""
    try:
        # Try to get single mode
        return statistics.mode(input_data.data)
    except statistics.StatisticsError:
        # Multiple modes exist, calculate them manually
        counter = Counter(input_data.data)
        max_count = max(counter.values())
        modes = [value for value, count in counter.items() if count == max_count]
        return modes if len(modes) > 1 else modes[0]

# 分位数相关统计
async def percentile(input_data, p: float):
    """Calculate the pth percentile of a dataset."""
    if not 0 <= p <= 100:
        raise ValueError("Percentile must be between 0 and 100")
    if p == 0:
        return min(input_data.data)
    elif p == 100:
        return max(input_data.data)
    else:
        sorted_data = sorted(input_data.data)
        n = len(sorted_data)
        k = (n - 1) * p / 100
        f = int(k)
        c = k - f
        if f + 1 < n:
            return sorted_data[f] + c * (sorted_data[f + 1] - sorted_data[f])
        else:
            return sorted_data[f]

async def quartiles(input_data):
    """Calculate the quartiles (Q1, Q2, Q3) of a dataset."""
    sorted_data = sorted(input_data.data)
    n = len(sorted_data)
    
    # Q1 (25th percentile)
    q1_idx = (n - 1) * 0.25
    q1 = sorted_data[int(q1_idx)] + (q1_idx % 1) * (sorted_data[min(int(q1_idx) + 1, n - 1)] - sorted_data[int(q1_idx)])
    
    # Q2 (median, 50th percentile)
    q2 = statistics.median(sorted_data)
    
    # Q3 (75th percentile)
    q3_idx = (n - 1) * 0.75
    q3 = sorted_data[int(q3_idx)] + (q3_idx % 1) * (sorted_data[min(int(q3_idx) + 1, n - 1)] - sorted_data[int(q3_idx)])
    
    return {
        "Q1": q1,
        "Q2": q2,
        "Q3": q3
    }

async def iqr(input_data):
    """Calculate the interquartile range (Q3 - Q1) of a dataset."""
    q_data = await quartiles(input_data)
    return q_data["Q3"] - q_data["Q1"]

# 特殊平均值
async def geometric_mean(input_data):
    """Calculate the geometric mean of a dataset."""
    if any(x <= 0 for x in input_data.data):
        raise ValueError("Geometric mean requires all positive values")
    return statistics.geometric_mean(input_data.data)

async def harmonic_mean(input_data):
    """Calculate the harmonic mean of a dataset."""
    if any(x <= 0 for x in input_data.data):
        raise ValueError("Harmonic mean requires all positive values")
    return statistics.harmonic_mean(input_data.data)