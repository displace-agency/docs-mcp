# MCP (Model Context Protocol) Documentation

## Model Context Protocol Server Setup Documentation

This repository documents various attempts to set up MCP (Model Context Protocol) servers for Claude Desktop and Claude Code, including successful implementations, in-progress setups, and troubleshooting of failed attempts.

## Repository Structure

```
docs-mcp/
├── README.md                 # This file
├── working-mcps/            # Documentation for successfully configured MCP servers
│   └── google-tag-manager-mcp.md
├── in-progress-mcps/        # Documentation for MCP servers currently being configured
│   └── google-ads-mcp/      # Google Ads MCP (installation complete, awaiting credentials)
├── failed-mcps/             # Documentation for MCP servers that failed to work
│   └── shopify-mcp/         # Shopify MCP setup attempts (3 implementations tried)
└── troubleshooting/         # General MCP troubleshooting guides
```

## Quick Links

- [Failed MCPs Documentation](./failed-mcps/README.md)
- [In-Progress MCPs Documentation](./in-progress-mcps/README.md)
- [Working MCP Configurations](./working-mcps/README.md)
- [Troubleshooting Guide](./troubleshooting/README.md)

## Current Status (Updated: August 17, 2025)

### ✅ Working MCP Servers

1. **Google Tag Manager MCP** (NEW)
   - **Status**: ✅ Installed (Desktop & CLI)
   - **Provider**: Stape.ai
   - **Documentation**: [google-tag-manager-mcp.md](working-mcps/google-tag-manager-mcp.md)
   - **Use Case**: GTM container management and tag configuration

2. **Vercel MCP**
   - **Status**: ✅ Installed (CLI)
   - **Location**: `/Users/v0687/mcp-servers/mcp-vercel`
   - **Use Case**: Vercel deployment management

3. **Cloudflare MCP Suite**
   - **Status**: ✅ Installed (Desktop)
   - **Components**: KV, Browser, R2
   - **Use Case**: Cloudflare services management

4. **Other Working MCPs**:
   - filesystem
   - docker-k8s
   - webflow
   - github
   - klaviyo
   - hf-mcp-server (Hugging Face)

### ⏳ In-Progress MCP Servers
- **Google Ads** - Installation complete, awaiting API credentials

### ❌ Failed MCP Servers
- **Shopify** - Multiple implementations attempted, all failed with similar issues

## Configuration Locations

### Claude Desktop App
```
~/Library/Application Support/Claude/claude_desktop_config.json
```

### Claude Code (CLI)
```
~/.config/claude/claude_desktop_config.json
```

## Installation Guide

### Adding a New MCP

1. **Desktop App**:
   - Settings → Developer → MCP Servers
   - Add configuration
   - Restart app

2. **CLI**:
   - Edit `~/.config/claude/claude_desktop_config.json`
   - Add MCP configuration
   - Restart Claude Code

### Documentation Standards

When documenting a new MCP:
1. Create file in appropriate directory (`working-mcps/`, `in-progress-mcps/`, or `failed-mcps/`)
2. Include installation status at top
3. Document both Desktop and CLI configurations
4. List capabilities and limitations
5. Provide troubleshooting guide
6. Include security considerations

## Overview of MCP

The Model Context Protocol (MCP) is a protocol that allows Claude Desktop and Claude Code to interact with external services and tools through standardized server implementations. MCP servers act as bridges between Claude and various APIs, databases, and services.

## Key Findings

- Working MCPs share common patterns (NPX-based, official packages)
- Failed MCPs suffer from protocol incompatibility issues
- Silent failures make debugging extremely difficult
- Need for better MCP protocol standardization and documentation
- Python-based MCPs require specific Python versions (3.10+) for MCP package compatibility
- Some MCPs install successfully but tools may not be exposed in Claude's interface (e.g., GTM MCP)

## Maintenance

- Review MCP configurations monthly
- Update documentation when changes occur
- Test MCP connectivity regularly
- Document any workarounds needed

## Contributing

This is a private repository for internal documentation. Please document any new MCP setup attempts, whether successful, in-progress, or failed, to help build our knowledge base.

---

**Last Updated**: August 17, 2025
**Maintained By**: v0687

## License

Private repository - For internal use only
