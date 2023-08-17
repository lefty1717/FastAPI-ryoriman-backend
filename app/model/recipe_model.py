from typing import Optional
from pydantic import BaseModel, Field
from bson import ObjectId as Oid

class IngredientRecommendTag(BaseModel):
    name: str

class IngredientTag(BaseModel):
    name: str

class IngredientsInfo(BaseModel):
    count: int
    name: str
    unit: str

class Step(BaseModel):
    content: str
    imageURL: Optional[str]

class RecipeModel(BaseModel):
    _id: Oid = Field()
    author: str
    cookTime: int = Field()
    ingredientRecommendTags: list[IngredientRecommendTag]
    ingredientTags: list[IngredientTag]
    ingredientsInfo: list[IngredientsInfo]
    likes: int = Field()
    name: str
    publishedAt: Optional[str] = None
    rating: int = Field()
    serving: int = Field()
    steps: list[Step]
    thumbnail: str
