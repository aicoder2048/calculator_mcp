# Calculator MCP Server

一个全面的数学计算 MCP (Model Context Protocol) 服务器，为 Claude Code 提供强大的数学计算功能。该服务器使用 FastMCP 框架构建，提供多种数学运算工具和智能提示功能。

## 功能特性

### 🧮 核心计算工具 (Tools)
- **基础运算**: 加法、减法、乘法、除法
- **高级运算**: 乘方、开方、取余、阶乘
- **基础统计**: 平均值、中位数、标准差、最小/最大值、总和、计数、极差、方差、众数
- **高级统计**: 百分位数、四分位数、四分位距、几何平均、调和平均

### 📋 智能提示 (Prompts)
- **乘法表生成**: 自定义大小和起始数字的乘法表
- **方程求解**: 分步骤解方程的对话式提示
- **金融计算**: 复利计算提示
- **几何计算**: 圆形、三角形、矩形、球体的详细计算指导
- **单位换算**: 温度、长度、重量、速度、体积的全方位换算指导
- **贷款分期**: 月供、总利息、提前还款、还款方式对比分析
- **概率计算**: 排列、组合、二项分布、期望值、贝叶斯定理计算
- **健身分析**: 步数、卡路里、心率、体重、血压的健康数据统计分析
- **资产清单**: 列出所有可用工具和提示

## 安装配置

### Global Scope (全局安装)
使用 FastMCP 命令行工具安装到 Claude Code 全局配置：

```bash
uv run fastmcp install claude-code src/mcp_server/server.py --name calculator_mcp
```
> **注意**：fastmcp 还不支持在 Project Scope 安装!!! (很奇怪!)

### Project Scope (项目级安装)
在项目根目录下的 `.mcp.json` 文件中添加以下配置：

```json
{
  "mcpServers": {
    "calculator-mcp": {
      "command": "/opt/homebrew/bin/uv",
      "args": [
        "run",
        "python",
        "/Users/szou/Python/Playground/CalculatorMCP/src/mcp_server/server.py"
      ]
    }
  }
}
```

> **注意**: 请将路径 `/Users/szou/Python/Playground/CalculatorMCP/` 替换为你的实际项目路径。

## 可用工具详情

### 基础运算工具

#### `add` - 加法运算
```
参数: a (float), b (float)
返回: float
示例: add(5.5, 3.2) → 8.7
```

#### `subtract` - 减法运算
```
参数: a (float), b (float)
返回: float
示例: subtract(10, 3) → 7
```

#### `multiply` - 乘法运算
```
参数: a (float), b (float)
返回: float
示例: multiply(4, 5.5) → 22.0
```

#### `divide` - 除法运算
```
参数: a (float), b (float)
返回: dict (包含结果和余数)
示例: divide(15, 4) → {"quotient": 3.75, "remainder": 3}
```

### 高级运算工具

#### `power` - 乘方运算
```
参数: base (float), exponent (float)
返回: float
示例: power(2, 3) → 8.0
```

#### `root` - 开方运算
```
参数: number (float), n (int, 默认=2)
返回: float
示例: root(16, 2) → 4.0, root(27, 3) → 3.0
```

#### `mod` - 取余运算
```
参数: a (int), b (int)
返回: int
示例: mod(17, 5) → 2
```

#### `factorial` - 阶乘运算
```
参数: n (int)
返回: int
示例: factorial(5) → 120
```

### 统计分析工具 - 基础统计

#### `mean` - 平均值
```
参数: numbers (List[float])
返回: float
示例: mean([1, 2, 3, 4, 5]) → 3.0
```

#### `median` - 中位数
```
参数: numbers (List[float])
返回: float
示例: median([1, 2, 3, 4, 5]) → 3.0
```

#### `stddev` - 标准差
```
参数: numbers (List[float])
返回: float
示例: stddev([1, 2, 3, 4, 5]) → 1.58
```

#### `min_value` - 最小值
```
参数: numbers (List[float])
返回: float
示例: min_value([5, 2, 8, 1, 9]) → 1
```

#### `max_value` - 最大值
```
参数: numbers (List[float])
返回: float
示例: max_value([5, 2, 8, 1, 9]) → 9
```

#### `sum` - 总和
```
参数: numbers (List[float])
返回: float
示例: sum([1, 2, 3, 4, 5]) → 15
```

#### `count` - 计数
```
参数: numbers (List[float])
返回: int
示例: count([1, 2, 3, 4, 5]) → 5
```

