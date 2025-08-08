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

## Common Patterns in Working MCPs

1. **NPX-based**: Most working MCPs use npx for package management
2. **Simple Authentication**: Environment variables or header-based auth
3. **Official Packages**: Many are official implementations (@modelcontextprotocol/*)
4. **Remote MCPs**: Some use mcp-remote for cloud-hosted servers
5. **Clear Error Messages**: Working MCPs provide clear feedback when misconfigured

## Key Success Factors

1. **Protocol Compliance**: Strict adherence to MCP protocol specification
2. **Error Handling**: Proper error messages and feedback
3. **Simple Setup**: Minimal configuration required
4. **Documentation**: Clear setup instructions
5. **Maintenance**: Regular updates and bug fixes

## Setup Best Practices

1. **Always restart Claude Desktop** after configuration changes
2. **Use absolute paths** for local files and executables
3. **Test environment variables** before adding to config
4. **Keep tokens secure** - never commit them to version control
5. **Monitor logs** during initial setup for debugging