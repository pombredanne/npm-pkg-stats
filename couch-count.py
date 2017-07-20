import couchdb
import time
import util

couch = couchdb.Server()
db = couch['registry']
f = open('stats/count.txt', 'w')
start = time.clock()
f.write(util.getLocalTime() + '\n')
f.write(str(len(db)) + '\n')
f.close()
print time.clock() - start
