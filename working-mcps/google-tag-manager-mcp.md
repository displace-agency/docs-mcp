# Google Tag Manager MCP (Model Context Protocol)

> ⚠️ **Installation Status**: Installed in both **Claude Desktop App** and **Claude Code**

## Overview
The Google Tag Manager MCP enables Claude to interact with Google Tag Manager containers, allowing for programmatic management of tags, triggers, and variables. This MCP is provided by Stape.ai and connects via their secure server-side endpoint.

## Installation Date
**August 17, 2025**

## Installation Locations

### 1. Claude Desktop App
**Config Location**: `/Users/v0687/Library/Application Support/Claude/claude_desktop_config.json`
```json
{
  "mcpServers": {
    "google-tag-manager-mcp-server": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://gtm-mcp.stape.ai/sse"
      ]
    }
  }
}
```

### 2. Claude Code (CLI)
**Config Location**: `/Users/v0687/.config/claude/claude_desktop_config.json`
```json
{
  "mcpServers": {
    "google-tag-manager-mcp-server": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://gtm-mcp.stape.ai/sse"
      ]
    }
  }
}
```

## MCP Details

### Server Information
- **Provider**: Stape.ai
- **Endpoint**: `https://gtm-mcp.stape.ai/sse`
- **Protocol**: Server-Sent Events (SSE)
- **Connection Type**: Remote MCP via npx

### Authentication
- **Method**: OAuth through Stape.ai portal
- **Status**: ✅ Authorized and connected
- **Google Account**: Linked via OAuth flow

## Capabilities

### What This MCP Can Do (Theoretical)

1. **Container Management**:
   - List GTM containers
   - Access container configurations
   - View container versions
   - Export/Import container settings

2. **Tag Operations**:
   - Create new tags
   - Update existing tags
   - Delete tags
   - Configure tag firing rules

3. **Trigger Management**:
   - Create custom triggers
   - Modify trigger conditions
   - Set up event listeners
   - Configure page view triggers

4. **Variable Configuration**:
   - Define custom variables
   - Set up data layer variables
   - Configure constant variables
   - Create lookup tables

5. **Version Control**:
   - Create new versions
   - Publish container versions
   - Preview changes
   - Rollback to previous versions

### Current Limitations

⚠️ **Important Note**: While the MCP is successfully installed and configured, the actual tool functions are not currently accessible in the Claude interface. This appears to be a limitation where:
- The MCP server is connected and authenticated
- The configuration is properly set up
- But the specific GTM tools/functions are not exposed to Claude's tool interface

## Use Cases Attempted

### Successfully Completed
1. ✅ MCP installation and configuration
2. ✅ Authentication with Google account
3. ✅ Connection to Stape.ai endpoint

### Attempted but Not Available
1. ❌ Direct tag creation via MCP tools
2. ❌ Programmatic container updates
3. ❌ Automated trigger configuration

## Workaround Solution Implemented

Since direct MCP tool access wasn't available, we successfully used an alternative approach:

1. **Created Enhanced GTM Container JSON**:
   ```json
   {
     "exportFormatVersion": 2,
     "containerVersion": {
       "tag": [/* GA4, Clarity, Custom Events */],
       "trigger": [/* All Pages, CTA Clicks, Form Submits */],
       "variable": [/* Custom Variables */]
     }
   }
   ```

2. **Manual Import Process**:
   - Generated comprehensive container configuration
   - Exported as JSON file
   - Imported via GTM web interface
   - Successfully published changes

## Container Configuration Created

### Container ID: GTM-NSHK59WL

**Tags Configured**:
1. Google Analytics 4 Configuration (G-90E691SG46)
2. Microsoft Clarity (sw7vd39iuc)
3. GA4 CTA Click Event
4. GA4 Form Submit Event

**Triggers Created**:
1. All Pages (Pageview)
2. CTA Button Clicks
3. Form Submissions

**Variables Defined**:
1. GA4 Measurement ID
2. Clarity Project ID
3. Built-in click and form variables

## Installation Process

### Step 1: Initial MCP Setup
```bash
# MCP was installed via Claude Desktop App UI
# Automatically added to configuration
```

### Step 2: Configuration Sync
```bash
# Copied configuration to Claude Code config
# Located at ~/.config/claude/claude_desktop_config.json
```

### Step 3: Authorization
- Clicked authorization link in Claude Desktop
- Completed Google OAuth flow
- Granted permissions to GTM containers

### Step 4: Verification
```bash
# Checked both config files
cat ~/Library/Application\ Support/Claude/claude_desktop_config.json
cat ~/.config/claude/claude_desktop_config.json
```

## Troubleshooting

### Issue: MCP Tools Not Accessible
**Problem**: Despite successful installation, GTM-specific tools not available in Claude's tool list

**Attempted Solutions**:
1. Restarted Claude applications
2. Verified configuration in both locations
3. Checked MCP server connectivity

**Resolution**: Used alternative JSON import method for GTM configuration

### Issue: Configuration Sync
**Problem**: MCP only appeared in Desktop app, not CLI

**Solution**: Manually copied configuration to CLI config file:
```bash
# Added google-tag-manager-mcp-server block to:
~/.config/claude/claude_desktop_config.json
```

## Future Improvements

### Potential Enhancements
1. **Full Tool Access**: Work with Stape.ai to expose GTM tools in Claude interface
2. **Batch Operations**: Enable bulk tag/trigger management
3. **Version Automation**: Automatic version creation and publishing
4. **Container Backup**: Scheduled container configuration exports

### Expected Capabilities (When Fully Functional)
- Real-time tag debugging
- Automated QA testing of tags
- Bulk migration between containers
- Template-based tag creation
- Cross-container synchronization

## Related Documentation

### Internal Docs
- [GTM Implementation](/Users/v0687/web-displace/documentation/03-deployment/03-google-tag-manager.md)
- [GTM Container JSON](/Users/v0687/web-displace/gtm-container-enhanced.json)

### External Resources
- [Stape.ai GTM MCP](https://gtm-mcp.stape.ai)
- [MCP Protocol Docs](https://modelcontextprotocol.com)
- [Google Tag Manager API](https://developers.google.com/tag-manager/api/v2)

## Security Considerations

### Access Control
- OAuth token stored securely by Stape.ai
- No credentials stored locally
- Read/write access to GTM containers
- Scoped to authorized Google account

### Best Practices
1. Regularly review MCP permissions
2. Rotate OAuth tokens periodically
3. Monitor container changes
4. Use version control for configurations

## Maintenance

### Regular Tasks
1. **Weekly**: Verify MCP connectivity
2. **Monthly**: Review and update configurations
3. **Quarterly**: Check for MCP updates from Stape.ai

### Update Process
```bash
# Check for updates
npx mcp-remote --version

# Update if needed (automatic via npx)
# Configuration persists across updates
```

## Status Summary

| Component | Status | Notes |
|-----------|--------|-------|
| Installation | ✅ Complete | Both Desktop and CLI |
| Configuration | ✅ Active | Properly configured |
| Authentication | ✅ Connected | OAuth authorized |
| Tool Access | ⚠️ Limited | Tools not exposed in Claude |
| Workaround | ✅ Successful | JSON import method works |

## Conclusion

The Google Tag Manager MCP is successfully installed and configured in both Claude Desktop App and Claude Code. While direct tool access is currently limited, the installation provides the foundation for future GTM automation capabilities. The JSON import workaround proved effective for implementing comprehensive tracking solutions.

**Last Updated**: August 17, 2025
**Maintained By**: v0687
**MCP Version**: Latest via npx