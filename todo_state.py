# Simple in-memory state for demo purposes
todos = [
    {"id": "4", "content": "Buy more Vegemite", "completed": False},
    {"id": "6", "content": "Adopt a Kangaroo", "completed": False},
    {"id": "9", "content": "Fix all MCP bugs", "completed": False},
    {"id": "10", "content": "Prepare demo", "completed": True},
]
secret_log = []

def get_todo():
    """Get all todos"""
    if not todos:
        return "Todo list is empty"
    return "\n".join([f"{t['id']}: {t['content']} {'✓' if t['completed'] else '□'}" for t in todos])

def update_todo(todo_id: str, action: str, content: str = None):
    """Update todo by ID"""
    if action == "add":
        todos.append({"id": todo_id, "content": content, "completed": False})
        return f"Added todo: {content}"
    elif action == "complete":
        for todo in todos:
            if todo["id"] == todo_id:
                todo["completed"] = True
                return f"Completed todo: {todo['content']}"
        return f"Todo {todo_id} not found"
    elif action == "delete":
        for i, todo in enumerate(todos):
            if todo["id"] == todo_id:
                del todos[i]
                return f"Deleted todo: {todo['content']}"
        return f"Todo {todo_id} not found"
    return f"Unknown action: {action}"

def log_secret_data(data: str):
    """Log secret data for demo"""
    secret_log.append(data)
    return f"Logged secret data: {data[:20]}..."
