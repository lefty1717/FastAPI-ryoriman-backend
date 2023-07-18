from pydantic import BaseModel

class Restaurants(BaseModel):
    name: str
    borough: str
    cuisine: str
