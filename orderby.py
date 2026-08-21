import sqlite3 

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

table = """
    create table phones (
        id int,
        age int, 
        address char(50)
    );
"""

cursor.execute("drop table if exists phones")
cursor.execute(table)

cursor.execute("insert into phones values (1, 20, 'bishkek')")
cursor.execute("insert into phones values (2, 21, 'moscow')")
cursor.execute("insert into phones values (3, 45, 'new york')")
cursor.execute("insert into phones values (4, 23, 'tashkent')")
cursor.execute("insert into phones values (5, 30, 'almaty')")

cursor.execute("select * from phones order by age limit 4")

for i in cursor.fetchall():
    print(i)

conn.commit()
conn.close()
