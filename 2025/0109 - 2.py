import sqlite3

conn=sqlite3.connect('test.db')
cur=conn.cursor()

user_id=input('아이디: ').strip()
user_pw=input('비번: ').strip()
name=input('이름: ').strip()
email=input('이메일: ').strip()

sql='insert into member values(?,?,?,?)'
cur.execute(sql, (user_id,user_pw,name,email))
conn.commit()

conn.close()