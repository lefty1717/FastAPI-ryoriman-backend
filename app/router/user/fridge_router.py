from fastapi import APIRouter, HTTPException

from configuration.core_setting import API_PREFIX
from configuration.db_setting import connect

from bson.objectid import ObjectId
from uuid import uuid4

from model.user_model import Fridge

from schema.user_schemas import fridge

router = APIRouter(
    prefix=f'{API_PREFIX}/user/fridge',
    tags=['Fridge'],
)

@router.get('/get')
async def get_fridge_items_by_user_id(user_id):
    res = fridge(connect.users.users.find_one({"_id": ObjectId(user_id)}))
    return res
@router.post("/add/{user_id}")
async def add_fridge_item(user_id: str, fridge_item: Fridge):
    food = fridge_item.model_dump()
    food["id"] = str(uuid4())
    try:
        res = connect.users.users.update_one(
            {"_id": ObjectId(user_id)},
            {"$push": {"fridge": food}}
        )

        if res.matched_count == 0:
            raise HTTPException(status_code=404, detail="User not found")
        
        return {"message": "Fridge item added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@router.put("/update/{user_id}/{id}")
async def update_fridge_item(user_id: str, id: str, fridge_item: Fridge):
    food = fridge_item.model_dump()
    try:
        result = connect.users.users.update_one(
            {"_id": ObjectId(user_id), "fridge.id": id},
            {"$set": {"fridge.$": food}}
        )

        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="User not found")
        
        return {"message": "Fridge item updated successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@router.delete("/delete/{user_id}/{id}")
async def delete_fridge_item(user_id: str, id: str):
    try:
        result = connect.users.users.update_one(
            {"_id": ObjectId(user_id)},
            {"$pull": {"fridge": {"id": id}}}
        )

        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="User not found")
        
        return {"message": "Fridge item deleted successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))