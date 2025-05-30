from fastapi import FastAPI, APIRouter, HTTPException
from configuration import collection
from database.schemas import all_tasks
from database.models import Todo
from bson.objectid import ObjectId
from datetime import datetime
app = FastAPI()
router = APIRouter()


@router.get("/")
async def get_all_todos():
    data = collection.find({"is_deleted": False})
    return all_tasks(data)

@router.post("/")
async def create_task(new_task :Todo):
    try:
        resp = collection.insert_one(new_task.dict())
        return {"status_code": 200, "message": "Task created successfully", "id": str(resp.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{task_id}")
async def update_task(task_id: str, updated_task: Todo):
    try:
        id= ObjectId(task_id)
        exsisting_doc = collection.find_one({"_id": id, "is_deleted":False})
        if not exsisting_doc:
            raise HTTPException(status_code=404, detail="Task not found or already deleted")
        updated_task.updated_at = datetime.timestamp(datetime.now())
        resp = collection.update_one(
            {"_id": id},
            {"$set": dict(updated_task)}
        )
        return {"status_code": 200, "message": "Task updated successfully", "matched_count": resp.matched_count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.delete("/{task_id}")
async def delete_task(task_id: str):
    try:
        id= ObjectId(task_id)
        exsisting_doc = collection.find_one({"_id": id, "is_deleted":False})
        if not exsisting_doc:
            raise HTTPException(status_code=404, detail="Task not found or already deleted")
        resp = collection.update_one(
            {"_id": id},
            {"$set": {"is_deleted": True}}
        )
        return {"status_code": 200, "message": "Task deleted successfully", "matched_count": resp.matched_count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

app.include_router(router)
