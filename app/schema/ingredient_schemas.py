

def ingredientEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "category": str(item["category"]),
        "imageURL": str(item["imageURL"]),
        "name": str(item["name"]),
        "unit": str(item["unit"])
    }
def ingredientsEntity(entity) -> list:
    return [ingredientEntity(item) for item in entity]