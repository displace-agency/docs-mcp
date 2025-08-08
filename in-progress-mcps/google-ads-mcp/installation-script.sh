#!/bin/bash
# Google Ads MCP Installation Script
# Created: August 8, 2025
# This script was used to automate the installation process

# Clone repository
cd ~/Desktop
git clone https://github.com/cohnen/mcp-google-ads.git
cd mcp-google-ads

# Create Python virtual environment
/opt/homebrew/bin/python3.11 -m venv venv

# Activate and install dependencies
source venv/bin/activate
pip install --upgrade pip
pip install mcp python-dotenv google-auth google-auth-oauthlib google-auth-httplib2 requests

# Create .env file template
cat > .env << 'EOF'
# Google Ads MCP Environment Configuration

# Authentication Type (choose one: "oauth" or "service_account")
GOOGLE_ADS_AUTH_TYPE=oauth

# Credentials Path
GOOGLE_ADS_CREDENTIALS_PATH=/Users/v0687/Desktop/mcp-google-ads/credentials.json

# Google Ads Developer Token (required)
GOOGLE_ADS_DEVELOPER_TOKEN=YOUR_DEVELOPER_TOKEN_HERE

# Manager Account ID (optional, for MCC accounts)
GOOGLE_ADS_LOGIN_CUSTOMER_ID=

# For OAuth-specific config
GOOGLE_ADS_CLIENT_ID=YOUR_CLIENT_ID_HERE
GOOGLE_ADS_CLIENT_SECRET=YOUR_CLIENT_SECRET_HERE
EOF

echo "Installation complete! Next steps:"
echo "1. Get your Google Ads Developer Token"
echo "2. Create OAuth 2.0 credentials in Google Cloud Console"
echo "3. Update the .env file with your credentials"
echo "4. Run the Claude configuration update script"