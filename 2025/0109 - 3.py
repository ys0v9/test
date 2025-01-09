import sqlite3

conn=sqlite3.connect('test.db')
cur=conn.cursor()

user_id=input('아이디: ').strip()
user_pw=input('이름: ').strip()

sql="""
update member set name=?
where user_id=?
"""
cur.execute(sql, (name,user_id))
conn.commit()

conn.close()