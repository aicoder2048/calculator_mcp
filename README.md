  在Claude Code上安装MCP

  uv run fastmcp install claude-code src/server.py --name calculator_mcp --project .

  接下来的步骤：

  1. 重启 Claude Code - 关闭并重新打开 Claude Code 以加载新的 MCP 服务器
  2. 验证安装 - 重启后，您可以通过以下方式验证服务器是否正常工作：
    - 在 Claude Code 中询问可用的工具
    - 尝试使用计算功能，例如：
    帮我计算 15 + 27
  计算 2^10 的值
  求数列 [1,2,3,4,5] 的平均值
  3. 可用的工具：
    - 基础算术：add, subtract, multiply, divide
    - 高级数学：power (乘方), root (开方), mod (余数), factorial (阶乘)
    - 统计：mean (平均值), median (中位数), stddev (标准差)
    - 提示模板：multiplication table, equation solver, financial calculations

  现在您的 Claude Code
  已经具备了完整的数学计算能力！您可以让我帮您测试任何数学运算。
