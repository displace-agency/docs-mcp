# MCP Documentation

## Model Context Protocol (MCP) Server Setup Documentation

This repository documents various attempts to set up MCP (Model Context Protocol) servers for Claude Desktop, including successful implementations, in-progress setups, and troubleshooting of failed attempts.

## Repository Structure

- `/failed-mcps/` - Documentation for MCP servers that failed to work
  - `/shopify-mcp/` - Shopify MCP setup attempts (3 implementations tried)
- `/in-progress-mcps/` - Documentation for MCP servers currently being configured
  - `/google-ads-mcp/` - Google Ads MCP (installation complete, awaiting credentials)
- `/working-mcps/` - Documentation for successfully configured MCP servers
- `/troubleshooting/` - General MCP troubleshooting guides

## Quick Links

- [Failed MCPs Documentation](./failed-mcps/README.md)
- [In-Progress MCPs Documentation](./in-progress-mcps/README.md)
- [Working MCP Configurations](./working-mcps/README.md)
- [Troubleshooting Guide](./troubleshooting/README.md)

## Overview of MCP

The Model Context Protocol (MCP) is a protocol that allows Claude Desktop to interact with external services and tools through standardized server implementations. MCP servers act as bridges between Claude and various APIs, databases, and services.

## Current Status (August 8, 2025)

### ✅ Working MCP Servers
- filesystem
- docker-k8s
- vercel
- webflow
- github
- klaviyo
- hf-mcp-server (Hugging Face)

### ⏳ In-Progress MCP Servers
- **Google Ads** - Installation complete, awaiting API credentials

### ❌ Failed MCP Servers
- **Shopify** - Multiple implementations attempted, all failed with similar issues

## Key Findings

- Working MCPs share common patterns (NPX-based, official packages)
- Failed MCPs suffer from protocol incompatibility issues
- Silent failures make debugging extremely difficult
- Need for better MCP protocol standardization and documentation
- Python-based MCPs require specific Python versions (3.10+) for MCP package compatibility

## Contributing

This is a private repository for internal documentation. Please document any new MCP setup attempts, whether successful, in-progress, or failed, to help build our knowledge base.

## License

Private repository - For internal use only