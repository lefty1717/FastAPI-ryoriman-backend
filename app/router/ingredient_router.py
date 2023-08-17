from fastapi import APIRouter

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
async def fetch_all_ingredients():
    return ingredientsEntity(connect.ingredients.ingredients.find())
@router.get("/{id}")
async def fetch_ingredients_by_id(id):
    return ingredientEntity(connect.ingredients.ingredients.find_one({"_id": ObjectId(id)}))

@router.post("/add")
async def add_ingredient(ingredient: IngredientModel):
    connect.ingredients.ingredients.insert_one(dict(ingredient))
    return 'success'

@router.put("/update/{id}")
async def update_ingredient(id, ingredient: IngredientModel):
    connect.ingredients.ingredients.update_one({"_id": ObjectId(id)}, {"$set": dict(ingredient)})
    return ingredientEntity(connect.ingredients.ingredients.find_one({"_id": ObjectId(id)}))

@router.delete("/delete/{id}")
async def delete_ingredient(id):
    connect.ingredients.ingredients.delete_one({"_id": ObjectId(id)})
    return 'success'