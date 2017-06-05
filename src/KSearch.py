# ref https://docs.scipy.org/doc/scipy/reference/spatial.html#spatial-data-structures-and-algorithms

from scipy.spatial import KDTree
import numpy
import sqlite3 as sql3

DIM = 3 # dimensions

# TODO: work with DB
con = None
try:
    con = sql3.connect('/home/az/work/NYT/DATA/db_stars')
    con.text_factory = str
    cur = con.cursor()
    # cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    # cur.execute('SELECT id,bf,x,y,z from hygdata0 LIMIT 2')
    cur.execute('SELECT x,y,z from hygdata0 LIMIT 100')
    cur.fetchone()
    data = cur.fetchall()
    # print "SQLite version: %s" % data
except sql3.Error, e:
    print "Error %s:" % e.args[0]
    sys.exit(1)
finally:
    if con:
        con.close()
# exit(0)

# TODO read points into array
# https://github.com/astronexus/HYG-Database
# a = numpy.fromfile('hygdata_v3.csv', sep=',')
a = numpy.array(data)
# print(a)

a.shape = a.size / DIM, DIM

# TODO 1: read input instead: \
# TODO 1:  if no params - assume Earth [0,0]... \
# TODO 1:  read K - number of nearby stars

point =  [ 10.0,   12.234,  50.432] # highly intelligent pick
print 'point:', point

# find 10 nearest points
tree = KDTree(a, leafsize=a.shape[0]+1)
print("Tree is built")
distances, ndx = tree.query([point], k=2)

# print 10 nearest points to the chosen one
print a[ndx]

# TODO 2: get the dname/description for these stars from DB
