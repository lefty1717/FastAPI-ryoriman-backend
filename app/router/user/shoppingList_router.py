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

@router.get('/{user_id}')
async def get_shopping_list_by_user_id(user_id):
    res = shoppingList(connect.ryoriman_db.users.find_one({"_id": ObjectId(user_id)}))
    return res
@router.post('/{user_id}')
async def add_shopping_list_item(user_id: str, shopping_list_item: ShoppingList):
    try:
        exist_quantity = 0
        shopping_list_item = shopping_list_item.model_dump()
        exist = connect.ryoriman_db.users.find_one(
            {
                "_id": ObjectId(user_id), 
                "shoppingList.name": shopping_list_item["name"]
            },
            {
                "_id": 0, "shoppingList.$": 1
            }
        )
        if exist:
            # 找到該食物數量
            for item in exist["shoppingList"]:
                if item['name'] == shopping_list_item["name"]:
                    exist_quantity = item['quantity']
            connect.ryoriman_db.users.update_one(
                {"_id": ObjectId(user_id), "shoppingList.name": shopping_list_item["name"]},
                {"$set": {"shoppingList.$.quantity": (shopping_list_item["quantity"] + exist_quantity)}}
            )
            
        else:
            connect.ryoriman_db.users.update_one(
                {"_id": ObjectId(user_id)},
                {"$push": {"shoppingList": shopping_list_item}}
            )
        return await get_shopping_list_by_user_id(user_id)

    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))



# @router.delete()
# async def delete_