#### `range_stat` - 极差
```
参数: numbers (List[float])
返回: float
示例: range_stat([1, 5, 3, 9, 2]) → 8
```

#### `variance` - 方差
```
参数: numbers (List[float])
返回: float
示例: variance([1, 2, 3, 4, 5]) → 2.5
```

#### `mode` - 众数
```
参数: numbers (List[float])
返回: float 或 List[float] (多个众数时)
示例: mode([1, 2, 2, 3, 2]) → 2
```

### 统计分析工具 - 高级统计

#### `percentile` - 百分位数
```
参数: numbers (List[float]), p (float, 0-100)
返回: float
示例: percentile([1, 2, 3, 4, 5], 50) → 3.0
```

#### `quartiles` - 四分位数
```
参数: numbers (List[float])
返回: dict {Q1, Q2, Q3}
示例: quartiles([1, 2, 3, 4, 5, 6, 7, 8]) → {"Q1": 2.25, "Q2": 4.5, "Q3": 6.75}
```

#### `iqr` - 四分位距
```
参数: numbers (List[float])
返回: float
示例: iqr([1, 2, 3, 4, 5, 6, 7, 8]) → 4.5
```

#### `geometric_mean` - 几何平均值
```
参数: numbers (List[float], 必须为正数)
返回: float
示例: geometric_mean([2, 4, 8]) → 4.0
```

#### `harmonic_mean` - 调和平均值
```
参数: numbers (List[float], 必须为正数)
返回: float
示例: harmonic_mean([1, 2, 4]) → 1.71
```

## 智能提示功能

### `build_multiplication_table` - 乘法表生成
生成自定义乘法表的提示，支持指定大小和起始数字。

**使用方法**: `/build_multiplication_table`
**参数**:
- `size` (int, 默认=10): 乘法表大小
- `start` (int, 默认=1): 起始数字

### `solve_equation_conversation` - 方程求解对话
启动分步骤解方程的对话式提示。

**使用方法**: `/solve_equation_conversation`
**参数**:
- `equation` (str): 要求解的方程

### `financial_calculation_prompt` - 金融计算
生成复利计算的提示和指导。

**使用方法**: `/financial_calculation_prompt`
**参数**:
- `principal` (float): 本金
- `rate` (float): 利率
- `time` (int): 时间（年）

### `geometry_calculation` - 几何计算
生成几何形状的详细计算步骤，包含目标、子目标和分步MCP工具调用指导。

**使用方法**: `/geometry_calculation`
**参数**:
- `shape` (str): 形状类型（circle、triangle、rectangle、sphere）
- `dimension1` (float): 第一个维度（如半径、长度、边a）
- `dimension2` (float, 可选): 第二个维度（如宽度、高度、边b）
- `dimension3` (float, 可选): 第三个维度（仅用于三角形的第三条边）

**支持的形状**:
- **圆形 (circle)**: 需要半径，计算面积、周长、对应球体属性
- **三角形 (triangle)**: 
  - 底和高模式：需要底边和高度
  - 三边模式：需要三条边长，使用海伦公式
- **矩形 (rectangle)**: 需要长和宽，计算面积、周长、对角线
- **球体 (sphere)**: 需要半径，计算表面积、体积、大圆周长

### `unit_conversion` - 单位换算
生成单位换算的详细步骤指导，包含换算公式、验证方法和实际应用场景。

**使用方法**: `/unit_conversion`
**参数**:
- `conversion_type` (str): 换算类型（temperature、length、weight/mass、speed/velocity、volume）
- `value` (float): 需要换算的数值
- `from_unit` (str, 可选): 源单位
- `to_unit` (str, 可选): 目标单位

**支持的换算类型**:
- **温度 (temperature)**: 摄氏度、华氏度、开尔文之间的换算
- **长度 (length)**: 公制、英制长度单位换算（km、m、cm、mm、miles、feet、inches等）
- **重量 (weight/mass)**: 质量单位换算（kg、g、pounds、ounces等）
- **速度 (speed/velocity)**: 速度单位换算（m/s、km/h、mph、knots等）
- **体积 (volume)**: 容积单位换算（liters、gallons、ml、cups等）

### `loan_amortization` - 贷款分期计算
生成贷款分期还款的详细分析，包含月供计算、利息分析、提前还款和还款方式对比。

**使用方法**: `/loan_amortization`
**参数**:
- `principal` (float): 贷款本金
- `annual_rate` (float): 年利率（百分比）
- `term_years` (int): 贷款期限（年）
- `calculation_type` (str, 可选): 计算类型，默认为"monthly_payment"

