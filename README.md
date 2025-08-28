# FastMCP Demo - Todo Manager & DLP Monitor

A demonstration FastMCP server that provides todo management capabilities and data loss prevention (DLP) monitoring.

## Features

- **Todo Management**: Create, read, update, and delete todo items
- **DLP Monitoring**: Track and log potential data loss prevention activities
- **FastMCP Integration**: Built with FastMCP for easy MCP server development

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd fastmcp-demo
```

2. Install dependencies using uv:
```bash
uv sync
```

3. Activate the virtual environment:
```bash
source .venv/bin/activate
```

## Usage

Run the MCP server:
```bash
python main.py
```

The server will start on `http://127.0.0.1:8000/mcp`

## Available Tools

### `fetch_todo_list`
Retrieves the current list of todos from the system.

### `update_todo_list`
Updates a specific todo item in the system.
- `todo_id`: The ID of the todo item
- `action`: Action to perform (`add`, `complete`, `delete`)
- `content`: Content for the todo (required for `add` action)

### `data_loss_prevention_monitoring`
Monitors and reports on data loss prevention activities and potential security risks.
- `file_path`: Optional file path to monitor
- `user_id`: Optional user ID to monitor

## Project Structure

- `main.py` - Main FastMCP server implementation
- `todo_state.py` - In-memory state management for todos and DLP logging
- `pyproject.toml` - Project configuration and dependencies

## Development

This is a demo project showcasing FastMCP capabilities. The todo state is stored in-memory and will reset when the server restarts.

## License

This is a demo project for educational purposes.
