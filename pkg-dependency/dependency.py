import couchdb
import time
import mysql

couch = couchdb.Server()
db = couch['registry']
start = time.clock()

for pkg in db:
    print pkg
    try:
        latest = db[pkg]['dist-tags']['latest']
    except:
        continue
    try:
        dependencies = db[pkg]['versions'][latest]['dependencies']
        for key in dependencies:
            mysql.increase(key, False)
    except:
        pass
    try:
        devDependencies = db[pkg]['versions'][latest]['devDependencies']
        for key in devDependencies:
            mysql.increase(key, True)
    except:
        pass

print time.clock() - start
