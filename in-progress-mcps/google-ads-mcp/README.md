# Google Ads MCP Setup Documentation

## Overview

**Repository**: [cohnen/mcp-google-ads](https://github.com/cohnen/mcp-google-ads)
**Status**: ⏳ In Progress - Installation complete, awaiting credentials
**Date Started**: August 8, 2025
**Installation Method**: Python-based with virtual environment

## Description

The Google Ads MCP server allows Claude Desktop to interact with Google Ads data through natural language conversations. It provides access to campaign information, performance metrics, keyword analytics, and ad management capabilities.

## Installation Steps Completed ✅

### 1. Repository Setup
```bash
# Cloned repository to Desktop
cd ~/Desktop
git clone https://github.com/cohnen/mcp-google-ads.git
```

### 2. Python Environment Configuration
```bash
# Created virtual environment with Python 3.11
/opt/homebrew/bin/python3.11 -m venv venv

# Activated virtual environment
source venv/bin/activate

# Installed dependencies
pip install --upgrade pip
pip install mcp python-dotenv google-auth google-auth-oauthlib google-auth-httplib2 requests
```

### 3. Environment File Created
Created `.env` file at `~/Desktop/mcp-google-ads/.env` with template:
```env
# Google Ads MCP Environment Configuration

# Authentication Type (choose one: "oauth" or "service_account")
GOOGLE_ADS_AUTH_TYPE=oauth

# Credentials Path
GOOGLE_ADS_CREDENTIALS_PATH=/Users/v0687/Desktop/mcp-google-ads/credentials.json

# Google Ads Developer Token (required)
GOOGLE_ADS_DEVELOPER_TOKEN=YOUR_DEVELOPER_TOKEN_HERE

# Manager Account ID (optional, for MCC accounts)
GOOGLE_ADS_LOGIN_CUSTOMER_ID=

# OAuth-specific config
GOOGLE_ADS_CLIENT_ID=YOUR_CLIENT_ID_HERE
GOOGLE_ADS_CLIENT_SECRET=YOUR_CLIENT_SECRET_HERE
```

### 4. Claude Desktop Configuration Updated
Added to `~/Library/Application Support/Claude/claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "google-ads": {
      "command": "~/Desktop/mcp-google-ads/venv/bin/python",
      "args": ["~/Desktop/mcp-google-ads/google_ads_server.py"],
      "env": {
        "PYTHONPATH": "~/Desktop/mcp-google-ads"
      }
    }
  }
}
```

## Remaining Tasks 🔄

### 1. Obtain Google Ads Developer Token
- [ ] Go to https://ads.google.com/aw/apicenter
- [ ] Sign in with Google Ads account
- [ ] Navigate to "API Center" → "API Access"
- [ ] Copy Developer Token
- [ ] Update `GOOGLE_ADS_DEVELOPER_TOKEN` in `.env`

### 2. Create OAuth 2.0 Credentials
- [ ] Visit https://console.cloud.google.com/
- [ ] Create new project or select existing
- [ ] Enable Google Ads API:
  - Go to "APIs & Services" → "Library"
  - Search for "Google Ads API"
  - Enable the API
- [ ] Create OAuth 2.0 credentials:
  - Go to "APIs & Services" → "Credentials"
  - Click "Create Credentials" → "OAuth client ID"
  - Choose "Desktop app" as application type
  - Name it (e.g., "Google Ads MCP")
  - Download JSON file
- [ ] Save JSON as `~/Desktop/mcp-google-ads/credentials.json`
- [ ] Update `.env` with Client ID and Secret from JSON

### 3. Test the Setup
- [ ] Run test script:
  ```bash
  cd ~/Desktop/mcp-google-ads
  source venv/bin/activate
  python test_google_ads_mcp.py
  ```
- [ ] Verify connection successful

### 4. Restart Claude Desktop
- [ ] Quit Claude Desktop completely (Cmd+Q)
- [ ] Reopen Claude Desktop
- [ ] Verify Google Ads MCP appears in available tools

## File Locations

- **MCP Server**: `~/Desktop/mcp-google-ads/`
- **Virtual Environment**: `~/Desktop/mcp-google-ads/venv/`
- **Configuration**: `~/Desktop/mcp-google-ads/.env`
- **Claude Config**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Setup Guide**: `~/Desktop/mcp-google-ads/SETUP_COMPLETE.md`

## Blockers & Issues

### Current Blockers
1. **Google Ads Developer Token Required**: Need to apply for and receive developer token from Google Ads API Center
2. **OAuth Credentials**: Requires Google Cloud Console access and project setup
3. **Account Access**: Requires active Google Ads account with API access enabled

### Potential Issues
- Test tokens have limited functionality
- Production token approval may take time
- OAuth flow requires manual authentication on first use

## Resources

- [Google Ads API Documentation](https://developers.google.com/google-ads/api/docs/start)
- [Google Cloud Console](https://console.cloud.google.com/)
- [Google Ads API Center](https://ads.google.com/aw/apicenter)
- [MCP Protocol Documentation](https://modelcontextprotocol.io/)
- [Repository Issues](https://github.com/cohnen/mcp-google-ads/issues)

## Testing Capabilities

Once configured, the MCP should enable:
- Listing Google Ads accounts
- Executing GAQL queries
- Retrieving campaign performance data
- Analyzing ad performance metrics
- Running custom Google Ads Query Language queries

## Notes

- Python version requirement: Python 3.10+ (using 3.11)
- MCP package version: 0.0.11+
- Authentication supports both OAuth and Service Account methods
- Installation automated via Terminal and osascript
- Configuration backup created with timestamp

## Alternative Implementations

Other Google Ads MCP servers found:
- `gomarble-ai/google-ads-mcp-server` - FastMCP-powered alternative
- Official Google exploration of MCP support (announced July 2025, not yet released)

## Next Steps

1. Obtain necessary credentials from Google
2. Complete configuration in `.env` file
3. Test connection with provided test scripts
4. Move to `working-mcps` once fully operational