import os
import logging
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'database.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('PRIORITIME_SETTINGS', silent=True)

def connect_db():

    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv



def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')

@app.route('/')
def home():
   return render_template('mainV2.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         yl = request.form['yearlevel']
         cno = request.form['courseno']
         cna = request.form['coursename']
         wd = request.form['whichdays']
         cl = request.form['classlength']

         with sqlite3.connect("database.db") as con:
            app.logger.info(con)
            cur = con.cursor()

            cur.execute("INSERT INTO courses_table (yearlevel,courseno,coursename,whichdays,classlength) VALUES (?,?,?,?,?)",(yl,cno,cna,wd,cl) )

            con.commit()
            msg = "Record successfully added"
      except:
         msg = "error in insert operation"
      return render_template('mainV2.html')

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()
