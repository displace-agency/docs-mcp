# MCP Documentation

## Model Context Protocol (MCP) Server Setup Documentation

This repository documents various attempts to set up MCP (Model Context Protocol) servers for Claude Desktop, including successful implementations and troubleshooting of failed attempts.

## Repository Structure

- `/shopify-mcp/` - Documentation for Shopify MCP setup attempts
- `/working-mcps/` - Documentation for successfully configured MCP servers
- `/troubleshooting/` - General MCP troubleshooting guides
- `/configs/` - Example configuration files

## Quick Links

- [Shopify MCP Setup Attempts](./shopify-mcp/README.md)
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

### ❌ Non-functional MCP Servers
- Shopify (multiple implementations attempted)

## Contributing

Feel free to contribute documentation for your own MCP setup experiences by submitting a pull request.

## License

MIT License - Feel free to use this documentation for your own MCP setups.