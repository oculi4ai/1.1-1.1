import sqlite3 as l
a=l.connect('test15')
a.execute('create table test7 (name TEXT ,id serial)')
a.execute('insert into test7 (name) values ("nn")')
a.commit()
print(a.execute('select * from test7').fetchall())

#AUTOINCREMENT