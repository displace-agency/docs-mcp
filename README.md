# MCP (Model Context Protocol) Documentation

This repository contains documentation for all installed and configured Model Context Protocol servers used with Claude Desktop App and Claude Code.

## Repository Structure

```
docs-mcp/
├── README.md                 # This file
└── working-mcps/            # Documentation for active MCP installations
    └── google-tag-manager-mcp.md
```

## Active MCP Servers

### 1. Google Tag Manager MCP
- **Status**: ✅ Installed (Desktop & CLI)
- **Provider**: Stape.ai
- **Documentation**: [google-tag-manager-mcp.md](working-mcps/google-tag-manager-mcp.md)
- **Use Case**: GTM container management and tag configuration

### 2. Vercel MCP
- **Status**: ✅ Installed (CLI)
- **Location**: `/Users/v0687/mcp-servers/mcp-vercel`
- **Use Case**: Vercel deployment management

### 3. Cloudflare MCP Suite
- **Status**: ✅ Installed (Desktop)
- **Components**: KV, Browser, R2
- **Use Case**: Cloudflare services management

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
1. Create file in `working-mcps/` directory
2. Include installation status at top
3. Document both Desktop and CLI configurations
4. List capabilities and limitations
5. Provide troubleshooting guide
6. Include security considerations

## Maintenance

- Review MCP configurations monthly
- Update documentation when changes occur
- Test MCP connectivity regularly
- Document any workarounds needed

---

**Last Updated**: August 17, 2025
**Maintained By**: v0687