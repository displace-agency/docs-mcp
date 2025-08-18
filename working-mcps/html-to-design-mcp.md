# HTML to Design MCP

## Overview
HTML to Design is a Figma plugin that allows you to convert HTML/CSS code directly into Figma designs. The MCP (Model Context Protocol) integration enables Claude to interact with this plugin seamlessly.

## Status
✅ **Working** - Successfully configured and operational

## Installation Date
August 18, 2025

## Configuration

### Claude Desktop/Web Configuration
Location: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "html-to-design": {
      "command": "uvx",
      "args": [
        "mcp-proxy",
        "--transport",
        "streamablehttp",
        "https://h2d-mcp.divriots.com/452905f5-77a4-4778-8ece-e4d86ce4b7df/mcp"
      ]
    }
  }
}
```

### Claude Code Configuration
Location: `~/.config/claude-code/mcp-settings.json`

```json
{
  "servers": {
    "html-to-design": {
      "command": "mcp-proxy",
      "args": [
        "--transport",
        "streamablehttp",
        "https://h2d-mcp.divriots.com/452905f5-77a4-4778-8ece-e4d86ce4b7df/mcp"
      ],
      "enabled": true
    }
  }
}
```

## Setup Instructions

### For Claude Desktop/Web
1. Open the Claude Desktop configuration file
2. Add the HTML to Design server configuration to the `mcpServers` object
3. Restart Claude Desktop application

### For Claude Code
1. Open the Claude Code MCP settings file
2. Add the HTML to Design server configuration to the `servers` object
3. Run `claude-code restart` in terminal

## Connection Details
- **MCP URL**: `https://h2d-mcp.divriots.com/452905f5-77a4-4778-8ece-e4d86ce4b7df/mcp`
- **Transport**: StreamableHTTP
- **Proxy**: Uses `mcp-proxy` (Claude Code) or `uvx` with mcp-proxy (Claude Desktop)

## Features
- Convert HTML/CSS code to Figma designs
- Direct integration with Figma through the plugin
- Streamable HTTP transport for efficient communication

## Prerequisites
- Active Figma account
- HTML to Design plugin installed in Figma
- Claude paid plan for MCP support

## Troubleshooting
- Ensure the Figma plugin is active and connected
- Verify the MCP URL is correctly configured
- Restart Claude applications after configuration changes
- Check that `uvx` or `mcp-proxy` is properly installed

## Notes
- The unique URL contains a user-specific token (452905f5-77a4-4778-8ece-e4d86ce4b7df)
- This MCP requires a paid Claude plan for full functionality
- Configuration can be done both on claude.ai and Claude Desktop