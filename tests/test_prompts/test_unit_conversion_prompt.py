from src.mcp_server.prompts.unit_conversion_prompt import unit_conversion_prompt

def test_temperature_celsius_to_fahrenheit():
    prompt = unit_conversion_prompt("temperature", 25.0, "celsius", "fahrenheit")
    assert "25.0° celsius to fahrenheit" in prompt
    assert "PRIMARY PURPOSE" in prompt
    assert "Temperature Transformation" in prompt
    assert "multiply(25.0, 1.8)" in prompt
    assert "add(result, 32)" in prompt
    assert "Input Validation" in prompt
    assert "≥ -273.15°C" in prompt

def test_temperature_fahrenheit_to_celsius():
    prompt = unit_conversion_prompt("temperature", 77.0, "fahrenheit", "celsius")
    assert "77.0° fahrenheit to celsius" in prompt
    assert "subtract(77.0, 32)" in prompt
    assert "multiply(result, 0.5556)" in prompt
    assert "≥ -459.67°F" in prompt

def test_temperature_celsius_to_kelvin():
    prompt = unit_conversion_prompt("temperature", 0.0, "celsius", "kelvin")
    assert "0.0° celsius to kelvin" in prompt
    assert "add(0.0, 273.15)" in prompt
    assert "absolute temperature" in prompt.lower()

def test_temperature_kelvin_to_celsius():
    prompt = unit_conversion_prompt("temperature", 300.0, "kelvin", "celsius")
    assert "300.0° kelvin to celsius" in prompt
    assert "subtract(300.0, 273.15)" in prompt

def test_temperature_fahrenheit_to_kelvin():
    prompt = unit_conversion_prompt("temperature", 32.0, "fahrenheit", "kelvin")
    assert "32.0° fahrenheit to kelvin" in prompt
    assert "subtract(32.0, 32)" in prompt
    assert "add(result, 273.15)" in prompt

def test_temperature_kelvin_to_fahrenheit():
    prompt = unit_conversion_prompt("temperature", 273.15, "kelvin", "fahrenheit")
    assert "273.15° kelvin to fahrenheit" in prompt
    assert "subtract(273.15, 273.15)" in prompt
    assert "multiply(result, 1.8)" in prompt
    assert "add(result, 32)" in prompt

def test_length_conversion():
    prompt = unit_conversion_prompt("length", 1000.0, "meters", "kilometers")
    assert "Length/Distance Measurement" in prompt
    assert "1000.0 meters to kilometers" in prompt
    assert "Conversion Factor Selection" in prompt
    assert "Multi-step Conversion" in prompt
    assert "1 kilometer = 1000 meters" in prompt
    assert "multiply, divide" in prompt

def test_weight_mass_conversion():
    prompt = unit_conversion_prompt("mass", 5.0, "kilograms", "pounds")
    assert "Weight/Mass Measurement" in prompt
    assert "5.0 kilograms of mass/weight to pounds" in prompt
    assert "Unit System Identification" in prompt
    assert "2.20462 pounds" in prompt
    assert "Practical Context" in prompt

def test_speed_velocity_conversion():
    prompt = unit_conversion_prompt("speed", 60.0, "mph", "km/h")
    assert "Speed/Velocity Transformation" in prompt
    assert "60.0 mph to km/h" in prompt
    assert "Unit Decomposition" in prompt
    assert "Compound Units" in prompt
    assert "distance/time" in prompt.lower()
    assert "1.60934" in prompt

def test_volume_conversion():
    prompt = unit_conversion_prompt("volume", 4.0, "liters", "gallons")
    assert "Volume/Capacity Measurement" in prompt
    assert "4.0 liters to gallons" in prompt
    assert "System Classification" in prompt
    assert "Cross-system Bridge" in prompt
    assert "3.78541" in prompt

def test_general_conversion_guide():
    prompt = unit_conversion_prompt("energy", 100.0)
    assert "General Conversion Guide" in prompt
    assert "100.0 units in the energy category" in prompt
    assert "AVAILABLE CONVERSION CATEGORIES" in prompt
    assert "Temperature Conversions" in prompt
    assert "Length/Distance Conversions" in prompt
    assert "Weight/Mass Conversions" in prompt
    assert "Speed/Velocity Conversions" in prompt
    assert "Volume/Capacity Conversions" in prompt

def test_temperature_contains_reference_points():
    prompt = unit_conversion_prompt("temperature", 100.0, "celsius", "fahrenheit")
    assert "Water freezes: 0°C = 32°F = 273.15K" in prompt
    assert "Room temperature" in prompt
    assert "Body temperature" in prompt
    assert "Water boils" in prompt

def test_length_contains_conversion_factors():
    prompt = unit_conversion_prompt("length", 1.0)
    assert "1 kilometer = 1000 meters" in prompt
    assert "1 mile = 5280 feet" in prompt
    assert "1 inch = 2.54 centimeters" in prompt

def test_weight_contains_reference_objects():
    prompt = unit_conversion_prompt("weight", 1.0)
    assert "Paperclip: ~1 gram" in prompt
    assert "Liter of water: 1 kilogram" in prompt
    assert "Small car: ~1000 kilograms" in prompt

def test_speed_contains_reference_speeds():
    prompt = unit_conversion_prompt("velocity", 50.0)
    assert "Walking: ~5 km/h" in prompt
    assert "Highway: ~100 km/h" in prompt
    assert "Sound: ~343 m/s" in prompt

def test_volume_contains_practical_references():
    prompt = unit_conversion_prompt("volume", 1.0)
    assert "Teaspoon: ~5 ml" in prompt
    assert "Soda can: 355 ml" in prompt
    assert "Wine bottle: 750 ml" in prompt

def test_prompt_contains_mcp_instructions():
    prompt = unit_conversion_prompt("temperature", 20.0, "celsius", "fahrenheit")
    assert "MCP tools" in prompt
    assert "multiply" in prompt or "divide" in prompt
    assert "Execution Instructions" in prompt

def test_prompt_contains_goals_structure():
    prompt = unit_conversion_prompt("length", 100.0, "meters", "feet")
    assert "🎯 PRIMARY PURPOSE" in prompt
    assert "📊 MAIN GOALS" in prompt
    assert "🔍 SUB-GOALS AND APPROACH" in prompt
    assert "Goal 1:" in prompt
    assert "**Objective**:" in prompt
    assert "**Why**:" in prompt

def test_prompt_contains_verification_steps():
    prompt = unit_conversion_prompt("temperature", 0.0, "celsius", "fahrenheit")
    assert "Result Verification" in prompt
    assert "Verification" in prompt
    assert "validate" in prompt.lower() or "verify" in prompt.lower()

def test_weight_conversion_alias():
    # Test that "weight" works as alias for "mass"
    prompt = unit_conversion_prompt("weight", 10.0, "kg", "lbs")
    assert "Weight/Mass Measurement" in prompt
    assert "10.0 kg of mass/weight to lbs" in prompt