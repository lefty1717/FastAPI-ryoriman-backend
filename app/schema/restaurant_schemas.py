def restaurantEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "borough": str(item["borough"]),
        "cuisine": str(item["cuisine"])
    }
def restaurantsEntity(entity) -> list:
    return [restaurantEntity(item) for item in entity]