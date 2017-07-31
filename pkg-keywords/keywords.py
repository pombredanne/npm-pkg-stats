import couchdb
import time
import mysql

couch = couchdb.Server()
db = couch['registry']
start = time.clock()

for pkg in db:
    print pkg
    try:
        keywords = db[pkg]['keywords']
        for keyword in keywords:
            mysql.increase(keyword)
    except:
        continue

print time.clock() - start
