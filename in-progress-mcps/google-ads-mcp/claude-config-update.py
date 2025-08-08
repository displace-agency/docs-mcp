#!/usr/bin/env python3
"""
Claude Desktop Configuration Updater for Google Ads MCP
Created: August 8, 2025

This script updates the Claude Desktop configuration to include the Google Ads MCP server.
"""

import json
import os
from datetime import datetime
from pathlib import Path

def update_claude_config():
    """Update Claude Desktop configuration with Google Ads MCP server."""
    
    # Path to Claude config
    config_path = Path.home() / "Library" / "Application Support" / "Claude" / "claude_desktop_config.json"
    
    # Create directory if it doesn't exist
    config_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Read existing config or create new one
    if config_path.exists():
        # Backup existing config
        backup_path = config_path.with_suffix(f".backup.{datetime.now().strftime('%Y%m%d_%H%M%S')}")
        config_path.rename(backup_path)
        print(f"Backed up existing config to: {backup_path}")
        
        # Read the backup
        with open(backup_path, 'r') as f:
            config = json.load(f)
    else:
        config = {"mcpServers": {}}
    
    # Ensure mcpServers key exists
    if 'mcpServers' not in config:
        config['mcpServers'] = {}
    
    # Add Google Ads MCP server configuration
    config['mcpServers']['google-ads'] = {
        "command": str(Path.home() / "Desktop" / "mcp-google-ads" / "venv" / "bin" / "python"),
        "args": [str(Path.home() / "Desktop" / "mcp-google-ads" / "google_ads_server.py")],
        "env": {
            "PYTHONPATH": str(Path.home() / "Desktop" / "mcp-google-ads")
        }
    }
    
    # Write updated config
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)
    
    print("Claude configuration updated successfully!")
    print(f"Config saved to: {config_path}")
    print("\nNext steps:")
    print("1. Get your Google Ads Developer Token from: https://ads.google.com/aw/apicenter")
    print("2. Create OAuth 2.0 credentials in Google Cloud Console")
    print("3. Update the .env file with your credentials")
    print("4. Restart Claude Desktop for the changes to take effect")

if __name__ == "__main__":
    update_claude_config()