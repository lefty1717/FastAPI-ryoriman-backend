def fridgeSchema(field) -> dict:
    return {
        "id": str(field["id"]),
        "name": str(field["name"]),
        "startDate": str(field["startDate"]),
        "endDate": str(field["endDate"]),
    }
def fridgeItems(item) -> dict:
    return [fridgeSchema(field) for field in item]
def fridge(field) -> dict:
    return {
        "user_id": str(field["_id"]),
        "fridge": fridgeItems(field["fridge"])
    }

def shoppingListSchema(field) -> dict:
    return {
        "category": str(field["category"]),
        "imageURL": str(field["imageURL"]),
        "name": str(field["name"]),
        "quantity": int(field["quantity"]),
        "unit": str(field["unit"]),
    }
def shoppingListItems(item) -> dict:
    return [shoppingListSchema(field) for field in item]
def shoppingList(field) -> dict:
    return {
        "user_id": str(field["_id"]),
        "shoppingList": shoppingListItems(field["shoppingList"])
    }

def notificationsSchema(field) -> dict:
    return {
        "createdAt": str(field["createdAt"]),
        "isChecked": bool(field["isChecked"]),
        "message": str(field["message"]),
        "title": str(field["title"]),
        "type": str(field["type"]),
    }
def notificationsItems(item) -> dict:
    return [notificationsSchema(field) for field in item]
def notifications(field) -> dict:
    return {
        "user_id": str(field["_id"]),
        "notifications": str(field["notifications"])
    }

def userEntity(field) -> dict:
    return {
        "user_id": str(field["_id"]),
        "name": str(field["name"]),
        "auth": str(field["auth"]), 
        "fridge": fridgeItems(field["fridge"]),
        "email": str(field["email"]),
        "historyIngredients": list(field["historyIngredients"]),
        "imageURL": str(field["imageURL"]),
        "isCompletedRecipes": list(field["isCompletedRecipes"]),
        "isLikedRecipes": list(field["isLikedRecipes"]),
        "notifications": notificationsItems(field["notifications"]),
        "shoppingList": list(field["shoppingList"]),
    }
def usersEntity(item) -> list:
    return [userEntity(field) for field in item]