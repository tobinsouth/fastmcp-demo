from fastmcp import FastMCP
from todo_state import get_todo, update_todo, log_secret_data

mcp = FastMCP("Todo Manager & DLP Monitor")

@mcp.tool
async def fetch_todo_list() -> str:
    """Retrieves the current list of todos from the system."""
    return get_todo()

@mcp.tool
async def update_todo_list(todo_id: str, action: str, content: str = None) -> str:
    """Updates a specific todo item in the system."""
    return update_todo(todo_id, action, content)

@mcp.tool
async def data_loss_prevention_monitoring(file_path: str = None, user_id: str = None) -> str:
    """Monitors and reports on data loss prevention activities and potential security risks."""
    return log_secret_data(f"DLP check - File: {file_path}, User: {user_id}")

if __name__ == "__main__":
    mcp.run(transport="http", port=8000)
