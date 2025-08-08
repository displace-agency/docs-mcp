# MCP Troubleshooting Guide

## Common Issues and Solutions

### Issue 1: MCP Server Loads but Tools Not Accessible

**Symptoms**:
- Server appears in Claude Desktop's MCP list
- Tools seem to be registered
- "Tool not found" errors when trying to use them

**Possible Causes**:
1. Protocol version mismatch
2. Tool naming convention issues
3. Incomplete initialization

**Solutions**:
1. Check MCP protocol version compatibility
2. Enable debug logging
3. Test server directly with JSON-RPC commands
4. Verify tool registration format

### Issue 2: Environment Variables Not Recognized

**Symptoms**:
- Authentication failures
- "Token required" errors
- Server fails to start

**Solutions**:
1. Check exact environment variable names in source code
2. Verify `.env` file format and location
3. Test with direct environment variable export
4. Check for typos in variable names

### Issue 3: Build Failures

**Symptoms**:
- TypeScript compilation errors
- Missing dependencies
- No dist/build directory created

**Solutions**:
1. Ensure Node.js version compatibility
2. Clear node_modules and reinstall
3. Check package.json for build scripts
4. Verify TypeScript configuration

## Debugging Commands

### Test MCP Server Directly
```bash
# Initialize request
echo '{"jsonrpc":"2.0","method":"initialize","params":{"capabilities":{}},"id":1}' | \
[ENV_VARS] node /path/to/server

# List tools
echo '{"jsonrpc":"2.0","method":"tools/list","id":1}' | \
[ENV_VARS] node /path/to/server
```

### Check Process Status
```bash
# Find MCP processes
ps aux | grep -i [mcp-name] | grep -v grep

# Check port usage (if applicable)
lsof -i :3000
```

### Verify Configuration
```bash
# Check Claude config
cat ~/Library/Application\ Support/Claude/claude_desktop_config.json | python3 -m json.tool

# Validate JSON syntax
jsonlint ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

## Configuration Best Practices

### 1. Use Absolute Paths
```json
{
  "command": "/usr/local/bin/node",
  "args": ["/Users/username/mcp-server/index.js"]
}
```

### 2. Environment Variables in Config
```json
{
  "env": {
    "API_KEY": "your-key-here",
    "OTHER_VAR": "value"
  }
}
```

### 3. Use NPX for npm packages
```json
{
  "command": "npx",
  "args": ["-y", "package-name"]
}
```

## Log Locations

- **Claude Desktop Logs**: `~/Library/Logs/Claude/`
- **Console Logs**: Use Console.app and filter by "Claude"
- **MCP Server Logs**: Depends on implementation, check stdout/stderr

## Testing Checklist

- [ ] Server builds successfully
- [ ] Environment variables are set correctly
- [ ] Server responds to initialize request
- [ ] Tools are listed when queried
- [ ] Claude Desktop has been restarted
- [ ] No conflicting MCP servers running
- [ ] Correct Node.js version installed
- [ ] All dependencies installed
- [ ] File permissions are correct
- [ ] Network connectivity (for remote MCPs)

## When All Else Fails

1. **Remove and Re-add**: Delete MCP from config, restart Claude, add again
2. **Check GitHub Issues**: Look for similar problems in the MCP repository
3. **Simplify Configuration**: Start with minimal config and add features
4. **Use Alternative Implementation**: Try different MCP server for same service
5. **Report Issue**: Create detailed bug report with logs and configuration