# ryoriman-be

1. 安裝requirement.txt中需要的套件
    - 直接使用pip安裝
        - ```pip install -r requirement.txt```
    - 或建立虛擬環境
        1. 根據[如何虛擬環境](https://ithelp.ithome.com.tw/articles/10301302)建立環境。
        2. 安裝requirement.txt中的套件
            ```pipenv install -r requirement.txt```
2. 執行專案
    1. 輸出環境變數
        ```export PROFILE=local```
    2. 執行專案
        ```python app/main.py```
