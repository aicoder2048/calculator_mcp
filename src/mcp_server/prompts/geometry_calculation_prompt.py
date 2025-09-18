def geometry_calculation_prompt(shape: str, dimension1: float, dimension2: float = None, dimension3: float = None) -> str:
    """Generate a prompt for geometric calculations with step-by-step MCP tool usage."""
    
    shape_lower = shape.lower()
    
    if shape_lower == "circle":
        return f"""## Geometric Calculation Task: Circle Analysis

### 🎯 PRIMARY PURPOSE
Calculate all geometric properties of a circle with radius = {dimension1} using MCP mathematical tools to demonstrate precise computational methods.

### 📊 MAIN GOALS
1. **Basic Circle Metrics** - Compute fundamental circle measurements
2. **Extended Properties** - Calculate related geometric values
3. **3D Extension** - Explore sphere properties with same radius
4. **Verification** - Validate calculations through relationships

### 🔍 SUB-GOALS AND APPROACH

#### Goal 1: Basic Circle Metrics
**Objective**: Calculate area, circumference, and diameter
**Why**: These are fundamental properties needed for any circle-related problem

**Step 1.1**: Area calculation (A = πr²)
   - Purpose: Find the total space enclosed by the circle
   - Calculate r²: power({dimension1}, 2)
   - Use π ≈ 3.14159
   - Calculate area: multiply(3.14159, r_squared)
   - Expected outcome: Area in square units

**Step 1.2**: Circumference calculation (C = 2πr)
   - Purpose: Find the perimeter/boundary length
   - Calculate 2π: multiply(2, 3.14159)
   - Calculate circumference: multiply(two_pi, {dimension1})
   - Expected outcome: Linear distance around the circle

**Step 1.3**: Diameter calculation
   - Purpose: Find the longest distance across the circle
   - Simply: multiply(2, {dimension1})
   - Expected outcome: Maximum width of the circle

#### Goal 2: 3D Extension - Sphere Properties
**Objective**: Extend to 3-dimensional space with same radius
**Why**: Many practical applications involve spherical objects

**Step 2.1**: Surface area (4πr²)
   - Purpose: Total area covering the sphere surface
   - Method: multiply(4, multiply(3.14159, power({dimension1}, 2)))
   - Relationship: Exactly 4 times the circle area

**Step 2.2**: Volume (4/3 πr³)
   - Purpose: Total space enclosed by the sphere
   - Calculate r³: power({dimension1}, 3)
   - Calculate 4/3: divide(4, 3)
   - Calculate volume: multiply(four_thirds, multiply(3.14159, r_cubed))
   - Expected outcome: Cubic units of space

#### Goal 3: Verification
**Objective**: Validate calculations through known relationships
- Check: Sphere surface area = 4 × Circle area
- Check: Diameter = 2 × Radius
- Check: Circumference/Diameter = π

### 📐 Formula Reference
- Circle area: A = πr²
- Circle circumference: C = 2πr
- Sphere surface area: A = 4πr²
- Sphere volume: V = (4/3)πr³

### ⚙️ Execution Instructions
Please use MCP tools (add, subtract, multiply, divide, power, root) for ALL calculations.
Follow the steps sequentially, using the output of each step as needed for subsequent calculations."""

    elif shape_lower == "triangle":
        if dimension3 is not None:
            # Three sides provided - use Heron's formula
            a, b, c = dimension1, dimension2, dimension3
            return f"""## Geometric Calculation Task: Triangle Analysis (Three Sides)

### 🎯 PRIMARY PURPOSE
Analyze a triangle with sides a={a}, b={b}, c={c} using Heron's formula and validate its properties through MCP calculations.

### 📊 MAIN GOALS
1. **Basic Measurements** - Calculate perimeter and area
2. **Triangle Classification** - Determine triangle type
3. **Validation** - Verify triangle inequality and special properties
4. **Advanced Properties** - Calculate heights and angles (if needed)

### 🔍 SUB-GOALS AND APPROACH

#### Goal 1: Basic Triangle Metrics
**Objective**: Calculate fundamental triangle properties
**Why**: Essential for understanding the triangle's size and shape

**Step 1.1**: Perimeter calculation
   - Purpose: Find total boundary length
   - Method: add({a}, {b}) then add(result, {c})
   - Expected outcome: Total perimeter = {a} + {b} + {c}

**Step 1.2**: Area calculation using Heron's formula
   - Purpose: Find the enclosed area without needing height
   - **Phase 1 - Semi-perimeter**:
     - Calculate total: add({a}, add({b}, {c}))
     - Find s: divide(perimeter, 2)
     - Why: Semi-perimeter is the key to Heron's formula
   
   - **Phase 2 - Differences**:
     - Calculate (s-a): subtract(s, {a})
     - Calculate (s-b): subtract(s, {b})
     - Calculate (s-c): subtract(s, {c})
     - Why: These represent the "excess" of semi-perimeter over each side
   
   - **Phase 3 - Area computation**:
     - Multiply factors: multiply(s, s_minus_a) → Product1
     - Continue: multiply(Product1, s_minus_b) → Product2
     - Final product: multiply(Product2, s_minus_c) → Product3
     - Extract area: root(Product3, 2)
     - Expected outcome: Area in square units

#### Goal 2: Triangle Classification
**Objective**: Determine the type of triangle
**Why**: Different triangle types have unique properties and applications

**Step 2.1**: Check for right triangle (Pythagorean theorem)
   - Purpose: Identify if one angle is 90°
   - Calculate: power({a}, 2) → a_squared
   - Calculate: power({b}, 2) → b_squared
   - Calculate: power({c}, 2) → c_squared
   - Test: Does add(a_squared, b_squared) = c_squared?
   - Significance: Right triangles have special trigonometric properties

**Step 2.2**: Check for equilateral/isosceles
   - Purpose: Identify symmetry in the triangle
   - Check if any two sides are equal
   - Equilateral: All three sides equal
   - Isosceles: Two sides equal

#### Goal 3: Validation
**Objective**: Ensure the triangle is valid
**Why**: Three sides must satisfy the triangle inequality

- Check: {a} + {b} > {c}
- Check: {b} + {c} > {a}
- Check: {a} + {c} > {b}

### 📐 Formula Reference
- Heron's formula: Area = √[s(s-a)(s-b)(s-c)] where s = (a+b+c)/2
- Pythagorean theorem: a² + b² = c² (for right triangles)
- Triangle inequality: Sum of any two sides > third side

### ⚙️ Execution Instructions
Please use MCP tools (add, subtract, multiply, divide, power, root) for ALL calculations.
Each calculation builds on previous results - maintain precision throughout."""
        else:
            # Base and height provided
            base, height = dimension1, dimension2
            return f"""Calculate triangle geometry with base={base}, height={height}:

Instructions - Use MCP tools for all calculations:

1. Area calculation (A = ½ × base × height):
   - Step 1: multiply({base}, {height})
   - Step 2: divide(previous_result, 2)

2. If this is an equilateral triangle with side={base}:
   - Perimeter: multiply(3, {base})
   - Height verification: multiply({base}, divide(root(3, 2), 2))
   - Area using side: multiply(divide(root(3, 2), 4), power({base}, 2))

3. If this is an isosceles triangle:
   - Half base: divide({base}, 2)
   - Slant height using Pythagorean theorem:
     - Calculate: power(half_base, 2)
     - Calculate: power({height}, 2)
     - Slant height: root(add(half_base_squared, height_squared), 2)

Formula reminders:
- Triangle area: A = ½ × base × height
- Equilateral triangle area: A = (√3/4) × side²
- Pythagorean theorem: c² = a² + b²

Please use MCP tools for ALL calculations."""

    elif shape_lower == "rectangle":
        length, width = dimension1, dimension2
        return f"""## Geometric Calculation Task: Rectangle Analysis

### 🎯 PRIMARY PURPOSE
Analyze a rectangle with length={length} and width={width}, computing all essential properties using MCP mathematical tools.

### 📊 MAIN GOALS
1. **Basic Properties** - Calculate area and perimeter
2. **Diagonal Analysis** - Compute diagonal length using Pythagorean theorem
3. **3D Extension** - Explore rectangular prism properties
4. **Relationships** - Verify geometric relationships

### 🔍 SUB-GOALS AND APPROACH

#### Goal 1: Fundamental Rectangle Metrics
**Objective**: Calculate basic rectangular properties
**Why**: These are the foundation for all rectangle-related problems

**Step 1.1**: Area calculation (A = length × width)
   - Purpose: Find the total surface enclosed by the rectangle
   - Method: multiply({length}, {width})
   - Expected outcome: Area = {length} × {width} square units
   - Significance: Represents the 2D space covered

**Step 1.2**: Perimeter calculation (P = 2(length + width))
   - Purpose: Find the total boundary length
   - Phase 1: add({length}, {width}) → semi-perimeter
   - Phase 2: multiply(2, semi-perimeter) → full perimeter
   - Expected outcome: Total distance around rectangle
   - Application: Fencing, border calculations

#### Goal 2: Diagonal Analysis
**Objective**: Calculate the diagonal using Pythagorean theorem
**Why**: The diagonal is the longest distance within the rectangle

**Step 2.1**: Apply Pythagorean theorem (d = √(length² + width²))
   - Purpose: Find the distance from corner to opposite corner
   - Calculate length²: power({length}, 2)
   - Calculate width²: power({width}, 2)
   - Sum squares: add(length_squared, width_squared)
   - Extract diagonal: root(sum_of_squares, 2)
   - Significance: Maximum internal distance

#### Goal 3: 3D Extension - Rectangular Prism
**Objective**: Explore properties if extended to 3D with height h
**Why**: Many real-world applications involve boxes and rooms

**Step 3.1**: Volume calculation (if height h is given)
   - Purpose: Find 3D space enclosed
   - Method: multiply(area, h)
   - Represents: Capacity of a box

**Step 3.2**: Surface area calculation
   - Purpose: Total area of all six faces
   - Formula: 2(lw + lh + wh)
   - Breakdown: 
     - Top/bottom: 2 × multiply({length}, {width})
     - Front/back: 2 × multiply({length}, h)
     - Left/right: 2 × multiply({width}, h)

#### Goal 4: Verification
**Objective**: Validate calculations through relationships
- Check: Diagonal > length and diagonal > width
- Check: Perimeter = 2 × (length + width)
- Check: For square (length = width), diagonal = length × √2

### 📐 Formula Reference
- Rectangle area: A = length × width
- Rectangle perimeter: P = 2(length + width)
- Diagonal: d = √(length² + width²)
- Rectangular prism volume: V = l × w × h
- Rectangular prism surface area: SA = 2(lw + lh + wh)

### ⚙️ Execution Instructions
Please use MCP tools (add, subtract, multiply, divide, power, root) for ALL calculations.
Maintain precision and use previous results where applicable."""

    elif shape_lower == "sphere":
        radius = dimension1
        return f"""## Geometric Calculation Task: Sphere Analysis

### 🎯 PRIMARY PURPOSE
Analyze a sphere with radius={radius}, calculating all fundamental 3D properties using MCP mathematical tools.

### 📊 MAIN GOALS
1. **Surface Area** - Calculate the outer boundary area
2. **Volume** - Compute the enclosed 3D space
3. **Related Metrics** - Great circle, diameter
4. **Cross-dimensional Relations** - Compare with 2D circle

### 🔍 SUB-GOALS AND APPROACH

#### Goal 1: Surface Area Calculation
**Objective**: Calculate the total surface area of the sphere
**Why**: Critical for material requirements, heat transfer, and coating applications

**Step 1.1**: Surface area calculation (A = 4πr²)
   - Purpose: Find total outer surface of the sphere
   - Phase 1: Calculate r²: power({radius}, 2)
   - Phase 2: Calculate 4π: multiply(4, 3.14159)
   - Phase 3: Calculate surface area: multiply(four_pi, r_squared)
   - Expected outcome: Total surface area in square units
   - Insight: This is exactly 4 times the area of its great circle

#### Goal 2: Volume Calculation
**Objective**: Compute the 3D space enclosed by the sphere
**Why**: Essential for capacity, mass, and density calculations

**Step 2.1**: Volume calculation (V = (4/3)πr³)
   - Purpose: Find total space contained within the sphere
   - Phase 1: Calculate r³: power({radius}, 3)
   - Phase 2: Calculate 4/3: divide(4, 3) ≈ 1.3333
   - Phase 3: Calculate π × r³: multiply(3.14159, r_cubed)
   - Phase 4: Final volume: multiply(four_thirds, pi_r_cubed)
   - Expected outcome: Volume in cubic units
   - Application: Container capacity, material volume

#### Goal 3: Related Metrics
**Objective**: Calculate additional useful measurements
**Why**: These metrics are often needed in practical applications

**Step 3.1**: Great circle circumference (C = 2πr)
   - Purpose: Find the perimeter of the largest circle on the sphere
   - Method: Calculate 2π: multiply(2, 3.14159)
   - Result: multiply(two_pi, {radius})
   - Significance: Equatorial distance, orbital paths

**Step 3.2**: Diameter calculation
   - Purpose: Maximum distance through the sphere
   - Method: multiply(2, {radius})
   - Application: Clearance requirements, fitting through openings

#### Goal 4: Cross-dimensional Verification
**Objective**: Relate sphere to 2D circle properties
**Why**: Validates calculations and provides intuitive understanding

**Relationships to verify**:
- Surface area = 4 × (area of great circle)
- Great circle has same circumference as 2D circle with radius={radius}
- Volume formula contains 4/3 factor (not present in 2D)

### 📐 Formula Reference
- Sphere surface area: A = 4πr²
- Sphere volume: V = (4/3)πr³
- Great circle: C = 2πr
- Diameter: d = 2r
- π ≈ 3.14159

### 🔬 Interesting Facts
- Surface area to volume ratio: 3/r (decreases as sphere grows)
- Sphere has minimum surface area for given volume
- All points on surface are equidistant from center

### ⚙️ Execution Instructions
Please use MCP tools (add, subtract, multiply, divide, power, root) for ALL calculations.
Follow the sequential steps, using each result to build toward the final answer."""

    else:
        return f"""Geometric calculation for shape: {shape}

Available shapes and required dimensions:
- Circle: radius
- Triangle: (base, height) OR (side1, side2, side3)
- Rectangle: length, width
- Sphere: radius

Please specify:
- Shape: {shape}
- Dimension 1: {dimension1}
- Dimension 2: {dimension2 if dimension2 else "not provided"}
- Dimension 3: {dimension3 if dimension3 else "not provided"}

General geometric formulas that can be calculated with MCP tools:
- Areas: Use multiply() for products, divide() for fractions
- Perimeters: Use add() for sums
- Volumes: Use power() for exponents, multiply() for products
- Diagonals/distances: Use root() for square roots, power() for squares
- π calculations: Use 3.14159 as approximation

Please use MCP tools (add, subtract, multiply, divide, power, root) for ALL calculations."""