import couchdb
import time

# couch = couchdb.Server('https://skimdb.npmjs.com/')

# print len(couch['registry'])

db = couchdb.Database('https://registry.npmjs.com')
f = open('stats/remote-main.txt', 'w')
start = time.clock()
keysStats = {}
for pkg in db:
    for id in db[pkg]:
        if id in keysStats:
            keysStats[id] += 1
        else:
            keysStats[id] = 1
for key, value in keysStats.iteritems():
    f.write(key + (5 - len(key) / 4) * '\t' + str(value) + '\n')
f.close()
print time.clock() - start
