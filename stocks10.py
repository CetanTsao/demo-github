# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 19:18:51 2020

@author: User
"""


import sqlite3
import pandas as pd

data = pd.read_csv('stocks.csv')

# 建立資料表
connection = sqlite3.connect('stock_db.db')
cursor = connection.cursor()
cursor.execute(
        '''
        CREATE TABLE stocks (
                id TEXT PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,
                closing_price INT NOT NULL
        );
        '''
)
# 將資料放入資料表 
for i in range(len(data)):
    ID = '00' + str(data['證券代號'][i])
    Name = data['證券名稱'][i]
    Price = data['收盤價'][i]
    cursor.execute('''INSERT INTO stocks VALUES(?, ?, ?)''', (ID, Name, Price))

rows = cursor.execute('''SELECT * FROM stocks WHERE closing_price >30;''')

for row in rows:
        print(f'id:{row[0]}, company_name:{row[1]}, price:{row[2]}')

# 執行存在資料庫
connection.commit()

# 關閉資料庫連線
connection.close()
