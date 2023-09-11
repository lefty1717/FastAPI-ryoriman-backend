from fastapi import APIRouter

from configuration.core_setting import API_PREFIX
from configuration.db_setting import connect

from model.recipe_model import RecipeModel
from schema.recipe_schemas import RecipeEntity, RecipesEntity

from bson.objectid import ObjectId

router = APIRouter(
    prefix=f'{API_PREFIX}/recipes',
    tags=['recipes'],
)

@router.get('/{id}')
async def get_recipe_by_id(recipe_id: str):
    return RecipeEntity(connect.ryoriman_db.recipes.find_one({"_id": ObjectId(recipe_id)}))
@router.get('/{name}', response_model=RecipeModel)
async def get_recipe_by_name(name: str):
    return RecipesEntity(connect.ryoriman_db.recipes.find({name: str(name)}))

@router.post('')
async def create_recipe(recipe: RecipeModel):
    connect.ryoriman_db.recipes.insert_one(recipe.dict())
    return recipe

@router.put('/{id}')
async def update_recipe(recipe_id: str, recipe: RecipeModel):
    connect.ryoriman_db.recipes.update_one({"_id": ObjectId(recipe_id)}, {"$set": recipe.dict()})
    return recipe

@router.delete('/{id}')
async def delete_recipe(recipe_id: str):
    connect.ryoriman_db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    return recipe_id