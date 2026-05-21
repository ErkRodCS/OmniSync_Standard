# OmniSync Standard Edition
# Author: @erk
# License: MIT
# Source: https://github.com/ErkRodCS/OmniSync_Standard
# -----------------------------------------------------------------------------

import asyncio
from mcp.server import Server
import mcp.types as types
from mcp.server.stdio import stdio_server
from omnisync_engine import OmniSyncEngine

server = Server("omnisync-standard")
engine = OmniSyncEngine()

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """Retorna las herramientas expuestas por OmniSync Standard."""
    return [
        types.Tool(
            name="sync_standard",
            description="Standard SHA-256 secure synchronization (FREE)",
            inputSchema={
                "type": "object",
                "properties": {
                    "feed_id": {
                        "type": "string",
                        "description": "Unique identifier for the sync feed"
                    },
                    "old_content": {
                        "type": "string",
                        "description": "Previous version of the text"
                    },
                    "new_content": {
                        "type": "string",
                        "description": "Updated version of the text"
                    },
                    "last_hash": {
                        "type": "string",
                        "description": "Optional. Previous SHA-256 hash for validation"
                    }
                },
                "required": ["feed_id", "new_content", "old_content"]
            }
        )
    ]

@server.call_tool()
async def handle_call_tool(name: str, arguments: dict | None) -> list[types.TextContent]:
    """Procesa las llamadas a herramientas de OmniSync Standard."""
    args = arguments or {}
    if name == "sync_standard":
        try:
            result = engine.execute_sync(args)
            output = f"🔄 OmniSync Standard Result: [{result.get('changed', False)}]\nDelta: {result.get('delta', 'N/A')}\nCursor: {result.get('cursor', 'N/A')}"
            return [types.TextContent(type="text", text=output)]
        except Exception as e:
            return [types.TextContent(type="text", text=f"❌ Error en sync_standard: {str(e)}")]
    
    raise ValueError(f"Unknown tool: {name}")

async def main() -> None:
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())
