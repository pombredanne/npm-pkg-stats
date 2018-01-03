import MySQLdb
import csv

db = MySQLdb.connect("localhost", "root", "", "newregistry")
cursor = db.cursor()
cursor.execute("SELECT * FROM dependency ORDER BY total DESC LIMIT 5000")
results = cursor.fetchall()
db.close()
with open('test.csv', 'wb') as csvfile:
  for row in results:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow([row[0], row[1], row[2]])
