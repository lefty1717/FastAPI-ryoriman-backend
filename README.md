# ryoriman-be FastAPI + MongoDB

1. 安裝requirement.txt中需要的套件
    - 直接使用pip安裝
        - ```pip install -r requirement.txt```
    - 或建立虛擬環境
        1. 根據[如何虛擬環境](https://ithelp.ithome.com.tw/articles/10301302)建立環境。
        2. 安裝requirement.txt中的套件
            ```pipenv install -r requirement.txt```
2. 執行專案
    1.開啟虛擬環境
       ```pipenv shell```
   
    2. 輸出環境變數
        ```export PROFILE=local```
    3. 執行專案
        ```python app/main.py```
4. 加入IP加入DB存取許可
    1. 到MongoDB SECURITY底下的Network Access將自己的IP位址加入存取許可。
    2. 點選Add IP Access中的 ADD CURRENT IP ADDRESS加入當前IP位址

## API 實體
- 使用者 user
    - id: string
    - name: string
    - email: string
    - password: string
- 食材 ingredient
    - id: string
    - name: string
    - unit: string
    - price: int
- 食譜 recipe
    - id: string
    - name: string
    - ingredients: [
        - ingredient_id: string
        - amount: int
    ]
- 冰箱 refrigerator
    - id: string
    - user_id: string
    - ingredients: [
        - ingredient_id: string
        - amount: int
    ]

## API 規格
- 使用者 user
    - 新增使用者(註冊)
        - POST /users
        - Request
            ```json
            {
                "name": "string",
                "email": "string",
                "password": "string"
            }
            ```
        - Response
            ```json
            {
                "id": "string",
                "name": "string",
                "email": "string",
                "password": "string"
            }
            ```
    - 取得使用者(登入後取得個人資料)
        - GET /users/{id}
        - Response
            ```json
            {
                "id": "string",
                "name": "string",
                "email": "string",
                "password": "string"
            }
            ```
    - 更新使用者(修改使用者個人資料)
        - PUT /users/{id}
        - Request
            ```json
            {
                "name": "string",
                "email": "string",
                "password": "string"
            }
            ```
        - Response
            ```json
            {
                "id": "string",
                "name": "string",
                "email": "string",
                "password": "string"
            }
            ```
    <!-- - 刪除使用者
        - DELETE /users/{id}
        - Response
            ```json
            {
                "id": "string",
                "name": "string",
                "email": "string",
                "password": "string"
            }
            ``` -->
- 食材 ingredients
    <!-- - 新增食材
        - POST /ingredients
        - Request
            ```json
            {
                "name": "string",
                "unit": "string",
                "price": "int"
            }
            ```
        - Response
            ```json
            {
                "id": "string",
                "name": "string",
                "unit": "string",
                "price": "int"
            }
            ``` -->
    - 取得食材列表(用於前端顯示使用者可選用食材)
        - GET /ingredients
        - Response
            ```json
            [
                {
                    "id": "string",
                    "name": "string",
                    "unit": "string",
                    "price": "int"
                }
            ]
            ```
    <!-- - 取得食材
        - GET /ingredients/{id}
        - Response
            ```json
            {
                "id": "string",
                "name": "string",
                "unit": "string",
                "price": "int"
            }
            ``` -->
    <!-- - 更新食材
        - PUT /ingredients/{id}
        - Request
            ```json
            {
                "name": "string",
                "unit": "string",
                "price": "int"
            }
            ```
        - Response
            ```json
            {
                "id": "string",
                "name": "string",
                "unit": "string",
                "price": "int"
            }
            ``` -->
    <!-- - 刪除食材
        - DELETE /ingredients/{id}
        - Response
            ```json
            {
                "id": "string",
                "name": "string",
                "unit": "string",
                "price": "int"
            }
            ``` -->
- 食譜 recipes
    - 新增食譜
        - POST /recipes
        - Request
            ```json
            {
                "name": "string",
                "ingredients": [
                    {
                        "ingredient_id": "string",
                        "amount": "int"
                    }
                ]
            }
            ```
        - Response
            ```json
            {
                "id": "string",
                "name": "string",
                "ingredients": [
                    {
                        "ingredient_id": "string",
                        "amount": "int"
                    }
                ]
            }
            ```
    - 取得食譜列表
        - GET /recipes
        - Response
            ```json
            [
                {
                    "id": "string",
                    "name": "string",
                    "ingredients": [
                        {
                            "ingredient_id": "string",
                            "amount": "int"
                        }
                    ]
                }
            ]
            ```
    - 取得食譜
        - GET /recipes/{id}
        - Response
            ```json
            {
                "id": "string",
                "name": "string",
                "ingredients": [
                    {
                        "ingredient_id": "string",
                        "amount": "int"
                    }
                ]
            }
            ```
    - 更新食譜
        - PUT /recipes/{id}
        - Request
            ```json
            {
                "name": "string",
                "ingredients": [
                    {
                        "ingredient_id": "string",
                        "amount": "int"
                    }
                ]
            }
            ```
        - Response
            ```json
            {
                "id": "string",
                "name": "string",
                "ingredients": [
                    {
                        "ingredient_id": "string",
                        "amount": "int"
                    }
                ]
            }
            ```
    - 刪除食譜
        - DELETE /recipes/{id}
        - Response
            ```json
            {
                "id": "string",
                "name": "string",
                "ingredients": [
                    {
                        "ingredient_id": "string",
                        "amount": "int"
                    }
                ]
            }
            ```
- 冰箱 refrigerators
    - 新增冰箱
        - POST /refrigerators
        - Request
            ```json
            {
                "user_id": "string",
                "ingredients": [
                    {
                        "ingredient_id": "string",
                        "amount": "int"
                    }
                ]
            }
            ```
        - Response
            ```json
            {
                "id": "string",
                "user_id": "string",
                "ingredients": [
                    {
                        "ingredient_id": "string",
                        "amount": "int"
                    }
                ]
            }
            ```
    - 取得冰箱列表
        - GET /refrigerators
        - Response
            ```json
            [
                {
                    "id": "string",
                    "user_id": "string",
                    "ingredients": [
                        {
                            "ingredient_id": "string",
                            "amount": "int"
                        }
                    ]
                }
            ]
            ```
    - 取得冰箱
        - GET /refrigerators/{id}
        - Response
            ```json
            {
                "id": "string",
                "user_id": "string",
                "ingredients": [
                    {
                        "ingredient_id": "string",
                        "amount": "int"
                    }
                ]
            }
            ```
    - 更新冰箱
        - PUT /refrigerators/{id}
        - Request
            ```json
            {
                "user_id": "string",
                "ingredients": [
                    {
                        "ingredient_id": "string",
                        "amount": "int"
                    }
                ]
            }
            ```
        - Response
            ```json
            {
                "id": "string",
                "user_id": "string",
                "ingredients": [
                    {
                        "ingredient_id": "string",
                        "amount": "int"
                    }
                ]
            }
            ```
    - 清空冰箱
        - DELETE /refrigerators/{id}
        - Response
            ```json
            {
                "id": "string",
                "user_id": "string",
                "ingredients": [
                    {
                        "ingredient_id": "string",
                        "amount": "int"
                    }
                ]
            }
            ```
