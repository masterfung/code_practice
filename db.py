import sqlite3

db = sqlite3.connect('people.db')

c = db.cursor()

c.execute('''CREATE TABLE people
            (first Text, last Text, age FLOAT)''')

c.execute(
	"insert into people values ('Jennifer', 'Hua', 31)"
	)

c.execute('select * from people')

db.commit()

results = c.fetchall()

print results

db.close()