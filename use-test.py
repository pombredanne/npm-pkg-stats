import couchdb

db = couchdb.Server()['registry']
count = 0

for pkg in db:
  print pkg
  try:
    latest = db[pkg]['dist-tags']['latest']
    for key in db[pkg]['versions'][latest]['devDependencies']:
      count += 1
      break
      # if key in ['mocha', 'tape', 'nyc', 'jest', 'jasmine', 'should', 'chai', 'karma', 'cucumber', 'unexpected', 'ava', 'sinon', 'enzyme', 'testdouble', 'istanbul', 'protractor', 'nightwatch', 'phantom', 'casper', 'wallaby', 'testcafe']:
      #   count += 1
      #   break
  except Exception as e:
      pass

print count
