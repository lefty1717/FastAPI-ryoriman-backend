from fastapi import APIRouter, HTTPException

from configuration.core_setting import API_PREFIX
from configuration.db_setting import connect

from bson.objectid import ObjectId

from model.ingredient_model import IngredientModel
from schema.ingredient_schemas import ingredientEntity, ingredientsEntity


router = APIRouter(
    prefix=f'{API_PREFIX}/ingredients',
    tags=['ingredients'],
)

@router.get("/all")
async def get_all_ingredients():
    return ingredientsEntity(connect.ryoriman_db.ingredients.find())
@router.get("/{id}")
async def get_ingredients_by_id(id):
    return ingredientEntity(connect.ryoriman_db.ingredients.find_one({"_id": ObjectId(id)}))

@router.post("/add")
async def add_ingredient(ingredient: IngredientModel):
    connect.ryoriman_db.ingredients.insert_one(dict(ingredient))
    return await get_all_ingredients()

@router.put("/update/{id}")
async def update_ingredient(id, ingredient: IngredientModel):
    connect.ryoriman_db.ingredients.update_one(
        {
            "_id": ObjectId(id)
        },
        {
            "$set": dict(ingredient)
        }
    )
    return await get_ingredients_by_id(id)

@router.delete("/delete/{id}")
async def delete_ingredient(id):
    connect.ryoriman_db.ingredients.delete_one({"_id": ObjectId(id)})
    return 'delete success!'