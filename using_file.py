text = 'python test text'
f = open('test.conf', 'w')
f.write(text)
f.close()

f = open('test.conf')

while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end='')

f.close()