from src.mcp_server.prompts.geometry_calculation_prompt import geometry_calculation_prompt

def test_geometry_circle():
    prompt = geometry_calculation_prompt("circle", 5.0)
    assert "radius = 5.0" in prompt
    assert "Area calculation (A = πr²)" in prompt
    assert "power(5.0, 2)" in prompt
    assert "Circumference calculation (C = 2πr)" in prompt
    assert "multiply(two_pi, 5.0)" in prompt
    assert "sphere" in prompt.lower()
    assert "Volume (4/3 πr³)" in prompt

def test_geometry_triangle_base_height():
    prompt = geometry_calculation_prompt("triangle", 6.0, 4.0)
    assert "base=6.0" in prompt
    assert "height=4.0" in prompt
    assert "Area calculation (A = ½ × base × height)" in prompt
    assert "multiply(6.0, 4.0)" in prompt
    assert "divide(previous_result, 2)" in prompt
    assert "equilateral" in prompt.lower()
    assert "isosceles" in prompt.lower()

def test_geometry_triangle_three_sides():
    prompt = geometry_calculation_prompt("triangle", 3.0, 4.0, 5.0)
    assert "sides a=3.0, b=4.0, c=5.0" in prompt
    assert "Heron's formula" in prompt
    assert "semi-perimeter" in prompt
    assert "add(3.0, 4.0)" in prompt
    assert "right triangle" in prompt.lower()
    assert "Pythagorean theorem" in prompt

def test_geometry_rectangle():
    prompt = geometry_calculation_prompt("rectangle", 8.0, 6.0)
    assert "length=8.0" in prompt
    assert "width=6.0" in prompt
    assert "Area calculation (A = length × width)" in prompt
    assert "multiply(8.0, 6.0)" in prompt
    assert "Perimeter calculation (P = 2(length + width))" in prompt
    assert "Diagonal Analysis" in prompt  # Updated to match new structure
    assert "Pythagorean theorem" in prompt

def test_geometry_sphere():
    prompt = geometry_calculation_prompt("sphere", 7.0)
    assert "radius=7.0" in prompt
    assert "Surface area calculation (A = 4πr²)" in prompt
    assert "power(7.0, 2)" in prompt
    assert "Volume calculation (V = (4/3)πr³)" in prompt
    assert "power(7.0, 3)" in prompt
    assert "Great circle circumference" in prompt
    assert "multiply(two_pi, 7.0)" in prompt

def test_geometry_unknown_shape():
    prompt = geometry_calculation_prompt("hexagon", 5.0)
    assert "Geometric calculation for shape: hexagon" in prompt
    assert "Available shapes" in prompt
    assert "Circle: radius" in prompt
    assert "Triangle:" in prompt
    assert "Rectangle:" in prompt
    assert "Sphere:" in prompt

def test_geometry_contains_mcp_instructions():
    prompt = geometry_calculation_prompt("circle", 10.0)
    # Check for MCP tools instruction in various forms
    assert "USE MCP TOOLS" in prompt.upper() and "ALL CALCULATIONS" in prompt.upper()
    assert "multiply" in prompt
    assert "divide" in prompt
    assert "power" in prompt
    assert "root" in prompt
    
def test_geometry_pi_approximation():
    prompt = geometry_calculation_prompt("circle", 1.0)
    assert "3.14159" in prompt
    assert "π" in prompt or "pi" in prompt.lower()

def test_geometry_formulas_included():
    # Test circle formulas
    circle_prompt = geometry_calculation_prompt("circle", 2.0)
    assert "A = πr²" in circle_prompt
    assert "C = 2πr" in circle_prompt
    
    # Test triangle formulas
    triangle_prompt = geometry_calculation_prompt("triangle", 3.0, 4.0, 5.0)
    assert "Area = √[s(s-a)(s-b)(s-c)]" in triangle_prompt
    
    # Test rectangle formulas
    rectangle_prompt = geometry_calculation_prompt("rectangle", 5.0, 3.0)
    assert "A = length × width" in rectangle_prompt
    assert "P = 2(length + width)" in rectangle_prompt