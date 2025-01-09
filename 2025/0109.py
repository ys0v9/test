import sqlite3
conn=sqlite3.connect('test.db')
cur=conn.cursor()
cur.execute("""
select * from member
""")

rs=cur.fetchall()
for i in rs:
    user_id = i[0]
    user_pw = i[1]
    name = i[2]
    email = i[3]
    print(user_id,user_pw,name,email)

conn.close()