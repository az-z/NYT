# ref https://docs.scipy.org/doc/scipy/reference/spatial.html#spatial-data-structures-and-algorithms
# run in 2.7
import sys, os
from scipy.spatial import KDTree
import numpy
import sqlite3 as sql3
import argparse


# TODO 1: read input instead: \                     - DONE
# TODO 1:  if no params - assume Earth [0,0]... \   - DONE
# TODO 1:  read K - number of nearby stars          - DONE

# TODO 3:  Add functions.               - maybe if i have time.


parser = argparse.ArgumentParser(description='Script looks up shortest distances to the selected coordinates.')
parser.add_argument('-T', '--top'    ,help='Max shortest distances to the stars from provided coordinates',type=int,required=True)
parser.add_argument('-XYZ','--xyz'   ,help='XYZ Decart coordinates in form \'X,Y,Z\'; Default to (0,0,0) (Earth) ',default='0,0,0')

args = parser.parse_args()
K = args.top # ingenious decision
point = [ float(i) for i in  args.xyz.split(',')]

# Lets get the env setup a bit
path= os.path.dirname(os.path.realpath(__file__))

DIM = 3  # dimensions

# TODO: work with DB - DONE
con = None

try:
	con = sql3.connect(path + '/../DATA/db_stars')  # scary
	con.text_factory = str
	cur = con.cursor()
	# cur.execute('SELECT id,bf,x,y,z from hygdata0 LIMIT 2')
	# cur.execute('SELECT x,y,z from hygdata0 LIMIT 100')

	cur.execute('SELECT x,y,z from hygdata0')
	# data_=cur.fetchone()
	# print(data_)
	data = cur.fetchall()
	# print "SQLite version: %s" % data
except sql3.Error, e:
	print "Error %s:" % e.args[0]
	sys.exit(1)
finally:
	if con:
		con.close()
# exit(0)

# TODO read points into array - DONE
# https://github.com/astronexus/HYG-Database
# a = numpy.fromfile('hygdata_v3.csv', sep=',')
a = numpy.array(data)
# print(a)

a.shape = a.size / DIM, DIM

tree = KDTree(a, leafsize=a.shape[0] + 1)
print("Tree is built")

distances, ndx = tree.query([point], k=K)

# print 10 nearest points to the chosen one
# print a[ndx][0]

# TODO 2: get the dname/description for these stars from DB  - DONE

con = sql3.connect(path+'/../DATA/db_stars')
con.text_factory = str
cur = con.cursor()

print "Top %d closest stars to the selected coordinates (%s):" % (K, point)
for row in a[ndx]:
	for item in row:
		cur.execute(
				'SELECT id, proper, dist, x,y,z from hygdata0 where x = {x} and y = {y} and z = {z}'.format(x=item[0],
				                                                                                            y=item[1],
				                                                                                            z=item[2]))
		data = cur.fetchall()
		for i in data:
			print "ID - %(id)s , Common Name - %(proper)s , Dist - %(dist)s , X- %(x)s, Y- %(y)s , Z- %(z)s" % \
			      {"id": i[0], "proper": i[1], "dist": i[2], "x": i[3], "y": i[4], "z": i[5]}



# cur.execute('SELECT id, proper, dist, x,y,z from hygdata0 where x = {x} and y = {y} and z = {z}'.format(x=xyz[0], y=xyz[1], z=xyz[2]))
# data = cur.fetchall()
# for i in data:
# 	print "DBID - %(id)s , Common Name - %(proper)s , Dist - %(dist)s , X- %(x)s, Y- %(y)s , Z- %(z)s" % \
#           { "id" : i[0], "proper" : i[1],  "dist" : i[2], "x" : i[3], "y" : i[4], "z" : i[5] }