**支持的计算类型**:
- **月供计算 (monthly_payment/payment)**: 计算固定月供金额、总成本、利息分解
- **总利息分析 (total_interest/interest)**: 专注分析贷款生命周期的总利息成本
- **提前还款 (early_payoff/prepayment)**: 分析额外本金还款的影响和节省
- **还款方式对比 (comparison/equal_principal)**: 等额本息 vs 等额本金还款方式对比

### `probability_calculation` - 概率计算
生成概率论和组合数学的详细计算指导，包含排列组合、概率分布和统计推理。

**使用方法**: `/probability_calculation`
**参数**:
- `calculation_type` (str): 计算类型（permutation、combination、binomial、expected_value、bayes）
- `n` (int, 可选): 总数量或试验次数
- `r` (int, 可选): 选择数量或成功次数
- `probability` (float, 可选): 成功概率（用于二项分布）
- `trials` (int, 可选): 试验次数（用于二项分布）

**支持的计算类型**:
- **排列 (permutation/arrangement)**: 计算P(n,r)，顺序重要的排列数
- **组合 (combination/choose)**: 计算C(n,r)，顺序无关的组合数
- **二项概率 (binomial/binomial_probability)**: 计算二项分布概率P(X=k)
- **期望值 (expected_value/expectation)**: 计算概率分布的期望值E(X)
- **贝叶斯 (bayes/conditional)**: 计算条件概率和贝叶斯推理

### `list_all_assets` - 资产清单
列出所有可用的工具和提示功能。

**使用方法**: `/list_all_assets`

## 使用示例

### 工具使用示例

#### 基础计算
```
# 加法运算
@calculator-mcp add 25.5 14.3

# 乘方运算
@calculator-mcp power 2 10

# 统计分析
@calculator-mcp mean [85, 92, 78, 96, 88]
```

#### 复杂计算组合
```
# 计算复合表达式: (5 + 3) * 2^3
@calculator-mcp add 5 3          # 结果: 8
@calculator-mcp power 2 3        # 结果: 8
@calculator-mcp multiply 8 8     # 结果: 64
```

### Slash Commands 示例

#### 生成乘法表
```
/build_multiplication_table size:12 start:1
```
生成 1-12 的乘法表提示。

#### 求解方程
```
/solve_equation_conversation equation:"2x + 5 = 15"
```
启动求解线性方程的分步对话。

#### 金融计算
```
/financial_calculation_prompt principal:10000 rate:0.05 time:3
```
生成本金10000元，年利率5%，3年期复利计算的提示。

#### 几何计算
```
# 圆形计算（半径=5）
/geometry_calculation shape:"circle" dimension1:5.0

# 三角形计算（底=6，高=4）
/geometry_calculation shape:"triangle" dimension1:6.0 dimension2:4.0

# 三角形计算（三边：3, 4, 5 - 直角三角形）
/geometry_calculation shape:"triangle" dimension1:3.0 dimension2:4.0 dimension3:5.0

# 矩形计算（长=8，宽=6）
/geometry_calculation shape:"rectangle" dimension1:8.0 dimension2:6.0

# 球体计算（半径=7）
/geometry_calculation shape:"sphere" dimension1:7.0
```
生成带有详细目标和分步指导的几何计算提示，每个步骤都包含MCP工具调用说明。

#### 单位换算
```
# 温度换算（25摄氏度转华氏度）
/unit_conversion conversion_type:"temperature" value:25.0 from_unit:"celsius" to_unit:"fahrenheit"

# 长度换算（100米转英尺）
/unit_conversion conversion_type:"length" value:100.0 from_unit:"meters" to_unit:"feet"

# 重量换算（5公斤转磅）
/unit_conversion conversion_type:"weight" value:5.0 from_unit:"kilograms" to_unit:"pounds"

# 速度换算（60英里/小时转公里/小时）
/unit_conversion conversion_type:"speed" value:60.0 from_unit:"mph" to_unit:"km/h"

# 体积换算（4升转美制加仑）
/unit_conversion conversion_type:"volume" value:4.0 from_unit:"liters" to_unit:"gallons"

# 获取通用换算指导（不指定具体单位）
/unit_conversion conversion_type:"energy" value:100.0
```
生成详细的单位换算指导，包含换算公式、验证步骤、参考点和MCP工具调用说明。

