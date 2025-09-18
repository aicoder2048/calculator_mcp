def unit_conversion_prompt(conversion_type: str, value: float, from_unit: str = None, to_unit: str = None) -> str:
    """Generate a prompt for unit conversion calculations with detailed MCP tool usage."""
    
    conversion_lower = conversion_type.lower()
    
    if conversion_lower == "temperature":
        # Temperature conversions
        if from_unit and to_unit:
            from_lower = from_unit.lower()
            to_lower = to_unit.lower()
            
            return f"""## Unit Conversion Task: Temperature Transformation

### 🎯 PRIMARY PURPOSE
Convert {value}° {from_unit} to {to_unit} using precise mathematical formulas and MCP calculation tools.

### 📊 MAIN GOALS
1. **Input Validation** - Verify the temperature value is physically possible
2. **Formula Application** - Apply the correct conversion formula
3. **Result Verification** - Validate the output makes physical sense
4. **Reference Points** - Compare with known temperature benchmarks

### 🔍 SUB-GOALS AND APPROACH

#### Goal 1: Input Validation
**Objective**: Ensure the input temperature is physically valid
**Why**: Temperatures have absolute minimums that cannot be exceeded

**Validation checks**:
- Celsius: Must be ≥ -273.15°C (absolute zero)
- Fahrenheit: Must be ≥ -459.67°F (absolute zero)
- Kelvin: Must be ≥ 0 K (by definition)

#### Goal 2: Temperature Conversion
**Objective**: Apply the appropriate conversion formula
**Why**: Each temperature scale has a specific mathematical relationship

{_get_temperature_conversion_steps(from_lower, to_lower, value)}

#### Goal 3: Result Verification
**Objective**: Ensure the result is reasonable
**Why**: Catch calculation errors and validate physical plausibility

**Verification steps**:
- Check result is above absolute zero in target scale
- Compare with reference points (water freezing/boiling)
- Verify reverse conversion returns to original value

#### Goal 4: Reference Context
**Objective**: Provide context for the converted temperature
**Why**: Helps understand the practical meaning of the result

**Common reference points**:
- Water freezes: 0°C = 32°F = 273.15K
- Room temperature: ~20°C = ~68°F = ~293K
- Body temperature: 37°C = 98.6°F = 310.15K
- Water boils: 100°C = 212°F = 373.15K

### 📐 Formula Reference
- Celsius to Fahrenheit: F = (C × 9/5) + 32
- Fahrenheit to Celsius: C = (F - 32) × 5/9
- Celsius to Kelvin: K = C + 273.15
- Kelvin to Celsius: C = K - 273.15
- Fahrenheit to Kelvin: K = (F - 32) × 5/9 + 273.15
- Kelvin to Fahrenheit: F = (K - 273.15) × 9/5 + 32

### ⚙️ Execution Instructions
Please use MCP tools (add, subtract, multiply, divide) for ALL calculations.
Break down complex formulas into simple steps for accuracy."""
        
    elif conversion_lower == "length":
        return f"""## Unit Conversion Task: Length/Distance Measurement

### 🎯 PRIMARY PURPOSE
Convert {value} {from_unit if from_unit else 'units'} to {to_unit if to_unit else 'target units'} using standard conversion factors and MCP tools.

### 📊 MAIN GOALS
1. **Conversion Factor Selection** - Identify the correct conversion multiplier
2. **Multi-step Conversion** - Handle conversions through intermediate units
3. **Precision Management** - Maintain appropriate decimal precision
4. **Practical Context** - Relate to real-world applications

### 🔍 SUB-GOALS AND APPROACH

#### Goal 1: Direct Conversion Path
**Objective**: Find the most efficient conversion route
**Why**: Minimize rounding errors and calculation steps

**Common conversion factors**:
- 1 kilometer = 1000 meters
- 1 meter = 100 centimeters
- 1 meter = 1000 millimeters
- 1 mile = 1.60934 kilometers
- 1 mile = 5280 feet
- 1 foot = 12 inches
- 1 inch = 2.54 centimeters
- 1 yard = 3 feet = 0.9144 meters

**Step 1.1**: Identify conversion type
- Metric to Metric: Simple power of 10
- Imperial to Imperial: Use defined ratios
- Metric to Imperial: Use precise conversion factors

**Step 1.2**: Calculate conversion
- For {value} {from_unit if from_unit else 'units'}:
- Method: multiply({value}, conversion_factor)
- Or for reverse: divide({value}, conversion_factor)

#### Goal 2: Multi-step Conversions
**Objective**: Handle complex conversions requiring intermediate steps
**Why**: Some units don't have direct conversion factors

**Example: Kilometers to Inches**
- Step 1: km to meters: multiply({value}, 1000)
- Step 2: meters to cm: multiply(result, 100)
- Step 3: cm to inches: divide(result, 2.54)

#### Goal 3: Precision and Rounding
**Objective**: Maintain appropriate precision
**Why**: Different applications require different accuracy levels

**Guidelines**:
- Engineering: 4-6 significant figures
- Construction: 2-3 decimal places
- Everyday use: Round to practical values

#### Goal 4: Verification
**Objective**: Validate the conversion makes sense
**Why**: Catch errors in conversion factor or calculation

**Verification methods**:
- Magnitude check: Is the result in the expected range?
- Reverse conversion: Does it return to original value?
- Reference comparison: Compare with known equivalents

### 📏 Common Length Conversions
**Metric chain**:
km → m (×1000) → cm (×100) → mm (×10)

**Imperial chain**:
miles → yards (×1760) → feet (×3) → inches (×12)

**Cross-system**:
- 1 meter ≈ 3.28084 feet
- 1 kilometer ≈ 0.621371 miles
- 1 inch = exactly 2.54 cm

### ⚙️ Execution Instructions
Please use MCP tools (multiply, divide) for ALL conversions.
Show each step explicitly when doing multi-step conversions."""
        
    elif conversion_lower == "weight" or conversion_lower == "mass":
        return f"""## Unit Conversion Task: Weight/Mass Measurement

### 🎯 PRIMARY PURPOSE
Convert {value} {from_unit if from_unit else 'units'} of mass/weight to {to_unit if to_unit else 'target units'} using standard conversion factors.

### 📊 MAIN GOALS
1. **Unit System Identification** - Determine metric, imperial, or other systems
2. **Conversion Calculation** - Apply appropriate conversion factors
3. **Precision Handling** - Maintain accuracy for the use case
4. **Context Provision** - Relate to familiar objects

### 🔍 SUB-GOALS AND APPROACH

#### Goal 1: Mass Unit Relationships
**Objective**: Understand the relationship between units
**Why**: Essential for accurate conversion

**Metric System (Base: kilogram)**:
- 1 metric ton (tonne) = 1000 kilograms
- 1 kilogram = 1000 grams
- 1 gram = 1000 milligrams
- 1 milligram = 1000 micrograms

**Imperial/US System**:
- 1 ton (US) = 2000 pounds
- 1 ton (UK) = 2240 pounds
- 1 pound = 16 ounces
- 1 ounce = 28.3495 grams

**Step 1.1**: Calculate using conversion factor
- Input: {value} {from_unit if from_unit else 'units'}
- Identify factor: [specific to conversion]
- Calculate: multiply({value}, factor) or divide({value}, factor)

#### Goal 2: Cross-System Conversions
**Objective**: Convert between metric and imperial
**Why**: Different regions use different systems

**Key conversion bridges**:
- 1 kilogram = 2.20462 pounds
- 1 pound = 0.453592 kilograms
- 1 ounce = 28.3495 grams
- 1 gram = 0.0353 ounces

**Step 2.1**: Multi-step conversion if needed
- Convert to common unit first (usually kg or g)
- Then convert to target unit
- Example: ounces → grams → kilograms

#### Goal 3: Practical Context
**Objective**: Provide relatable comparisons
**Why**: Helps visualize the mass/weight

**Reference objects**:
- Paperclip: ~1 gram
- AA battery: ~23 grams
- Smartphone: ~150-200 grams
- Liter of water: 1 kilogram
- Average adult: 60-80 kilograms
- Small car: ~1000 kilograms (1 tonne)

#### Goal 4: Verification
**Objective**: Ensure conversion accuracy
**Why**: Prevent order-of-magnitude errors

**Checks**:
- Direction: Did value increase/decrease as expected?
- Magnitude: Is the result reasonable?
- Reversibility: Can you convert back to original?

### 📊 Conversion Strategy
1. Identify source and target unit systems
2. Find direct conversion factor if available
3. Otherwise, convert through intermediate unit
4. Apply MCP tools for calculation
5. Verify result makes sense

### ⚙️ Execution Instructions
Please use MCP tools (multiply, divide) for ALL calculations.
For complex conversions, show intermediate steps clearly."""
        
    elif conversion_lower == "speed" or conversion_lower == "velocity":
        return f"""## Unit Conversion Task: Speed/Velocity Transformation

### 🎯 PRIMARY PURPOSE
Convert {value} {from_unit if from_unit else 'units'} to {to_unit if to_unit else 'target units'} for speed/velocity measurements.

### 📊 MAIN GOALS
1. **Unit Decomposition** - Break down compound units (distance/time)
2. **Systematic Conversion** - Convert distance and time components
3. **Practical Application** - Relate to real-world speeds
4. **Accuracy Verification** - Ensure reasonable results

### 🔍 SUB-GOALS AND APPROACH

#### Goal 1: Understanding Compound Units
**Objective**: Decompose speed units into distance and time
**Why**: Speed conversions require handling two unit types

**Common speed units**:
- m/s (meters per second) - SI standard
- km/h (kilometers per hour) - Common metric
- mph (miles per hour) - US/UK standard
- ft/s (feet per second) - Engineering
- knots (nautical miles per hour) - Maritime/Aviation

#### Goal 2: Conversion Methodology
**Objective**: Apply systematic conversion approach
**Why**: Ensures accuracy and traceability

**Step 2.1**: Direct conversions
- km/h to m/s: divide({value}, 3.6)
- m/s to km/h: multiply({value}, 3.6)
- mph to km/h: multiply({value}, 1.60934)
- km/h to mph: divide({value}, 1.60934)
- knots to km/h: multiply({value}, 1.852)

**Step 2.2**: Component conversion method
- Convert distance unit: multiply/divide by distance factor
- Convert time unit: multiply/divide by time factor
- Example: ft/s to m/s
  - Feet to meters: multiply({value}, 0.3048)
  - Seconds unchanged: result is in m/s

#### Goal 3: Multi-step Conversions
**Objective**: Handle complex conversions
**Why**: Some conversions lack direct factors

**Example: mph to m/s**
- Step 1: mph to km/h: multiply({value}, 1.60934)
- Step 2: km/h to m/h: multiply(result, 1000)
- Step 3: m/h to m/s: divide(result, 3600)
- Simplified: multiply({value}, 0.44704)

#### Goal 4: Context and Validation
**Objective**: Provide reference speeds
**Why**: Helps validate conversion results

**Reference speeds**:
- Walking: ~5 km/h = ~3 mph = ~1.4 m/s
- Bicycle: ~20 km/h = ~12 mph = ~5.5 m/s
- City driving: ~50 km/h = ~31 mph = ~14 m/s
- Highway: ~100 km/h = ~62 mph = ~28 m/s
- Sound: ~343 m/s = ~1235 km/h = ~767 mph

### 📐 Conversion Formulas
- 1 m/s = 3.6 km/h
- 1 km/h = 0.277778 m/s
- 1 mph = 1.60934 km/h = 0.44704 m/s
- 1 knot = 1.852 km/h = 0.514444 m/s
- 1 ft/s = 0.3048 m/s

### ⚙️ Execution Instructions
Please use MCP tools (multiply, divide) for ALL calculations.
Show clear steps for compound unit conversions."""
        
    elif conversion_lower == "volume":
        return f"""## Unit Conversion Task: Volume/Capacity Measurement

### 🎯 PRIMARY PURPOSE
Convert {value} {from_unit if from_unit else 'units'} to {to_unit if to_unit else 'target units'} for volume/capacity measurements.

### 📊 MAIN GOALS
1. **System Classification** - Identify metric, imperial, or US customary units
2. **Conversion Execution** - Apply correct conversion factors
3. **Practical Context** - Relate to common containers
4. **Cross-system Bridge** - Handle metric-imperial conversions

### 🔍 SUB-GOALS AND APPROACH

#### Goal 1: Volume Unit Systems
**Objective**: Understand different measurement systems
**Why**: Volume units vary significantly by region and application

**Metric System**:
- 1 cubic meter (m³) = 1000 liters
- 1 liter = 1000 milliliters (ml)
- 1 liter = 1 cubic decimeter (dm³)
- 1 milliliter = 1 cubic centimeter (cm³/cc)

**US Customary**:
- 1 gallon (US) = 4 quarts
- 1 quart = 2 pints
- 1 pint = 2 cups
- 1 cup = 8 fluid ounces
- 1 gallon (US) = 3.78541 liters

**Imperial (UK)**:
- 1 gallon (UK) = 4.54609 liters
- 1 gallon (UK) = 1.20095 gallons (US)

#### Goal 2: Conversion Calculations
**Objective**: Execute precise conversions
**Why**: Accuracy matters in recipes, chemistry, and engineering

**Step 2.1**: Metric conversions
- Liters to milliliters: multiply({value}, 1000)
- m³ to liters: multiply({value}, 1000)
- ml to liters: divide({value}, 1000)

**Step 2.2**: US customary conversions
- Gallons to quarts: multiply({value}, 4)
- Quarts to cups: multiply({value}, 4)
- Cups to fluid ounces: multiply({value}, 8)

**Step 2.3**: Cross-system conversions
- Liters to US gallons: divide({value}, 3.78541)
- US gallons to liters: multiply({value}, 3.78541)
- Liters to UK gallons: divide({value}, 4.54609)

#### Goal 3: Cubic Measurements
**Objective**: Handle three-dimensional volume units
**Why**: Used in shipping, construction, and science

**Relationships**:
- 1 m³ = 1,000,000 cm³
- 1 ft³ = 1728 in³
- 1 yd³ = 27 ft³
- 1 m³ = 35.3147 ft³

**Conversion approach**:
- Convert each dimension separately
- Or use direct volume conversion factor
- Example: ft³ to m³: multiply({value}, 0.0283168)

#### Goal 4: Practical Applications
**Objective**: Provide relatable context
**Why**: Helps visualize volumes

**Common references**:
- Teaspoon: ~5 ml
- Tablespoon: ~15 ml
- Shot glass: ~44 ml (1.5 fl oz)
- Soda can: 355 ml (12 fl oz)
- Wine bottle: 750 ml
- 2-liter bottle: 2000 ml
- Bathtub: ~300-400 liters
- Swimming pool: 50,000+ liters

### 📊 Quick Reference
**Kitchen conversions**:
- 1 tablespoon = 3 teaspoons = 15 ml
- 1 cup = 16 tablespoons = 237 ml
- 1 liter ≈ 4.23 cups

**Fuel/liquid**:
- 1 barrel (oil) = 42 US gallons = 159 liters

### ⚙️ Execution Instructions
Please use MCP tools (multiply, divide) for ALL calculations.
When converting between systems, show intermediate steps."""
        
    else:
        return f"""## Unit Conversion Task: General Conversion Guide

### 🎯 PRIMARY PURPOSE
Provide guidance for converting {value} units in the {conversion_type} category using MCP calculation tools.

### 📊 AVAILABLE CONVERSION CATEGORIES

#### 1. Temperature Conversions
- Celsius ↔ Fahrenheit ↔ Kelvin
- Formula-based conversions requiring add, subtract, multiply, divide

#### 2. Length/Distance Conversions
- Metric: km, m, cm, mm
- Imperial: miles, yards, feet, inches
- Direct multiplication/division factors

#### 3. Weight/Mass Conversions
- Metric: tonnes, kg, g, mg
- Imperial: tons, pounds, ounces
- Cross-system conversions available

#### 4. Speed/Velocity Conversions
- m/s, km/h, mph, knots
- Compound unit conversions (distance/time)

#### 5. Volume/Capacity Conversions
- Metric: liters, milliliters, m³
- US: gallons, quarts, cups, fl oz
- Imperial: UK gallons, pints

### 🔍 GENERAL CONVERSION APPROACH

#### Step 1: Identify Unit Systems
- Determine source and target unit systems
- Check if direct conversion exists

#### Step 2: Find Conversion Path
- Direct conversion: Single multiplication/division
- Indirect: Convert through intermediate unit

#### Step 3: Execute Calculation
- Use MCP tools for all calculations
- Break complex formulas into steps

#### Step 4: Verify Result
- Check magnitude and direction
- Compare with known references
- Test reverse conversion

### 📐 Universal Principles
1. **Metric prefixes**: kilo (×1000), centi (÷100), milli (÷1000)
2. **Dimensional analysis**: Track units through calculation
3. **Significant figures**: Maintain appropriate precision
4. **Verification**: Always sanity-check results

### ⚙️ Execution Instructions
Specify the exact conversion needed:
- Conversion type: {conversion_type}
- Value: {value}
- From unit: {from_unit if from_unit else 'not specified'}
- To unit: {to_unit if to_unit else 'not specified'}

Please use MCP tools (add, subtract, multiply, divide) for ALL calculations."""

