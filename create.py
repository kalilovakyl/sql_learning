import sqlite3

conn = sqlite3.connect("1.db")

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS HUMAN")

create_table = """
    CREATE TABLE HUMAN (
        Email VARCHAR(255) NOT NULL,
        First_name CHAR(25) NOT NULL,
        Last_name CHAR(25),
        Score INT
    );
"""

cursor.execute(create_table)

if cursor:
    print("Table created successfully!")
else:
    print("WE ALL DIE!!!")

conn.commit()
conn.close()