#### 贷款分期计算
```
# 月供计算（25万贷款，4.5%年利率，30年）
/loan_amortization principal:250000.0 annual_rate:4.5 term_years:30 calculation_type:"monthly_payment"

# 总利息分析（30万贷款，5.0%年利率，20年）
/loan_amortization principal:300000.0 annual_rate:5.0 term_years:20 calculation_type:"total_interest"

# 提前还款分析（20万贷款，4.25%年利率，15年）
/loan_amortization principal:200000.0 annual_rate:4.25 term_years:15 calculation_type:"early_payoff"

# 还款方式对比（40万贷款，3.75%年利率，25年）
/loan_amortization principal:400000.0 annual_rate:3.75 term_years:25 calculation_type:"comparison"

# 默认月供计算（不指定calculation_type）
/loan_amortization principal:180000.0 annual_rate:5.5 term_years:30
```
生成详细的贷款分析，包含分步的MCP工具计算、财务洞察、验证步骤和实用建议。

#### 概率计算
```
# 排列计算（10选3的排列数）
/probability_calculation calculation_type:"permutation" n:10 r:3

# 组合计算（彩票：49选6）
/probability_calculation calculation_type:"combination" n:49 r:6

# 二项分布（20次试验中15次成功，成功率80%）
/probability_calculation calculation_type:"binomial" n:20 r:15 probability:0.8

# 期望值计算（投资回报期望）
/probability_calculation calculation_type:"expected_value"

# 贝叶斯推理（医学诊断概率更新）
/probability_calculation calculation_type:"bayes"

# 通用概率指导（不指定具体参数）
/probability_calculation calculation_type:"general_guide"
```
生成详细的概率和组合数学指导，包含公式推导、MCP工具计算步骤、实际应用场景和验证方法。

#### 健身数据分析
```
# 步数分析（每日分析，减重目标）
/fitness_analytics metric_type:"steps" time_period:"daily" goal_type:"weight_loss"

# 心率分析（每周分析，运动训练目标）
/fitness_analytics metric_type:"heart_rate" time_period:"weekly" goal_type:"athletic_training"

# 血压监控（每月分析，健康监控）
/fitness_analytics metric_type:"blood_pressure" time_period:"monthly" goal_type:"health_monitoring"

# 体重追踪（每周分析，减重目标）
/fitness_analytics metric_type:"weight" time_period:"weekly" goal_type:"weight_loss"

# 卡路里分析（每日分析，健身改善）
/fitness_analytics metric_type:"calories" time_period:"daily" goal_type:"fitness_improvement"

# 默认参数（步数，每周，健康监控）
/fitness_analytics metric_type:"steps"

# 季度健康综合分析
/fitness_analytics metric_type:"heart_rate" time_period:"quarterly" goal_type:"health_monitoring"
```
生成详细的健身数据统计分析，包含：
- 健康指标的统计描述（均值、方差、范围、分位数）
- 时间趋势分析和模式识别  
- 目标导向的健康建议和优化策略
- MCP统计工具的分步计算指导
- 健康风险评估和安全注意事项

### `fitness_analytics` - 健身数据分析
生成健身和健康数据的统计分析，包含多种健康指标的详细分析和趋势监控。

**使用方法**: `/fitness_analytics`
**参数**:
- `metric_type` (str): 健康指标类型（steps、calories、heart_rate、weight、blood_pressure）
- `time_period` (str, 默认="weekly"): 分析周期（daily、weekly、monthly、quarterly）
- `goal_type` (str, 默认="health_monitoring"): 健身目标（weight_loss、fitness_improvement、health_monitoring、athletic_training）

**支持的健康指标**:
- **步数分析 (steps)**: 日常活动量评估，步数目标追踪，活动模式识别
- **卡路里分析 (calories)**: 能量消耗分析，代谢评估，减重/增重指导
- **心率分析 (heart_rate)**: 心血管健康监控，运动强度分析，静息心率趋势
- **体重分析 (weight)**: 体重变化趋势，减重/增重进度，健康体重范围评估
- **血压分析 (blood_pressure)**: 血压监控，心血管风险评估，健康警报

**分析周期选项**:
- **日常 (daily)**: 每日数据变化和短期波动分析
- **每周 (weekly)**: 周度趋势和模式识别
- **每月 (monthly)**: 月度进展追踪和长期趋势
- **季度 (quarterly)**: 长期健康趋势和年度目标评估

