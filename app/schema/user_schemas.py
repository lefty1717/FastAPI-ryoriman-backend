def fridge(item) -> dict:
    return {
        "id": str(item["id"]),
        "name": str(item["name"]),
        "startDate": str(item["startDate"]),
        "endDate": str(item["endDate"]),
    }
def fridgeItems(entity) -> dict:
    return [fridge(item) for item in entity]
def fridgeSchema(item) -> dict:
    return {
        "id": str(item["_id"]),
        "fridge": fridgeItems(item["fridge"])
    }

def notification(item) -> dict:
    return {
        "createdAt": str(item["createdAt"]),
        "isChecked": bool(item["isChecked"]),
        "message": str(item["message"]),
        "title": str(item["title"]),
        "type": str(item["type"]),
    }
def notificationsItems(entity) -> dict:
    return [notification(item) for item in entity]
def notificationsSchema(item) -> dict:
    return {
        "id": str(item["_id"]),
        "notifications": str(item["notifications"])
    }

def userEntity(item) -> dict:
    print(item)
    return {
        "id": str(item["_id"]),
        "name": str(item["name"]),
        "auth": str(item["auth"]),
        "fridge": fridgeItems(item["fridge"]),
        "email": str(item["email"]),
        "historyIngredients": list(item["historyIngredients"]),
        "imageURL": str(item["imageURL"]),
        "isCompletedRecipes": list(item["isCompletedRecipes"]),
        "isLikedRecipes": list(item["isLikedRecipes"]),
        "notifications": notificationsItems(item["notifications"]),
        "shoppingList": list(item["shoppingList"]),
    }
def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]