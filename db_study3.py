# db_study3.py

import pymysql

conn = pymysql.connect(
    host="localhost",
    user="krkr", # 수정?
    password="1234", # 수정?
    database="krkr", # 수정?
    charset='utf8'
)

cur = conn.cursor()

# cur.execute( 쿼리문 )
# conn.commit()

cur.execute("select * from item where item_qa >= %s",
            (30,))

rows = cur.fetchall()
for row in rows:
    print(row)