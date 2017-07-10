import couchdb
import time

couch = couchdb.Server()
db = couch['registry']
print db
print len(db)
f = open('npm.txt', 'w')
start = time.clock()
for id in db:
    f.write(id + '\n')
f.close()
print time.clock() - start
