import couchdb
import datetime

couch = couchdb.Server()
db = couch['registry']
ch = db.changes(feed='continuous', include_docs=True) 
counter=0
for each in ch:
    counter += 1
    if (counter > 20000):
        print each
        T = datetime.datetime.now
        print T
        counter=0