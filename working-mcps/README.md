# Working MCP Configurations

## Successfully Configured MCP Servers

This directory contains documentation for MCP servers that are working correctly with Claude Desktop.

## Working Servers List

### 1. Filesystem MCP
```json
{
  "filesystem": {
    "command": "npx",
    "args": [
      "-y",
      "@modelcontextprotocol/server-filesystem",
      "/Users/[username]/Desktop"
    ]
  }
}
```
**Status**: ✅ Working
**Functionality**: Provides file system access to specified directory

### 2. Docker-K8s MCP
```json
{
  "docker-k8s": {
    "command": "docker",
    "args": [
      "run",
      "-i",
      "--rm",
      "-v",
      "/Users/[username]/.kube:/home/appuser/.kube:ro",
      "ghcr.io/alexei-led/k8s-mcp-server:latest"
    ]
  }
}
```
**Status**: ✅ Working
**Functionality**: Kubernetes cluster management

### 3. Vercel MCP
```json
{
  "vercel": {
    "command": "/usr/local/bin/node",
    "args": [
      "/Users/[username]/mcp-servers/mcp-vercel/build/index.js"
    ],
    "env": {
      "VERCEL_API_TOKEN": "[TOKEN]"
    }
  }
}
```
**Status**: ✅ Working
**Functionality**: Vercel deployment management

### 4. Webflow MCP
```json
{
  "webflow": {
    "command": "npx",
    "args": [
      "-y",
      "mcp-remote",
      "https://mcp.webflow.com/sse"
    ]
  }
}
```
**Status**: ✅ Working
**Functionality**: Webflow site management

### 5. GitHub MCP
```json
{
  "github": {
    "command": "npx",
    "args": [
      "-y",
      "@modelcontextprotocol/server-github"
    ],
    "env": {
      "GITHUB_PERSONAL_ACCESS_TOKEN": "[TOKEN]"
    }
  }
}
```
**Status**: ✅ Working
**Functionality**: GitHub repository management

### 6. Klaviyo MCP
```json
{
  "klaviyo": {
    "command": "/opt/homebrew/Caskroom/miniconda/base/bin/uvx",
    "args": [
      "klaviyo-mcp-server@latest"
    ],
    "env": {
      "PRIVATE_API_KEY": "[KEY]",
      "READ_ONLY": "false"
    }
  }
}
```
**Status**: ✅ Working
**Functionality**: Klaviyo marketing automation

### 7. Hugging Face MCP
```json
{
  "hf-mcp-server": {
    "command": "npx",
    "args": [
      "mcp-remote",
      "https://huggingface.co/mcp",
      "--header",
      "Authorization: Bearer [TOKEN]"
    ]
  }
}
```
**Status**: ✅ Working
**Functionality**: Hugging Face model interaction

### 8. Google Analytics MCP
```json
{
  "google-analytics": {
    "command": "/Users/[username]/.local/bin/google-analytics-mcp",
    "args": [],
    "env": {
      "GOOGLE_CLOUD_PROJECT": "[PROJECT_ID]",
      "GOOGLE_CLOUD_QUOTA_PROJECT": "[PROJECT_ID]"
    }
  }
}
```
**Status**: ✅ Working (August 9, 2025)
**Functionality**: Google Analytics data access and reporting
**Documentation**: [Full Setup Guide](./google-analytics-mcp.md)

#### Key Requirements:
- Google Cloud project with Analytics APIs enabled
- Quota project configuration in ADC
- pipx installation (not npm/npx based)
- Authentication via gcloud CLI

### 9. HTML to Design MCP ⭐ NEW
```json
{
  "html-to-design": {
    "command": "uvx",
    "args": [
      "mcp-proxy",
      "--transport",
      "streamablehttp",
      "https://h2d-mcp.divriots.com/[USER_TOKEN]/mcp"
    ]
  }
}
```
**Status**: ✅ Working (August 18, 2025)
**Functionality**: Convert HTML/CSS to Figma designs
**Documentation**: [Full Setup Guide](./html-to-design-mcp.md)

#### Key Requirements:
- Figma account with HTML to Design plugin
- Claude paid plan for MCP support
- User-specific token from plugin setup

## Common Patterns in Working MCPs

1. **NPX-based**: Most working MCPs use npx for package management
2. **Simple Authentication**: Environment variables or header-based auth
3. **Official Packages**: Many are official implementations (@modelcontextprotocol/*)
4. **Remote MCPs**: Some use mcp-remote for cloud-hosted servers
5. **Clear Error Messages**: Working MCPs provide clear feedback when misconfigured
6. **Python MCPs**: Some use pipx/uvx for Python-based servers (Klaviyo, Google Analytics)

## Key Success Factors

1. **Protocol Compliance**: Strict adherence to MCP protocol specification
2. **Error Handling**: Proper error messages and feedback
3. **Simple Setup**: Minimal configuration required
4. **Documentation**: Clear setup instructions
5. **Maintenance**: Regular updates and bug fixes
6. **API Configuration**: Some require external API setup (Google Cloud, GitHub, etc.)

## Setup Best Practices

1. **Always restart Claude Desktop** after configuration changes
2. **Use absolute paths** for local files and executables
3. **Test environment variables** before adding to config
4. **Keep tokens secure** - never commit them to version control
5. **Monitor logs** during initial setup for debugging
6. **Check API quotas** for cloud-based services
7. **Verify authentication** before troubleshooting other issues

## Statistics

- **Total Working MCPs**: 9
- **NPX-based**: 4 (44.4%)
- **Python-based**: 3 (33.3%) - includes uvx/mcp-proxy
- **Docker-based**: 1 (11.1%)
- **Node.js direct**: 1 (11.1%)
