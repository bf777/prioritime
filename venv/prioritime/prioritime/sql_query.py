import sqlite3
import numpy

sqlite_file = '/Users/brandon/prioritime/venv/prioritime/prioritime/database.db'
table_name = 'courses_table'
column1 = 'yearlevel'
column2 = 'courseno'
column3 = 'coursename'
column4 = 'whichdays'


con = sqlite3.connect(sqlite_file)
c = con.cursor()

c.execute('SELECT * from courses_table')
courselist = c.fetchall()
len(courselist)
courselist[0]
data1 = numpy.array(courselist)
print data1[0][1]




con.commit()
con.close()
