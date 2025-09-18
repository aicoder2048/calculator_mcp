# Calculator MCP Server

一个全面的数学计算 MCP (Model Context Protocol) 服务器，为 Claude Code 提供强大的数学计算功能。该服务器使用 FastMCP 框架构建，提供多种数学运算工具和智能提示功能。

## 功能特性

### 🧮 核心计算工具 (Tools)
- **基础运算**: 加法、减法、乘法、除法
- **高级运算**: 乘方、开方、取余、阶乘
- **统计分析**: 平均值、中位数、标准差

### 📋 智能提示 (Prompts)
- **乘法表生成**: 自定义大小和起始数字的乘法表
- **方程求解**: 分步骤解方程的对话式提示
- **金融计算**: 复利计算提示
- **几何计算**: 圆形、三角形、矩形、球体的详细计算指导
- **单位换算**: 温度、长度、重量、速度、体积的全方位换算指导
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

### 统计分析工具

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

#### 查看所有功能
```
/list_all_assets
```
显示所有可用的工具和提示功能清单。

## 技术架构

### 项目结构
```
src/mcp_server/
├── server.py              # 主服务器文件
├── models/
│   └── schemas.py         # 数据模型定义
├── tools/                 # 计算工具实现
│   ├── add_tool.py
│   ├── subtract_tool.py
│   ├── multiply_tool.py
│   ├── divide_tool.py
│   ├── power_tool.py
│   ├── root_tool.py
│   ├── mod_tool.py
│   ├── factorial_tool.py
│   └── statistics_tool.py
└── prompts/              # 智能提示实现
    ├── multiplication_table_prompt.py
    ├── solve_equation_prompt.py
    ├── financial_calculation_prompt.py
    └── list_assets_prompt.py
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
