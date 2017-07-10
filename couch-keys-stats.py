import couchdb
import time

pkgs = ['gulp', 'webpack', 'react', 'vue', 'grunt', 'bower']

couch = couchdb.Server()
db = couch['registry']
f = open('stats/main.txt', 'w')
start = time.clock()
keysStats = {}
for pkg in pkgs:
    for id in db[pkg]:
        if id in keysStats:
            keysStats[id] += 1
        else:
            keysStats[id] = 1
for key, value in keysStats.iteritems():
    f.write(key + (4 - len(key) / 4) * '\t' + str(value) + '\n')
f.close()
print time.clock() - start
