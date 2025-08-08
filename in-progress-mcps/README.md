# In-Progress MCP Servers

## Overview

This directory contains documentation for MCP servers that are currently being set up or configured. These servers have been partially installed but require additional configuration or credentials before they can be fully operational.

## Current In-Progress MCPs

### 1. [Google Ads MCP](./google-ads-mcp/README.md)
- **Status**: Installation complete, awaiting credentials
- **Date Started**: August 8, 2025
- **Implementation**: cohnen/mcp-google-ads
- **Blocker**: Requires Google Ads API credentials and OAuth setup

## Progress Tracking

Each in-progress MCP has its own directory containing:
- Installation steps completed
- Configuration files created
- Remaining tasks
- Blockers or issues encountered
- Resources and documentation links

## Completion Criteria

An MCP moves from "in-progress" to "working" when:
1. All installation steps are complete
2. Required credentials are configured
3. The MCP successfully connects to Claude Desktop
4. Basic functionality has been tested and verified

## Failed Attempts

If an in-progress MCP cannot be completed after reasonable attempts, it should be moved to the `failed-mcps` directory with documentation on why it failed.

## Contributing

When adding a new in-progress MCP:
1. Create a new directory with the MCP name
2. Document all steps taken
3. Include configuration files and scripts
4. Note any blockers or issues
5. Update this README with the new entry