**健身目标类型**:
- **减重 (weight_loss)**: 针对减重目标的数据分析和建议
- **健身改善 (fitness_improvement)**: 提升体能和运动表现的指导
- **健康监控 (health_monitoring)**: 日常健康状态跟踪和预防
- **运动训练 (athletic_training)**: 专业运动表现优化和训练指导

**统计工具集成**: 每个指标分析都使用10+种统计工具进行深度分析：
- 基础统计: mean, variance, stddev, min_value, max_value, range_stat
- 分布分析: percentile, quartiles, iqr, mode
- 趋势分析: 时间序列模式，异常值检测，健康范围对比

#### 查看所有功能
```
/list_all_assets
```
显示所有可用的工具和提示功能清单。

## 技术架构

### 项目结构
```
CalculatorMCP/
├── README.md                     # 项目说明文档
├── pyproject.toml               # Python 项目配置
├── .mcp.json                    # MCP 服务器配置
├── CLAUDE.md                    # 开发指南
├── src/
│   └── mcp_server/              # MCP 服务器主目录
│       ├── __init__.py
│       ├── server.py            # 主服务器文件 - FastMCP 服务器实例
│       ├── models/              # 数据模型定义
│       │   ├── __init__.py
│       │   └── schemas.py       # Pydantic 数据验证模型
│       ├── tools/               # 计算工具实现 (23个工具)
│       │   ├── __init__.py
│       │   ├── add_tool.py      # 加法运算
│       │   ├── subtract_tool.py # 减法运算
│       │   ├── multiply_tool.py # 乘法运算
│       │   ├── divide_tool.py   # 除法运算
│       │   ├── power_tool.py    # 乘方运算
│       │   ├── root_tool.py     # 开方运算
│       │   ├── mod_tool.py      # 取余运算
│       │   ├── factorial_tool.py # 阶乘运算
│       │   └── statistics_tool.py # 统计分析工具 (15种统计函数)
│       └── prompts/             # 智能提示实现 (9个提示)
│           ├── __init__.py
│           ├── list_assets_prompt.py           # 资产清单提示
│           ├── multiplication_table_prompt.py  # 乘法表生成
│           ├── solve_equation_prompt.py        # 方程求解对话
│           ├── financial_calculation_prompt.py # 金融计算指导
│           ├── geometry_calculation_prompt.py  # 几何计算指导
│           ├── unit_conversion_prompt.py       # 单位换算指导
│           ├── loan_amortization_prompt.py     # 贷款分期分析
│           ├── probability_calculation_prompt.py # 概率计算指导
│           └── fitness_analytics_prompt.py     # 健身数据分析 (新增)
├── tests/                       # 测试文件目录
│   ├── __init__.py
│   ├── test_tools/              # 工具测试 (95个测试)
│   │   ├── __init__.py
│   │   ├── test_add_tool.py
│   │   ├── test_subtract_tool.py
│   │   ├── test_multiply_tool.py
│   │   ├── test_divide_tool.py
│   │   ├── test_power_tool.py
│   │   ├── test_root_tool.py
│   │   ├── test_mod_tool.py
│   │   ├── test_factorial_tool.py
│   │   ├── test_statistics_tool.py         # 基础统计测试
│   │   ├── test_statistics_extended.py     # 扩展统计测试
│   │   └── test_statistics_server_tools.py # 服务器集成测试
│   └── test_prompts/            # 提示测试 (101个测试)
│       ├── __init__.py
│       ├── test_list_assets_prompt.py
│       ├── test_multiplication_table_prompt.py
│       ├── test_solve_equation_prompt.py
│       ├── test_financial_calculation_prompt.py
│       ├── test_geometry_calculation_prompt.py
│       ├── test_unit_conversion_prompt.py
│       ├── test_loan_amortization_prompt.py
│       ├── test_probability_calculation_prompt.py
│       └── test_fitness_analytics_prompt.py # 健身分析测试 (新增)
└── ai_docs/                     # AI 生成的文档
    └── [documentation files]
```

### 依赖要求
- Python 3.8+
- FastMCP 框架
- Pydantic (数据验证)
- uvicorn (ASGI 服务器)

## 开发说明

### 本地运行
```bash
# 安装依赖
uv sync

# 启动服务器
uv run python src/mcp_server/server.py
```

### 测试
```bash
# 运行所有测试
uv run pytest

# 运行特定测试
uv run pytest tests/test_tools/test_add_tool.py
```

## 许可证

本项目基于 MIT 许可证开源。

## 贡献

欢迎提交 Issue 和 Pull Request 来改进这个项目！