def _get_temperature_conversion_steps(from_unit: str, to_unit: str, value: float) -> str:
    """Generate specific conversion steps for temperature."""
    
    conversions = {
        ('celsius', 'fahrenheit'): f"""**Step 2.1**: Celsius to Fahrenheit (F = C × 9/5 + 32)
   - Purpose: Convert from Celsius scale to Fahrenheit scale
   - Phase 1: Calculate 9/5: divide(9, 5) = 1.8
   - Phase 2: Multiply by factor: multiply({value}, 1.8)
   - Phase 3: Add offset: add(result, 32)
   - Expected result: Fahrenheit temperature""",
        
        ('fahrenheit', 'celsius'): f"""**Step 2.1**: Fahrenheit to Celsius (C = (F - 32) × 5/9)
   - Purpose: Convert from Fahrenheit scale to Celsius scale
   - Phase 1: Subtract offset: subtract({value}, 32)
   - Phase 2: Calculate 5/9: divide(5, 9) = 0.5556
   - Phase 3: Apply factor: multiply(result, 0.5556)
   - Expected result: Celsius temperature""",
        
        ('celsius', 'kelvin'): f"""**Step 2.1**: Celsius to Kelvin (K = C + 273.15)
   - Purpose: Convert to absolute temperature scale
   - Method: add({value}, 273.15)
   - Note: Simple offset, no scaling needed
   - Expected result: Kelvin temperature""",
        
        ('kelvin', 'celsius'): f"""**Step 2.1**: Kelvin to Celsius (C = K - 273.15)
   - Purpose: Convert from absolute to Celsius scale
   - Method: subtract({value}, 273.15)
   - Note: Simple offset, no scaling needed
   - Expected result: Celsius temperature""",
        
        ('fahrenheit', 'kelvin'): f"""**Step 2.1**: Fahrenheit to Kelvin (K = (F - 32) × 5/9 + 273.15)
   - Purpose: Convert Fahrenheit to absolute temperature
   - Phase 1: Subtract F offset: subtract({value}, 32)
   - Phase 2: Calculate 5/9: divide(5, 9) = 0.5556
   - Phase 3: Apply factor: multiply(result, 0.5556)
   - Phase 4: Add K offset: add(result, 273.15)
   - Expected result: Kelvin temperature""",
        
        ('kelvin', 'fahrenheit'): f"""**Step 2.1**: Kelvin to Fahrenheit (F = (K - 273.15) × 9/5 + 32)
   - Purpose: Convert absolute temperature to Fahrenheit
   - Phase 1: Convert to Celsius: subtract({value}, 273.15)
   - Phase 2: Calculate 9/5: divide(9, 5) = 1.8
   - Phase 3: Apply factor: multiply(result, 1.8)
   - Phase 4: Add F offset: add(result, 32)
   - Expected result: Fahrenheit temperature"""
    }
    
    key = (from_unit.lower(), to_unit.lower())
    return conversions.get(key, f"""**Step 2.1**: Custom conversion
   - From: {from_unit}
   - To: {to_unit}
   - Value: {value}
   - Note: Specify the conversion formula for calculation""")