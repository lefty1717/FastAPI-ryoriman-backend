from fastapi import APIRouter

from configuration.core_setting import API_PREFIX
from configuration.db_setting import connect

from bson.objectid import ObjectId

from model.restaurant_model import Restaurants
from schema.restaurant_schemas import restaurantsEntity

router = APIRouter(
    prefix=f'{API_PREFIX}/test',
    tags=['test'],
)

@router.get("/")
async def fetch_All():
    return restaurantsEntity(connect.sample_restaurants.restaurants.find())
@router.get("/{id}", response_model=Restaurants)
async def fetch_restaurant_by_id(id):
    return connect.sample_restaurants.restaurants.find_one({"_id": ObjectId(id)})