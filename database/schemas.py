def individual_data(todo):
    return{
        "id": str(todo.get("_id", "")),
        "title": todo.get("title", "N/A"),
        "description": todo.get("description", "N/A"),
        "status": todo.get("is_completed", False),
    }

def all_tasks(todos):
    return [individual_data(todo) for todo in todos]