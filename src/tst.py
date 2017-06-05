import sqlite3 as sql3

con = None
con = sql3.connect('/home/az/work/NYT/DATA/db_stars')
con.text_factory = str
cur = con.cursor()

    # cur.execute('SELECT id,bf,proper,dist,x,y,z from hygdata0')
cur.execute('SELECT bf from hygdata0 LIMIT 2')
 # cur.execute("SELECT name FROM sqlite_master WHERE type='table';")

data = cur.fetchall()
print "SQLite version: %s" % data
