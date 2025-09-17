def list_all_assets() -> str:
    """Generate a prompt to list all available tools and prompts with detailed information."""
    return """Please provide a comprehensive list of all available assets in this MCP server:

## Tools
List all available tools with:
- Tool name (function call name)
- Full function signature with parameter types
- Brief description of what the tool does
- Parameter details (name, type, description, constraints)
- Return type and format
- Example usage

## Prompts
List all available prompts with:
- Prompt name (function call name)
- Function signature with parameters
- Description of the prompt's purpose
- Parameters required
- Expected output format
- Example usage

Please organize the information in a clear, structured format."""