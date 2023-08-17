from pydantic import BaseModel
from typing import List, Optional

from datetime import datetime

from bson import ObjectId

class Fridge(BaseModel):
    id: str
    name: str
    startDate: datetime
    endDate: datetime

class HistoryIngredients(BaseModel):
    category: str
    name: str
    quantity: str
    unit: str
    imageURL: Optional[str]

class IsCompletedRecipes(BaseModel):
    name: str
    imageURL: Optional[str]

class IsLikedRecipes(BaseModel):
    id: str
    recipe: str
    image: Optional[str]

class Notifications(BaseModel):
    createdAt: datetime
    isChecked: bool
    message: str
    title: str
    type: str

class ShoppingList(BaseModel):
    category: str
    imageURL: Optional[str]
    name: str
    quantity: int
    unit: str

class User(BaseModel):
    _id: ObjectId
    name: str
    auth: str
    fridge: List[Fridge]
    email: str
    historyIngredients: List[HistoryIngredients]
    imageURL: str
    isCompletedRecipes: List[IsCompletedRecipes]
    isLikedRecipes: List[IsLikedRecipes]
    notifications: List[Notifications]
    shoppingList: List[ShoppingList]
