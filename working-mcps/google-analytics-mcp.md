# Google Analytics MCP Server

## Status: ✅ WORKING

**Installation Date:** August 8, 2025  
**Setup Time:** ~45 minutes (including troubleshooting)  
**Tested On:** macOS Sequoia, Claude Desktop

## Overview

The Google Analytics MCP server provides Claude with direct access to Google Analytics data through the Google Analytics Admin API and Data API. Successfully configured and tested with 6 Google Analytics properties across 2 accounts.

## Key Capabilities

- **Account Management**: List and manage Google Analytics accounts and properties
- **Reporting**: Run custom reports with date ranges, filters, and segments
- **Real-time Analytics**: Access real-time user data and activity
- **Metrics & Dimensions**: Access both standard and custom metrics/dimensions
- **Traffic Analysis**: Analyze sources, mediums, campaigns, and user behavior

## Installation Process

### Prerequisites
- macOS with Python 3.x
- Google account with Google Analytics access
- Claude Desktop application
- Homebrew (recommended)

### Step-by-Step Installation

#### 1. Install pipx
```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
export PATH="$HOME/.local/bin:$PATH"
```

#### 2. Install Google Cloud CLI
```bash
brew install google-cloud-sdk
```

#### 3. Authenticate with Google
```bash
# Login to Google Cloud
gcloud auth login

# Set up Application Default Credentials
gcloud auth application-default login \
    --scopes https://www.googleapis.com/auth/analytics.readonly,https://www.googleapis.com/auth/cloud-platform
```

#### 4. Configure Google Cloud Project
```bash
# Select or create a project
gcloud config set project YOUR_PROJECT_ID

# Enable required APIs
gcloud services enable analyticsadmin.googleapis.com
gcloud services enable analyticsdata.googleapis.com
```

#### 5. Install Google Analytics MCP Server
```bash
pipx install git+https://github.com/googleanalytics/google-analytics-mcp.git
```

#### 6. Configure Claude Desktop

Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "google-analytics": {
      "command": "/Users/YOUR_USERNAME/.local/bin/google-analytics-mcp",
      "args": [],
      "env": {
        "GOOGLE_CLOUD_PROJECT": "YOUR_PROJECT_ID",
        "GOOGLE_CLOUD_QUOTA_PROJECT": "YOUR_PROJECT_ID"
      }
    }
  }
}
```

#### 7. Set Quota Project in ADC

Critical step - update Application Default Credentials with quota project:

```python
#!/usr/bin/env python3
import json
import os

adc_path = os.path.expanduser("~/.config/gcloud/application_default_credentials.json")
with open(adc_path, 'r') as f:
    credentials = json.load(f)
credentials['quota_project_id'] = 'YOUR_PROJECT_ID'
with open(adc_path, 'w') as f:
    json.dump(credentials, f, indent=2)
```

#### 8. Restart Claude Desktop

Complete restart required (Cmd+Q, wait, reopen).

## Issues Encountered & Solutions

### Issue 1: Quota Project Error
**Error:** "API requires a quota project, which is not set by default"  
**Solution:** Must set quota_project_id in both ADC file and Claude environment variables

### Issue 2: pipx run Hanging
**Error:** `pipx run --spec` command hangs indefinitely  
**Solution:** Install directly with `pipx install` instead of using `pipx run`

### Issue 3: API Not Enabled
**Error:** "SERVICE_DISABLED"  
**Solution:** Enable both analyticsadmin and analyticsdata APIs (analyticsreporting v4 is optional)

### Issue 4: Authentication Scope
**Error:** Authentication failures  
**Solution:** Ensure both analytics.readonly and cloud-platform scopes are included

## Verification Tests

### Test 1: Server Initialization
```bash
echo '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0.0"}}}' | google-analytics-mcp
```

Expected: Returns server info with version 1.12.4

### Test 2: Claude Integration
Ask Claude: "What Google Analytics properties do I have access to?"

### Test 3: Data Retrieval
Ask Claude: "Show me traffic for [property] in the last 7 days"

## Working Features

✅ Account summaries retrieval  
✅ Property listing and details  
✅ Custom date range reports  
✅ Traffic source analysis  
✅ Device and browser analytics  
✅ User behavior metrics  
✅ Real-time data access  
✅ Custom dimensions and metrics  
✅ Multi-property support  

## Example Queries That Work

- "List all my Google Analytics properties"
- "Show me top pages for Draper Associates last week"
- "What's the bounce rate for mobile vs desktop?"
- "Get traffic sources breakdown for the last 30 days"
- "Show real-time active users"
- "Compare this week to last week's performance"

## File Locations

- **MCP Binary:** `~/.local/bin/google-analytics-mcp`
- **Claude Config:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **ADC Credentials:** `~/.config/gcloud/application_default_credentials.json`
- **Google Cloud Config:** `~/.config/gcloud/`

## Dependencies

- Python 3.10.9
- pipx 1.7.1
- Google Cloud SDK 533.0.0
- google-analytics-mcp 0.1.0

## Performance Notes

- Initial connection: ~2 seconds
- Query response time: 1-3 seconds for standard reports
- Memory usage: Minimal (~50MB)
- Supports concurrent queries

## Security Considerations

- Uses read-only API access
- Credentials stored locally in user directory
- No data caching between sessions
- Requires explicit Google account authentication

## Maintenance

- Check for updates: `pipx upgrade google-analytics-mcp`
- Rotate credentials periodically
- Monitor API quota usage in Google Cloud Console

## Resources

- [Official Repository](https://github.com/googleanalytics/google-analytics-mcp)
- [Google Analytics API Docs](https://developers.google.com/analytics)
- [MCP Protocol Docs](https://modelcontextprotocol.io)

## Support Status

**Official Support:** Yes - Google Analytics team maintains the repository  
**Community:** Active - Issues tracked on GitHub  
**Documentation:** Good - README and API documentation available  

---

*Last Updated: August 9, 2025*  
*Tested Version: 1.12.4*  
*Status: Fully Operational*
