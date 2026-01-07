# Memvid MCP Server

A Model Context Protocol (MCP) server that exposes Memvid video memory functionalities to AI clients. Encode text, PDFs, and other content into video memory format for efficient semantic search and chat interactions.

## Quick Start

```bash
# Setup environment
uv venv --python 3.12 --seed
source .venv/bin/activate
uv add -e .

# Run server
uv run python memvid_mcp_server/main.py
```

## Project Structure

- `memvid_mcp_server/` - Main server code
- `library/` - Generated FAISS indexes and memory files

## Key Commands

```bash
# Run tests
uv run pytest

# Format code
uv run black memvid_mcp_server/
uv run ruff check memvid_mcp_server/

# Type check
uv run mypy memvid_mcp_server/
```

## MCP Tools

- `get_server_status` - Check server status
- `add_chunks` - Add text chunks to encoder
- `add_text` - Add single text document
- `add_pdf` - Process and add PDF file
- `build_video` - Build video memory (supports h264/h265)
- `search_memory` - Semantic search on video memory
- `chat_with_memvid` - Chat with encoded knowledge base

## Workflow

1. Add content via `add_text`, `add_chunks`, or `add_pdf`
2. Build video memory with `build_video`
3. Query with `search_memory` or `chat_with_memvid`

## Configuration

See `example_mcp_config.json` for Claude Desktop setup.

## Debugging

- Logs: `~/Library/Logs/Claude/mcp*.log` (macOS)
- Set `LOG_LEVEL=DEBUG` for verbose output
- Use `get_server_status` to check state
