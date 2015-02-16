import sqlite3

db = sqlite3.connect('Awesome DB')

c = db.cursor()

table = ('people')


c.execute('''CREATE TABLE IF NOT EXISTS {}
            (Name Text)'''.format(table))

c.execute(
	"insert into people values ('Jennifer')"
	)

c.execute('select * from people')

db.commit()

results = c.fetchall()

print results

db.close()