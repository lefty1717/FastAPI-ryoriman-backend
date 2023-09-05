from fastapi import APIRouter, HTTPException

from configuration.core_setting import API_PREFIX
from configuration.db_setting import connect

from bson.objectid import ObjectId
from uuid import uuid4

from model.user_model import ShoppingList
from schema.user_schemas import shoppingList

router = APIRouter(
    prefix=f'{API_PREFIX}/user/shoppingList',
    tags=['Shopping List'],
)

@router.get("/get/{user_id}")
async def get_shopping_list_by_user_id(user_id):
    res = shoppingList(connect.users.users.find_one({"_id": ObjectId(user_id)}))
    return res
@router.post("/add/{user_id}")
async def add_shopping_list_item(user_id: str, shopping_list_item: ShoppingList):
    try:
        shopping_list_item = shopping_list_item.model_dump()
        exist = await get_shopping_list_by_user_id(user_id)
        for item in exist["shoppingList"]:
            if item['name'] == shopping_list_item["name"]:
                exist_quantity = item['quantity']
        if exist:
            connect.users.users.update_one(
                {"_id": ObjectId(user_id), "shoppingList.name": shopping_list_item["name"]},
                {"$set": {"shoppingList.$.quantity": (shopping_list_item["quantity"] + exist_quantity)}}
            )
            
        else:
            connect.users.users.update_one(
                {"_id": ObjectId(user_id)},
                {"$push": {"shoppingList": shopping_list_item}}
            )
        return await get_shopping_list_by_user_id(user_id)
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))

# @router.delete()
# async def delete_