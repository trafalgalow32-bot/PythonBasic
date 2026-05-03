# db_study1.py

# sqlLite - 설치 안함, 파일 하나로 동작하는 내장형 데이터베이스
# Mysql 같은 데이터베이스는 프로그램 <-> DB 서버 <-> 데이터
# SqlLite는 프로그램 <-> DB파일
'''
    INTEGER - 숫자
    TEXT - 문자열
    REAL - 실수
    BLOB - 바이너리
    NULL - 값 없음
'''

import sqlite3

conn = sqlite3.connect("test.db") # 파일 생성 후 연결

cur = conn.cursor() # 커서 생성

# cur.execute("""
#     create table info (
#             id integer primary key autoincrement,
#             name text,
#             age integer
#         )
# """)

# cur.execute("insert into info (name, age) values (?, ?)",
#             ("김유신", 34))
# conn.commit() # 저장 - DB에 반영

cur.execute("select * from info")

rows = cur.fetchall() # f.read()
# 테이블에서 한줄씩 읽기 - fetchone()
# n 개 가져오기 - fetchmany(n)

for row in rows:
    print(row)