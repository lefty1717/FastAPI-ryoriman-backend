from pydantic import BaseModel, Field

from bson import ObjectId

class IngredientModel(BaseModel):
    _id: ObjectId
    category: str
    imageURL: str
    name: str
    unit: str