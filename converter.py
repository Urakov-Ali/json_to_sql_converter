import json
import sqlite3

json_data = open('user_data_1000.json')   
data1 = json.load(json_data)

conn = sqlite3.connect("db.sqlite3")
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS test(
        id INTEGER,
        first_name varchar(30),
        last_name varchar(30),
        email varchar(30),
        gender varchar(30),
        ip_address varchar(30)
        )""")

for i in range(len(data1)):
    value = tuple(data1[i].values())
    c.execute('insert into my_app_myusers values(?,?,?,?,?,?)', value)
conn.commit()
