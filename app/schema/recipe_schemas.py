from bson.objectid import ObjectId

def RecipeEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "author": str(item["author"]),
        "cookTime": int(item["cookTime"]),
        "ingredientRecommendTags": list(item["ingredientRecommendTags"]),
        "ingredientTags": list(item["ingredientTags"]),
        "ingredientsInfo": list(item["ingredientsInfo"]),
        "likes": int(item["likes"]),
        "name": str(item["name"]),
        "publishedAt": str(item["publishedAt"]),
        "rating": int(item["rating"]),
        "serving": int(item["serving"]),
        "steps": list(item["steps"]),
        "thumbnail": str(item["thumbnail"]),
    }
def RecipesEntity(entity) -> dict:
    return [RecipeEntity(item) for item in entity]