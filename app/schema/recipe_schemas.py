def IngredientTagsSchema(item) -> dict:
    return {
        "name": str(item["name"])
    }
def IngredientTagsItems(item) -> dict:
    return [IngredientTagsSchema(field) for field in item]

def IngredientsInfo() -> dict:
    return {
        "count": str,
        "name": str,
        "unit": str
    }
def IngredientsInfoItems(item) -> dict:
    return [IngredientsInfo(field) for field in item]

def StepsSchema(item) -> dict:
    return {
        "content": str(item["content"]),
        "imageURL": str(item["imageURL"]),
    }
def StepsItems(item) -> dict:
    return [StepsSchema(field) for field in item]

def RecipeEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "author": str(item["author"]),
        "cookTime": int(item["cookTime"]),
        "ingredientRecommendTags": IngredientTagsItems(item["ingredientRecommendTags"]),
        "ingredientTags": IngredientTagsItems(item["ingredientTags"]),
        "ingredientsInfo": IngredientsInfoItems(item["ingredientsInfo"]),
        "likes": int(item["likes"]),
        "name": str(item["name"]),
        "publishedAt": str(item["publishedAt"]),
        "rating": int(item["rating"]),
        "serving": int(item["serving"]),
        "steps": StepsItems(item["steps"]),
        "thumbnail": str(item["thumbnail"]),
    }
def RecipesEntity(entity) -> dict:
    return [RecipeEntity(item) for item in entity]