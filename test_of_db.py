import sqlite3
sqlite_file = 'D:/my_first_db.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

#c.execute('CREATE TABLE table_1 (col1 INTEGER PRIMARY KEY)')
c.execute("ALTER TABLE table_1 ADD COLUMN 'col3' TEXT DEFAULT 'NEW FIELD AGAIN'")
c.execute("INSERT INTO table_1 (col1, col2, COL3) VALUES (2, 'AKomolafe', 'Lanre')")
conn.commit()
conn.close()



