f = open('/Users/aopeng/Desktop/test.txt', 'r')
for line in f.readlines():
    print(line.split())
f.close()

