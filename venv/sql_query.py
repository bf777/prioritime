import sqlite3
import numpy

sqlite_file = 'db.sqlite3'
table_name = 'courses_table'
column1 = 'yearlevel'
column2 = 'courseno'
column3 = 'coursename'
column4 = 'whichdays'
column5 = 'classlength'

con = sqlite3.connect(sqlite_file)
c = con.cursor()

cursor.execute('SELECT * from courses_table')
courselist = cursor.fetchall()
len(courselist)
courselist[0]
data1 = np.array(courselist)
np.allclose(courses_table, data1)



comm.commit()
comm.close()
