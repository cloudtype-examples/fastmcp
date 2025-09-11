"""FastMCP Server with Bearer Token Authentication"""

import os
import json
from datetime import datetime
from typing import Dict, List, Any
from fastmcp import FastMCP

# Initialize FastMCP server (auth disabled for now)
mcp = FastMCP(name="FastMCPServer")

# Sample data store
tasks_db: Dict[int, Dict[str, Any]] = {
    1: {"id": 1, "title": "Setup FastMCP", "completed": True, "created_at": "2024-01-01T10:00:00"},
    2: {"id": 2, "title": "Write documentation", "completed": False, "created_at": "2024-01-01T11:00:00"},
    3: {"id": 3, "title": "Deploy to production", "completed": False, "created_at": "2024-01-01T12:00:00"},
}

# Tools
@mcp.tool
def create_task(title: str, description: str = "") -> Dict[str, Any]:
    """Create a new task."""
    task_id = max(tasks_db.keys()) + 1 if tasks_db else 1
    new_task = {
        "id": task_id,
        "title": title,
        "description": description,
        "completed": False,
        "created_at": datetime.now().isoformat()
    }
    tasks_db[task_id] = new_task
    return new_task

@mcp.tool
def complete_task(task_id: int) -> Dict[str, Any]:
    """Mark a task as completed."""
    if task_id not in tasks_db:
        raise ValueError(f"Task {task_id} not found")
    
    tasks_db[task_id]["completed"] = True
    tasks_db[task_id]["completed_at"] = datetime.now().isoformat()
    return tasks_db[task_id]

@mcp.tool
def list_tasks() -> List[Dict[str, Any]]:
    """List all tasks."""
    return list(tasks_db.values())

@mcp.tool
def health_check() -> Dict[str, Any]:
    """Perform a health check of the server."""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "server": "FastMCP Server",
        "tasks_count": len(tasks_db),
        "auth_enabled": False
    }

# Resources - Read-only data sources
@mcp.resource("tasks://all")
def get_all_tasks() -> str:
    """Get all tasks as JSON."""
    return json.dumps(list(tasks_db.values()), indent=2)

@mcp.resource("tasks://pending")
def get_pending_tasks() -> str:
    """Get pending tasks as JSON."""
    pending_tasks = [task for task in tasks_db.values() if not task["completed"]]
    return json.dumps(pending_tasks, indent=2)

@mcp.resource("tasks://completed")
def get_completed_tasks() -> str:
    """Get completed tasks as JSON."""
    completed_tasks = [task for task in tasks_db.values() if task["completed"]]
    return json.dumps(completed_tasks, indent=2)

# Dynamic task resource
@mcp.resource("tasks://{task_id}")
def get_task_by_id(task_id: str) -> str:
    """Get a specific task by ID."""
    try:
        tid = int(task_id)
        if tid in tasks_db:
            return json.dumps(tasks_db[tid], indent=2)
        else:
            return json.dumps({"error": f"Task {tid} not found"})
    except ValueError:
        return json.dumps({"error": "Invalid task ID format"})

# Prompt templates
@mcp.prompt("task_planning")
def task_planning_prompt(project: str, deadline: str = "no specific deadline") -> List[Dict[str, str]]:
    """Generate a task planning prompt."""
    return [
        {
            "role": "system",
            "content": "You are a project management expert. Help break down projects into manageable tasks."
        },
        {
            "role": "user",
            "content": f"Create a detailed task breakdown for the project '{project}' with deadline: {deadline}. Include priorities and estimated time for each task."
        }
    ]

# ASGI 애플리케이션으로 노출 (uvicorn용)
app = mcp.http_app()

if __name__ == "__main__":
    import uvicorn
    
    host = os.getenv("FASTMCP_HOST", "0.0.0.0")
    port = int(os.getenv("FASTMCP_PORT", "8000"))
    
    print(f"🚀 Starting FastMCP Server on {host}:{port}")
    print("ℹ️  Authentication disabled for testing")
    
    uvicorn.run(app, host=host, port=port)