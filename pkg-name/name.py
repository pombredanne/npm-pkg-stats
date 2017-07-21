import couchdb
import time

couch = couchdb.Server()
db = couch['registry']
f = open('./name.txt', 'w')
start = time.clock()
for id in db:
    f.write(id + '\n')
f.close()
print time.clock() - start
