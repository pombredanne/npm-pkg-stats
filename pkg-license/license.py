import couchdb
import time
import util.util
import mysql

couch = couchdb.Server()
db = couch['registry']
start = time.clock()
licenses = {}

for pkg in db:
    try:
        license = db[pkg]['license']
        if license in licenses:
            licenses[license] += 1
        else:
            licenses[license] = 1
    except Exception as e:
        pass
for key, value in licenses.iteritems():
    try:
        mysql.insert(key, value)
    except Exception as e:
        # map(f.write, e.args)
        print e.args
print time.clock() - start
