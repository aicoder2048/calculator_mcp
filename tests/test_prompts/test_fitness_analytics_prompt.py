import pytest
from src.mcp_server.prompts.fitness_analytics_prompt import fitness_analytics_prompt

def test_fitness_analytics_steps_default():
    """Test steps analysis with default parameters."""
    result = fitness_analytics_prompt("steps")
    
    assert "Step Count Analysis" in result
    assert "weekly" in result
    assert "health monitoring" in result  # After replacement of underscores
    assert "mean(step_counts)" in result
    assert "variance(step_counts)" in result
    assert "percentile(step_counts" in result
    assert "8,000-10,000 steps" in result

def test_fitness_analytics_steps_custom_params():
    """Test steps analysis with custom parameters."""
    result = fitness_analytics_prompt("steps", "monthly", "weight_loss")
    
    assert "Step Count Analysis" in result
    assert "monthly" in result
    assert "weight loss" in result
    assert "10,000+ steps daily for calorie burn" in result
    assert "quartiles(step_counts)" in result

def test_fitness_analytics_calories():
    """Test calories analysis."""
    result = fitness_analytics_prompt("calories", "daily", "fitness_improvement")
    
    assert "Calorie Burn Analysis" in result
    assert "daily" in result
    assert "fitness improvement" in result
    assert "mean(calorie_burns)" in result
    assert "variance(calorie_burns)" in result
    assert "1,800-2,400 calories daily" in result

def test_fitness_analytics_heart_rate():
    """Test heart rate analysis."""
    result = fitness_analytics_prompt("heart_rate", "weekly", "athletic_training")
    
    assert "Heart Rate Analysis" in result
    assert "weekly" in result
    assert "athletic training" in result
    assert "mean(heart_rates)" in result
    assert "quartiles(heart_rates)" in result
    assert "cardiovascular health" in result
    assert "training zones" in result

def test_fitness_analytics_weight():
    """Test weight analysis."""
    result = fitness_analytics_prompt("weight", "monthly", "weight_loss")
    
    assert "Weight Progress Analysis" in result
    assert "monthly" in result
    assert "weight loss" in result
    assert "mean(weight_measurements)" in result
    assert "variance(weight_measurements)" in result
    assert "1-2 lb weekly loss" in result

def test_fitness_analytics_blood_pressure():
    """Test blood pressure analysis."""
    result = fitness_analytics_prompt("blood_pressure", "weekly", "health_monitoring")
    
    assert "Blood Pressure Monitoring" in result
    assert "weekly" in result
    assert "health monitoring" in result
    assert "mean(systolic_readings)" in result
    assert "mean(diastolic_readings)" in result
    assert "quartiles(systolic_readings)" in result
    assert "<120/80" in result
    assert "healthcare provider" in result

def test_fitness_analytics_unknown_metric():
    """Test with unknown metric type returns general guide."""
    result = fitness_analytics_prompt("unknown_metric")
    
    assert "Comprehensive Health Metrics Analysis" in result
    assert "steps" in result
    assert "calories" in result
    assert "heart_rate" in result
    assert "weight" in result
    assert "blood_pressure" in result

def test_fitness_analytics_all_time_periods():
    """Test all time period options."""
    periods = ["daily", "weekly", "monthly", "quarterly"]
    
    for period in periods:
        result = fitness_analytics_prompt("steps", period)
        assert period in result

def test_fitness_analytics_all_goal_types():
    """Test all goal type options."""
    goals = ["weight_loss", "fitness_improvement", "health_monitoring", "athletic_training"]
    
    for goal in goals:
        result = fitness_analytics_prompt("steps", "weekly", goal)
        # Replace underscores with spaces for display
        goal_display = goal.replace('_', ' ')
        assert goal_display in result

def test_fitness_analytics_statistical_tools_mentioned():
    """Test that statistical tools are mentioned in prompts."""
    metrics = ["steps", "calories", "heart_rate", "weight", "blood_pressure"]
    statistical_tools = [
        "mean", "variance", "stddev", "percentile", "quartiles", 
        "iqr", "mode", "min_value", "max_value", "range_stat"
    ]
    
    for metric in metrics:
        result = fitness_analytics_prompt(metric)
        # Each metric should mention multiple statistical tools
        mentioned_tools = [tool for tool in statistical_tools if tool in result]
        assert len(mentioned_tools) >= 5, f"Metric {metric} should mention at least 5 statistical tools"

def test_fitness_analytics_health_insights():
    """Test that health insights and recommendations are included."""
    result = fitness_analytics_prompt("heart_rate")
    
    # Should include health ranges and recommendations
    assert "60-100 bpm" in result or "resting HR" in result
    assert "optimization" in result.lower() or "strategies" in result.lower()
    assert "health" in result.lower()

def test_fitness_analytics_mcp_tool_instructions():
    """Test that MCP tool usage instructions are included."""
    result = fitness_analytics_prompt("weight")
    
    assert "MCP tools" in result
    assert "calculations" in result
    assert "Execution Instructions" in result

def test_fitness_analytics_goal_specific_content():
    """Test that goal-specific content is included."""
    # Weight loss goal should mention deficit
    weight_loss_result = fitness_analytics_prompt("calories", "weekly", "weight_loss")
    assert "deficit" in weight_loss_result.lower() or "weight loss" in weight_loss_result.lower()
    
    # Athletic training should mention performance
    athletic_result = fitness_analytics_prompt("heart_rate", "weekly", "athletic_training")
    assert "training" in athletic_result.lower() or "performance" in athletic_result.lower()
    
    # Health monitoring should mention stability
    health_result = fitness_analytics_prompt("blood_pressure", "weekly", "health_monitoring")
    assert "monitor" in health_result.lower() or "health" in health_result.lower()

def test_fitness_analytics_safety_considerations():
    """Test that safety and medical considerations are included."""
    bp_result = fitness_analytics_prompt("blood_pressure")
    hr_result = fitness_analytics_prompt("heart_rate")
    
    # Blood pressure should mention medical consultation
    assert "healthcare provider" in bp_result or "medical" in bp_result.lower()
    
    # Heart rate should mention health alerts
    assert "health" in hr_result.lower() and ("alert" in hr_result.lower() or "concern" in hr_result.lower())

def test_fitness_analytics_case_insensitive():
    """Test that function handles case variations."""
    # Test different cases
    result1 = fitness_analytics_prompt("STEPS")
    result2 = fitness_analytics_prompt("Steps")
    result3 = fitness_analytics_prompt("steps")
    
    # All should work and contain step analysis content
    for result in [result1, result2, result3]:
        assert "Step Count Analysis" in result

def test_fitness_analytics_parameter_combinations():
    """Test various parameter combinations."""
    combinations = [
        ("steps", "daily", "weight_loss"),
        ("calories", "monthly", "fitness_improvement"),
        ("heart_rate", "quarterly", "athletic_training"),
        ("weight", "weekly", "health_monitoring"),
        ("blood_pressure", "daily", "health_monitoring")
    ]
    
    for metric, period, goal in combinations:
        result = fitness_analytics_prompt(metric, period, goal)
        assert len(result) > 1000  # Should be substantial content
        # Check for metric name in various forms
        metric_found = (
            metric in result.lower() or 
            metric.title() in result or
            metric.replace('_', ' ').title() in result
        )
        assert metric_found, f"Metric {metric} not found in result"
        assert period in result
        assert goal.replace('_', ' ') in result