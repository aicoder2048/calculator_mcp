def fitness_analytics_prompt(metric_type: str, time_period: str = "weekly", goal_type: str = "health_monitoring") -> str:
    """Generate a prompt for fitness and health analytics with detailed MCP tool guidance."""
    
    metric = metric_type.lower()
    period = time_period.lower()
    goal = goal_type.lower()
    
    if metric == "steps":
        return f"""## Fitness Analytics Task: Step Count Analysis

### 🎯 PRIMARY PURPOSE
Analyze daily step count data over {time_period} period to assess activity levels, identify patterns, and optimize fitness goals for {goal_type.replace('_', ' ')}.

### 📊 MAIN GOALS
1. **Activity Assessment** - Evaluate current activity levels and consistency
2. **Pattern Recognition** - Identify daily/weekly activity patterns
3. **Goal Optimization** - Set realistic and achievable step targets
4. **Health Impact** - Correlate activity with general wellness indicators

### 🔍 SUB-GOALS AND APPROACH

#### Goal 1: Basic Activity Metrics
**Objective**: Calculate fundamental step statistics
**Why**: Establish baseline understanding of activity levels

**Step 1.1**: Calculate average daily steps
   - Purpose: Determine typical activity level
   - Method: mean(step_counts)
   - Target insight: Are you meeting recommended 8,000-10,000 steps/day?
   - Health context: Higher averages indicate better cardiovascular health

**Step 1.2**: Find step count consistency
   - Purpose: Assess activity regularity
   - Calculate variance: variance(step_counts)
   - Calculate standard deviation: stddev(step_counts)  
   - Low variance = consistent activity, High variance = irregular patterns
   - Consistency is key for sustainable fitness improvements

**Step 1.3**: Identify activity range
   - Purpose: Understand activity spectrum
   - Calculate minimum: min_value(step_counts)
   - Calculate maximum: max_value(step_counts)
   - Calculate range: range_stat(step_counts)
   - Wide range may indicate lifestyle or motivation fluctuations

#### Goal 2: Performance Analysis
**Objective**: Analyze step count distribution and trends
**Why**: Identify improvement opportunities and set realistic goals

**Step 2.1**: Percentile analysis for goal setting
   - Purpose: Set achievable progressive targets
   - Calculate 25th percentile: percentile(step_counts, 25)
   - Calculate 50th percentile (median): median(step_counts)
   - Calculate 75th percentile: percentile(step_counts, 75)
   - Use 75th percentile as stretch goal, median as baseline

**Step 2.2**: Activity quartile breakdown
   - Purpose: Categorize performance levels
   - Calculate quartiles: quartiles(step_counts)
   - Q1: Lower activity days (need motivation boost)
   - Q2-Q3: Typical activity range
   - Q4: High activity days (analyze what made these successful)

**Step 2.3**: Outlier detection
   - Purpose: Identify unusual activity days
   - Calculate IQR: iqr(step_counts)
   - Days below Q1 - 1.5×IQR: Unusually low activity
   - Days above Q3 + 1.5×IQR: Exceptionally active days
   - Analyze context for both extremes

#### Goal 3: Activity Pattern Insights
**Objective**: Understand behavioral patterns and optimization opportunities
**Why**: Lifestyle integration and sustainable habit formation

**Step 3.1**: Most common activity levels
   - Purpose: Identify habitual activity patterns
   - Calculate mode: mode(step_counts)
   - This reveals your "default" activity level
   - Focus on gradually increasing this baseline

**Step 3.2**: Weekly trend analysis
   - Purpose: Detect weekly patterns and schedule optimization
   - Compare weekday vs weekend averages
   - Identify which days consistently have higher/lower activity
   - Plan activities around naturally active periods

#### Goal 4: Health Goal Alignment
**Objective**: Assess progress toward specific health objectives
**Why**: Different goals require different activity patterns

**For Weight Loss Goal**:
   - Target: 10,000+ steps daily for calorie burn
   - Analysis: Count days meeting target using statistical tools
   - Calculate deficit days and plan improvements

**For Fitness Improvement Goal**:
   - Target: Progressive increase in weekly averages
   - Analysis: Compare current to previous period means
   - Look for positive trends in maximum values

**For Health Monitoring Goal**:
   - Target: Consistent moderate activity (6,000-8,000 steps)
   - Analysis: Focus on reducing variance, maintaining median
   - Monitor for sudden decreases that might indicate health issues

### 💡 Activity Insights
- **Recommended Targets**: 8,000-10,000 steps for general health
- **Active Lifestyle**: 12,000+ steps daily
- **Sedentary Alert**: <5,000 steps consistently
- **Weekend Warriors**: High variance with periodic peaks

### 🏃 Optimization Strategies
- **Low Average**: Gradually increase daily target by 500-1,000 steps
- **High Variance**: Focus on consistency over peak performance
- **Plateau Pattern**: Add variety or intensity to break through
- **Declining Trend**: Identify barriers and adjust lifestyle factors

### 📱 Technology Integration
- **Smartphone Counting**: Generally underestimates by 5-10%
- **Fitness Trackers**: More accurate but check calibration
- **Manual Logging**: Prone to estimation errors
- **Data Quality**: Clean outliers (0 steps = device not worn)

### ⚙️ Execution Instructions
Use MCP tools for ALL calculations: mean, variance, stddev, min_value, max_value, range_stat, percentile, median, quartiles, iqr, mode.
Focus on actionable insights that support {goal_type.replace('_', ' ')} objectives."""

    elif metric == "calories":
        return f"""## Fitness Analytics Task: Calorie Burn Analysis

### 🎯 PRIMARY PURPOSE
Analyze calorie expenditure data over {time_period} period to optimize energy balance, support {goal_type.replace('_', ' ')}, and improve metabolic health.

### 📊 MAIN GOALS
1. **Energy Balance Assessment** - Calculate calorie burn patterns and deficits/surpluses
2. **Metabolic Insights** - Understand basal metabolic rate and active burn
3. **Goal Alignment** - Optimize calorie targets for specific fitness objectives
4. **Efficiency Analysis** - Identify most effective calorie-burning activities

### 🔍 SUB-GOALS AND APPROACH

#### Goal 1: Baseline Metabolic Analysis
**Objective**: Establish calorie burn baselines and patterns
**Why**: Understanding your metabolic profile is crucial for effective goal setting

**Step 1.1**: Average daily calorie burn
   - Purpose: Determine typical energy expenditure
   - Method: mean(calorie_burns)
   - Context: Average adult burns 1,800-2,400 calories daily
   - Include both BMR (60-70%) and activity calories (30-40%)

**Step 1.2**: Calorie burn consistency
   - Purpose: Assess metabolic and activity regularity
   - Calculate variance: variance(calorie_burns)
   - Calculate standard deviation: stddev(calorie_burns)
   - Low variance = stable routine, High variance = inconsistent activity
   - Consistency helps predict and plan energy needs

**Step 1.3**: Energy expenditure range
   - Purpose: Understand daily energy fluctuations
   - Calculate minimum: min_value(calorie_burns)
   - Calculate maximum: max_value(calorie_burns)
   - Calculate range: range_stat(calorie_burns)
   - Wide range indicates variable activity levels or measurement issues

#### Goal 2: Performance Distribution Analysis
**Objective**: Analyze calorie burn distribution for optimization
**Why**: Different burn levels correspond to different activity intensities

**Step 2.1**: Burn level categorization
   - Purpose: Classify daily energy expenditure patterns
   - Calculate quartiles: quartiles(calorie_burns)
   - Q1: Lower activity/metabolic days
   - Q2: Moderate energy expenditure (baseline)
   - Q3: Active days with elevated burn
   - Q4: High-intensity or long-duration activity days

**Step 2.2**: Target zone analysis
   - Purpose: Set appropriate calorie burn goals
   - Calculate 75th percentile: percentile(calorie_burns, 75)
   - Use as stretch target for active days
   - Calculate median: median(calorie_burns)
   - Use as minimum consistency target

**Step 2.3**: Outlier identification
   - Purpose: Identify exceptional or problematic days
   - Calculate IQR: iqr(calorie_burns)
   - Very low days: Potential illness or inactivity
   - Very high days: Intense training or long activities
   - Analyze context for both extremes

#### Goal 3: Metabolic Pattern Recognition
**Objective**: Understand energy expenditure patterns and efficiency
**Why**: Optimize activity timing and intensity for goals

**Step 3.1**: Most common burn levels
   - Purpose: Identify habitual energy expenditure
   - Calculate mode: mode(calorie_burns)
   - This reveals your typical metabolic state
   - Focus on strategies to elevate this baseline

**Step 3.2**: Weekly energy patterns
   - Purpose: Optimize weekly energy planning
   - Compare different days of week
   - Identify naturally high-burn days
   - Plan intense activities during peak burn periods

#### Goal 4: Goal-Specific Calorie Analysis
**Objective**: Align calorie burn with specific fitness objectives
**Why**: Different goals require different energy strategies

**For Weight Loss Goal**:
   - Target: 500-750 calorie daily deficit through increased burn
   - Analysis: Compare burn to estimated intake needs
   - Calculate days achieving deficit target
   - Focus on sustainable burn increase strategies

**For Fitness Improvement Goal**:
   - Target: Progressive increase in active calories (not just BMR)
   - Analysis: Track trend in maximum daily burns
   - Look for improvements in burn efficiency
   - Monitor recovery between high-burn days

**For Athletic Training Goal**:
   - Target: Optimize burn for performance and recovery
   - Analysis: Balance high-intensity and recovery days
   - Monitor for overtraining (consistently declining burns)
   - Track adaptation through burn efficiency improvements

**For Health Monitoring Goal**:
   - Target: Stable, consistent energy expenditure
   - Analysis: Focus on reducing day-to-day variance
   - Monitor for sudden changes indicating health issues
   - Maintain moderate, sustainable activity levels

### 💡 Calorie Burn Insights
- **Sedentary BMR**: 1,200-1,500 calories (basic functions)
- **Light Activity**: 1,500-2,000 calories (office work + light exercise)
- **Moderate Activity**: 2,000-2,500 calories (regular exercise)
- **High Activity**: 2,500+ calories (intense training/physical job)

### 🔥 Optimization Strategies
- **Low Average**: Add 150-300 calories through increased activity
- **High Variance**: Establish consistent daily movement baseline
- **Plateau Pattern**: Vary exercise intensity and duration
- **Recovery Balance**: Ensure adequate rest between high-burn days

### 📊 Measurement Considerations
- **Fitness Trackers**: Generally overestimate by 15-25%
- **Heart Rate Based**: More accurate for cardio activities
- **Activity Specific**: Different activities have different accuracy
- **Individual Variation**: Calibrate to your personal metabolic rate

### ⚙️ Execution Instructions
Use MCP tools for ALL calculations: mean, variance, stddev, min_value, max_value, range_stat, percentile, median, quartiles, iqr, mode.
Focus on sustainable energy balance strategies supporting {goal_type.replace('_', ' ')}."""

    elif metric == "heart_rate":
        return f"""## Fitness Analytics Task: Heart Rate Analysis

### 🎯 PRIMARY PURPOSE
Analyze heart rate data over {time_period} period to assess cardiovascular health, optimize training zones, and monitor {goal_type.replace('_', ' ')} progress.

### 📊 MAIN GOALS
1. **Cardiovascular Health Assessment** - Evaluate resting HR and variability
2. **Training Zone Optimization** - Identify optimal exercise intensity ranges
3. **Recovery Monitoring** - Track heart rate recovery and adaptation
4. **Health Risk Detection** - Identify concerning HR patterns or trends

### 🔍 SUB-GOALS AND APPROACH

#### Goal 1: Baseline Heart Rate Assessment
**Objective**: Establish resting and average heart rate baselines
**Why**: Resting HR is a key indicator of cardiovascular fitness and health

**Step 1.1**: Average heart rate analysis
   - Purpose: Determine typical heart rate across all activities
   - Method: mean(heart_rates)
   - Context: Should reflect mix of resting (60-100) and active (100+) periods
   - Lower averages generally indicate better cardiovascular fitness

**Step 1.2**: Heart rate variability assessment
   - Purpose: Evaluate cardiovascular system stability
   - Calculate variance: variance(heart_rates)
   - Calculate standard deviation: stddev(heart_rates)
   - Moderate variance is healthy (indicates responsive system)
   - Very low variance may indicate poor adaptation

**Step 1.3**: Heart rate range analysis
   - Purpose: Understand cardiovascular range and capacity
   - Calculate minimum: min_value(heart_rates) (likely resting HR)
   - Calculate maximum: max_value(heart_rates) (peak exercise HR)
   - Calculate range: range_stat(heart_rates)
   - Wide range indicates good cardiovascular reserve

#### Goal 2: Training Zone Distribution
**Objective**: Analyze time spent in different heart rate zones
**Why**: Optimal training requires balanced time across intensity zones

**Step 2.1**: Heart rate zone classification
   - Purpose: Categorize training intensity distribution
   - Calculate quartiles: quartiles(heart_rates)
   - Zone 1 (Q1): Recovery/easy pace (50-60% max HR)
   - Zone 2 (Q2): Aerobic base (60-70% max HR)
   - Zone 3 (Q3): Tempo/threshold (70-80% max HR)
   - Zone 4+ (Q4): VO2 max/anaerobic (80%+ max HR)

**Step 2.2**: Training intensity analysis
   - Purpose: Optimize training distribution
   - Calculate 80th percentile: percentile(heart_rates, 80)
   - Most training should be below this threshold (80/20 rule)
   - Calculate median: median(heart_rates)
   - This should be in aerobic base zone for endurance athletes

**Step 2.3**: Peak performance identification
   - Purpose: Identify maximum effort sessions
   - Calculate 95th percentile: percentile(heart_rates, 95)
   - These represent peak training intensities
   - Monitor frequency and recovery from these sessions

#### Goal 3: Recovery and Adaptation Monitoring
**Objective**: Assess cardiovascular recovery and training adaptation
**Why**: Recovery quality indicates training effectiveness and overtraining risk

**Step 3.1**: Resting heart rate trends
   - Purpose: Monitor cardiovascular fitness improvements
   - Calculate lowest 10% of readings: percentile(heart_rates, 10)
   - This approximates true resting HR
   - Declining resting HR indicates improved fitness
   - Suddenly elevated resting HR may indicate overtraining or illness

**Step 3.2**: Heart rate pattern consistency
   - Purpose: Identify concerning variations
   - Calculate IQR: iqr(heart_rates)
   - Look for outliers beyond normal training ranges
   - Sudden spikes or consistently elevated readings need attention

**Step 3.3**: Common heart rate patterns
   - Purpose: Identify typical training intensities
   - Calculate mode: mode(heart_rates)
   - This reveals your most frequent training intensity
   - Should align with training phase goals

#### Goal 4: Health and Safety Monitoring
**Objective**: Detect potential health concerns through HR analysis
**Why**: Heart rate patterns can indicate health issues or overtraining

**For Health Monitoring Goal**:
   - Target: Stable resting HR (50-90 bpm for adults)
   - Analysis: Monitor resting HR trends over time
   - Alert: Resting HR consistently >100 or sudden increases >10 bpm
   - Track recovery HR after moderate exercise

**For Fitness Improvement Goal**:
   - Target: Decreasing resting HR, increasing max HR capacity
   - Analysis: Compare current to previous period baselines
   - Look for improved HR recovery (faster return to baseline)
   - Monitor training zone efficiency improvements

**For Athletic Training Goal**:
   - Target: Optimized training distribution (80% easy, 20% hard)
   - Analysis: Ensure adequate time in each training zone
   - Monitor for overtraining (elevated resting HR, poor recovery)
   - Track heart rate variability trends

**For Weight Loss Goal**:
   - Target: Consistent time in fat-burning zone (60-70% max HR)
   - Analysis: Calculate time spent in optimal zones
   - Balance moderate intensity with recovery
   - Monitor for excessive high-intensity work

### 💓 Heart Rate Reference Ranges
- **Resting HR**: 60-100 bpm (lower is generally better for fitness)
- **Fat Burning Zone**: 60-70% of max HR
- **Aerobic Zone**: 70-80% of max HR  
- **Anaerobic Zone**: 80-90% of max HR
- **Max HR Estimate**: 220 - age (rough approximation)

### 🏃 Training Optimization
- **High Resting HR**: Focus on more easy-pace training
- **Low Variability**: Add variety in training intensities
- **Poor Recovery**: Increase rest days and sleep quality
- **Plateau Performance**: Periodize training with intensity cycles

### ⚠️ Health Alerts
- **Resting HR >100**: Consult healthcare provider
- **Sudden HR Spikes**: Check for medication, caffeine, stress factors
- **Poor Exercise Recovery**: May indicate overtraining or health issues
- **Irregular Patterns**: Consider heart rhythm evaluation

### 📱 Measurement Notes
- **Chest Straps**: Most accurate for exercise
- **Wrist Monitors**: Good for trends, less accurate during exercise
- **Manual Pulse**: Reliable for resting measurements
- **Timing**: Measure resting HR upon waking before getting up

### ⚙️ Execution Instructions
Use MCP tools for ALL calculations: mean, variance, stddev, min_value, max_value, range_stat, percentile, median, quartiles, iqr, mode.
Focus on cardiovascular health insights supporting {goal_type.replace('_', ' ')} objectives."""

    elif metric == "weight":
        return f"""## Fitness Analytics Task: Weight Progress Analysis

### 🎯 PRIMARY PURPOSE
Analyze weight measurements over {time_period} period to track progress, identify trends, and optimize {goal_type.replace('_', ' ')} strategies.

### 📊 MAIN GOALS
1. **Progress Tracking** - Calculate weight trends and rate of change
2. **Consistency Assessment** - Evaluate measurement reliability and patterns
3. **Goal Achievement** - Analyze progress toward target weight
4. **Health Monitoring** - Detect concerning weight fluctuations

### 🔍 SUB-GOALS AND APPROACH

#### Goal 1: Weight Trend Analysis
**Objective**: Establish overall weight trajectory and patterns
**Why**: Weight fluctuates daily; trends are more meaningful than individual measurements

**Step 1.1**: Average weight calculation
   - Purpose: Determine central tendency for the period
   - Method: mean(weight_measurements)
   - Context: More reliable than any single measurement
   - Use for progress comparisons between periods

**Step 1.2**: Weight stability assessment
   - Purpose: Evaluate natural weight fluctuation range
   - Calculate variance: variance(weight_measurements)
   - Calculate standard deviation: stddev(weight_measurements)
   - Normal daily fluctuation: 1-3 lbs due to hydration, food, hormones
   - High variance may indicate measurement inconsistencies

**Step 1.3**: Weight range analysis
   - Purpose: Understand weight fluctuation extremes
   - Calculate minimum: min_value(weight_measurements)
   - Calculate maximum: max_value(weight_measurements)
   - Calculate range: range_stat(weight_measurements)
   - Large ranges (>5 lbs) may indicate water retention or measurement issues

#### Goal 2: Progress Distribution Analysis
**Objective**: Analyze weight distribution for realistic goal setting
**Why**: Understanding weight patterns helps set achievable targets

**Step 2.1**: Weight percentile analysis
   - Purpose: Identify typical vs. exceptional weight readings
   - Calculate quartiles: quartiles(weight_measurements)
   - Q1: Lower weight range (possible dehydration or loss goal)
   - Q2 (median): Typical stable weight
   - Q3: Higher weight range (possible retention or gain concern)
   - Use median for most accurate current weight

**Step 2.2**: Target weight assessment
   - Purpose: Set realistic short-term weight goals
   - Calculate 25th percentile: percentile(weight_measurements, 25)
   - This could be a reasonable short-term loss target
   - Calculate 75th percentile: percentile(weight_measurements, 75)
   - Monitor to ensure this doesn't become new baseline

**Step 2.3**: Outlier detection
   - Purpose: Identify measurement errors or concerning changes
   - Calculate IQR: iqr(weight_measurements)
   - Weights beyond Q1-1.5×IQR or Q3+1.5×IQR are outliers
   - Investigate context: scale calibration, timing, hydration

#### Goal 3: Weight Pattern Recognition
**Objective**: Identify behavioral and physiological weight patterns
**Why**: Patterns reveal underlying factors affecting weight

**Step 3.1**: Most common weight range
   - Purpose: Identify natural weight setpoint
   - Calculate mode: mode(weight_measurements)
   - This represents your body's preferred weight range
   - Significant changes from this may require sustained effort

**Step 3.2**: Weekly weight patterns
   - Purpose: Identify weekly fluctuation cycles
   - Compare same days of week across multiple weeks
   - Common patterns: Higher on Mondays, lower on Fridays
   - Use for timing weigh-ins and setting expectations

#### Goal 4: Goal-Specific Weight Analysis
**Objective**: Align weight analysis with specific objectives
**Why**: Different goals require different weight management approaches

**For Weight Loss Goal**:
   - Target: Consistent 1-2 lb weekly loss (healthy rate)
   - Analysis: Compare current mean to previous period mean
   - Calculate trend: subtract(current_average, previous_average)
   - Monitor for plateaus or rapid loss (>3 lbs/week)
   - Focus on reducing median weight over time

**For Weight Gain Goal** (muscle building):
   - Target: Gradual 0.5-1 lb weekly gain
   - Analysis: Ensure gain is consistent, not sporadic
   - Monitor variance to distinguish muscle vs. water/fat gain
   - Look for steady upward trend in minimum weights

**For Weight Maintenance Goal**:
   - Target: Stable weight within 2-3 lb range
   - Analysis: Minimize variance while maintaining median
   - Calculate coefficient of variation: divide(stddev, mean)
   - Lower percentages indicate better maintenance

**For Health Monitoring Goal**:
   - Target: Stable weight without concerning fluctuations
   - Analysis: Monitor for sudden changes >5% body weight
   - Track consistency of measurements
   - Alert for rapid unintentional changes

### ⚖️ Weight Management Insights
- **Healthy Loss Rate**: 1-2 lbs per week (0.5-1% body weight)
- **Daily Fluctuation**: 1-3 lbs normal due to various factors
- **Plateau Normal**: Weight loss often occurs in steps, not linear
- **Water Weight**: Can mask fat loss for several weeks

### 📊 Measurement Best Practices
- **Timing**: Same time daily (morning after bathroom, before eating)
- **Clothing**: Minimal, consistent clothing
- **Scale Placement**: Hard, level surface
- **Frequency**: Daily for trends, weekly for less stress
- **Context**: Note factors affecting weight (sodium, hormones, travel)

### 🎯 Goal Optimization Strategies
- **Slow Loss**: Increase calorie deficit gradually
- **Rapid Loss**: Ensure adequate nutrition, may be unsustainable
- **High Variance**: Improve measurement consistency, check scale calibration
- **Plateau**: May need diet/exercise changes or patience (normal)

### ⚠️ Health Considerations
- **Rapid Loss**: >3 lbs/week may indicate health issues
- **Rapid Gain**: >5 lbs/week may indicate fluid retention
- **Extreme Fluctuations**: >10 lb range may need medical evaluation
- **Unintentional Changes**: Significant changes without trying warrant investigation

### 📱 Technology and Tools
- **Digital Scales**: More precise, check calibration monthly
- **Smart Scales**: Track trends automatically, but focus on weight trends
- **Body Composition**: Weight alone doesn't show muscle vs. fat changes
- **Progress Photos**: Complement weight data for complete picture

### ⚙️ Execution Instructions
Use MCP tools for ALL calculations: mean, variance, stddev, min_value, max_value, range_stat, percentile, median, quartiles, iqr, mode.
Focus on sustainable weight management supporting {goal_type.replace('_', ' ')} objectives."""

    elif metric == "blood_pressure":
        return f"""## Fitness Analytics Task: Blood Pressure Monitoring

### 🎯 PRIMARY PURPOSE
Analyze blood pressure measurements over {time_period} period to monitor cardiovascular health, assess {goal_type.replace('_', ' ')} impact, and detect concerning trends.

### 📊 MAIN GOALS
1. **Health Risk Assessment** - Evaluate BP readings against clinical standards
2. **Trend Monitoring** - Track changes over time for health management
3. **Lifestyle Impact** - Correlate BP with fitness and lifestyle factors
4. **Risk Detection** - Identify concerning patterns requiring medical attention

### 🔍 SUB-GOALS AND APPROACH

#### Goal 1: Blood Pressure Baseline Assessment
**Objective**: Establish systolic and diastolic pressure baselines
**Why**: BP baseline is crucial for monitoring cardiovascular health and medication effectiveness

**Step 1.1**: Average blood pressure analysis
   - Purpose: Determine typical pressure levels for the period
   - Calculate systolic average: mean(systolic_readings)
   - Calculate diastolic average: mean(diastolic_readings)
   - Context: Compare to clinical guidelines (normal <120/80)
   - Use for trend analysis and medical discussions

**Step 1.2**: Blood pressure variability assessment
   - Purpose: Evaluate BP stability and consistency
   - Calculate systolic variance: variance(systolic_readings)
   - Calculate diastolic variance: variance(diastolic_readings)
   - Calculate standard deviations: stddev(systolic), stddev(diastolic)
   - High variability may indicate white coat syndrome or poor technique

**Step 1.3**: Pressure range analysis
   - Purpose: Understand BP fluctuation patterns
   - Calculate systolic range: range_stat(systolic_readings)
   - Calculate diastolic range: range_stat(diastolic_readings)
   - Find minimums: min_value(systolic), min_value(diastolic)
   - Find maximums: max_value(systolic), max_value(diastolic)
   - Wide ranges may indicate timing or technique inconsistencies

#### Goal 2: Clinical Risk Category Analysis
**Objective**: Classify readings according to medical guidelines
**Why**: Proper categorization guides treatment and lifestyle decisions

**Step 2.1**: Blood pressure percentile distribution
   - Purpose: Understand distribution of readings across risk categories
   - Calculate systolic quartiles: quartiles(systolic_readings)
   - Calculate diastolic quartiles: quartiles(diastolic_readings)
   - Q1: Best readings (target for improvement)
   - Q2 (median): Typical readings
   - Q3-Q4: Higher readings (focus for intervention)

**Step 2.2**: High blood pressure frequency
   - Purpose: Assess frequency of concerning readings
   - Calculate 90th percentile: percentile(systolic_readings, 90)
   - Calculate 90th percentile: percentile(diastolic_readings, 90)
   - Readings above 90th percentile require attention
   - Monitor frequency of readings >140/90 (stage 1 hypertension)

**Step 2.3**: Optimal reading frequency
   - Purpose: Identify percentage of healthy readings
   - Calculate 25th percentile: percentile(systolic_readings, 25)
   - Calculate 25th percentile: percentile(diastolic_readings, 25)
   - These represent your best quarter of readings
   - Goal: Increase frequency of readings in this range

#### Goal 3: Blood Pressure Pattern Recognition
**Objective**: Identify temporal and situational BP patterns
**Why**: Patterns help identify triggers and optimize management

**Step 3.1**: Most common pressure readings
   - Purpose: Identify typical pressure patterns
   - Calculate systolic mode: mode(systolic_readings)
   - Calculate diastolic mode: mode(diastolic_readings)
   - These represent your most frequent readings
   - Focus improvement strategies around these baseline values

**Step 3.2**: Daily and weekly patterns
   - Purpose: Identify timing factors affecting BP
   - Compare morning vs. evening readings
   - Identify days with consistently higher/lower readings
   - Note correlation with stress, exercise, diet, medication timing

**Step 3.3**: Outlier identification and analysis
   - Purpose: Identify concerning spikes or drops
   - Calculate IQR for systolic: iqr(systolic_readings)
   - Calculate IQR for diastolic: iqr(diastolic_readings)
   - Readings beyond Q3 + 1.5×IQR warrant investigation
   - Document context for outliers (stress, exercise, medication)

#### Goal 4: Health and Lifestyle Correlation
**Objective**: Connect BP trends with fitness and health goals
**Why**: BP responds to lifestyle changes and can indicate goal effectiveness

**For Health Monitoring Goal**:
   - Target: Maintain readings <120/80 consistently
   - Analysis: Calculate percentage of readings in normal range
   - Monitor for upward trends requiring intervention
   - Track response to lifestyle changes over time

**For Fitness Improvement Goal**:
   - Target: BP reduction through improved cardiovascular fitness
   - Analysis: Compare current to previous period averages
   - Look for decreasing trend in median readings
   - Monitor recovery BP after exercise (should decrease over time)

**For Weight Loss Goal**:
   - Target: BP improvement correlating with weight loss
   - Analysis: Track both systolic and diastolic changes
   - Even 5-10 lb weight loss can significantly improve BP
   - Monitor for dramatic changes requiring medication adjustment

**For Athletic Training Goal**:
   - Target: Optimal BP for performance and recovery
   - Analysis: Balance training intensity with BP response
   - Monitor resting BP trends (should improve with fitness)
   - Watch for overtraining signs (consistently elevated BP)

### 🩺 Blood Pressure Categories (AHA Guidelines)
- **Normal**: <120 AND <80
- **Elevated**: 120-129 AND <80
- **Stage 1 Hypertension**: 130-139 OR 80-89
- **Stage 2 Hypertension**: ≥140 OR ≥90
- **Hypertensive Crisis**: >180 AND/OR >120 (seek immediate care)

### 📊 Measurement Best Practices
- **Timing**: Same time daily, avoid caffeine/exercise 30 min prior
- **Position**: Seated, feet flat, arm at heart level
- **Cuff Size**: Proper cuff size crucial for accuracy
- **Multiple Readings**: Take 2-3 readings, use average
- **Rest Period**: 5 minutes quiet rest before measuring

### 🎯 BP Improvement Strategies
- **High Average**: Focus on lifestyle modifications (diet, exercise, stress)
- **High Variability**: Improve measurement technique and timing consistency
- **Upward Trend**: Increase cardio exercise, reduce sodium, manage stress
- **Medication Effects**: Track response to dosage changes with physician

### ⚠️ Medical Alert Thresholds
- **Stage 1 Hypertension**: 130/80 - lifestyle changes, possible medication
- **Stage 2 Hypertension**: 140/90 - medication likely needed
- **Sudden Spikes**: >160/100 - contact healthcare provider
- **Hypertensive Crisis**: >180/120 - seek immediate medical attention

### 💊 Medication and Lifestyle Factors
- **Medication Timing**: Track BP response to medication schedule
- **Exercise Impact**: BP may be elevated immediately post-exercise
- **Stress Response**: Note correlation with life events or stress
- **Dietary Factors**: High sodium can elevate BP for 24-48 hours

### 📱 Monitoring Technology
- **Home Monitors**: Validated devices with proper cuff size
- **Smart Monitors**: Convenient but verify accuracy periodically
- **Manual vs. Automatic**: Both can be accurate with proper technique
- **Data Logging**: Consistent tracking more valuable than perfect accuracy

### ⚙️ Execution Instructions
Use MCP tools for ALL calculations: mean, variance, stddev, min_value, max_value, range_stat, percentile, median, quartiles, iqr, mode.
Provide both systolic and diastolic analysis supporting {goal_type.replace('_', ' ')} health objectives.
IMPORTANT: Always recommend consulting healthcare providers for concerning readings or trends."""

    else:
        return f"""## Fitness Analytics: Comprehensive Health Metrics Analysis

### 🎯 PRIMARY PURPOSE
Analyze multiple health and fitness metrics over {time_period} period to provide comprehensive health insights for {goal_type.replace('_', ' ')}.

### 📊 AVAILABLE METRICS FOR ANALYSIS

#### 1. Steps Analysis ("steps")
- **Focus**: Daily activity levels, movement patterns, goal achievement
- **Tools Used**: mean, variance, percentile, quartiles, mode
- **Insights**: Activity consistency, goal setting, lifestyle optimization
- **Targets**: 8,000-10,000 steps daily for general health

#### 2. Calorie Burn Analysis ("calories")
- **Focus**: Energy expenditure, metabolic rate, deficit/surplus analysis
- **Tools Used**: mean, stddev, range_stat, percentile, quartiles
- **Insights**: Energy balance, burn optimization, goal alignment
- **Targets**: Varies by goal (deficit for loss, surplus for gain)

#### 3. Heart Rate Analysis ("heart_rate")
- **Focus**: Cardiovascular health, training zones, recovery monitoring
- **Tools Used**: mean, variance, quartiles, iqr, percentile
- **Insights**: Fitness level, training optimization, health monitoring
- **Targets**: Zone-based training, improving resting HR

#### 4. Weight Tracking ("weight")
- **Focus**: Progress monitoring, trend analysis, goal achievement
- **Tools Used**: mean, variance, median, quartiles, mode
- **Insights**: Progress trends, plateau detection, realistic goal setting
- **Targets**: 1-2 lbs/week change for healthy progress

#### 5. Blood Pressure Monitoring ("blood_pressure")
- **Focus**: Cardiovascular health, risk assessment, medication response
- **Tools Used**: mean, quartiles, percentile, iqr, outlier detection
- **Insights**: Health risk categories, trend monitoring, lifestyle impact
- **Targets**: <120/80 for optimal health

### 🔍 MULTI-METRIC ANALYSIS APPROACH

#### Comprehensive Health Assessment
**Objective**: Analyze relationships between different health metrics
**Why**: Health metrics are interconnected and provide holistic insights

**Cross-Metric Correlations**:
- Weight loss correlation with increased steps and calorie burn
- Heart rate improvement with consistent exercise and weight management
- Blood pressure response to cardiovascular fitness improvements
- Overall health trend analysis across all metrics

#### Goal-Specific Multi-Metric Insights
**For Weight Loss**: Steps ↑, Calories ↑, Weight ↓, BP ↓, HR efficiency ↑
**For Fitness**: Steps ↑, HR zones optimized, Calorie burn efficiency ↑
**For Health**: All metrics stable and within healthy ranges
**For Athletic Performance**: Optimized training loads across all metrics

### 💡 Integrated Health Insights
- **Holistic Patterns**: How different metrics support overall goals
- **Leading Indicators**: Which metrics predict others (steps → weight loss)
- **Lagging Indicators**: Which metrics confirm progress (BP improvement)
- **Plateau Detection**: When multiple metrics stagnate simultaneously

### 📊 Statistical Tool Applications
- **Central Tendencies**: mean, median, mode for typical values
- **Variability**: variance, stddev, range_stat for consistency
- **Distribution**: quartiles, percentile for goal setting
- **Outliers**: iqr for identifying concerning readings
- **Extremes**: min_value, max_value for performance ranges

### 🎯 Personalized Recommendations
Based on your selected metric and goal type:
1. Choose the specific metric analysis above
2. Focus on tools most relevant to your goal
3. Compare results across time periods
4. Set realistic targets based on statistical insights
5. Monitor trends rather than daily fluctuations

### ⚙️ Execution Instructions
Specify the metric_type parameter as one of:
- "steps" for step count analysis
- "calories" for calorie burn analysis  
- "heart_rate" for cardiovascular analysis
- "weight" for weight tracking analysis
- "blood_pressure" for BP monitoring

Use MCP statistical tools for ALL calculations to ensure precision and enable deeper insights into your health and fitness journey."""