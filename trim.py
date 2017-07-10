file = open('test.py')
result = open('result.py', 'w')

for line in file.readlines():
    result.write(line.rstrip() + '\n')
file.close()
result.close()
