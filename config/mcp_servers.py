"""
Central registry of all MCP servers.

Every agent refers to servers by name.
The connection details live here.
"""

MCP_SERVERS = {
    "filesystem": {
        "command": "npx",
        "args": [
            "-y",
            "@modelcontextprotocol/server-filesystem",
            ".",
        ],
    },

    "github": {
        "command": "npx",
        "args": [
            "-y",
            "@modelcontextprotocol/server-github",
        ],
    },
}