file = open('input.txt')
N = file.readline()
data = []
for i in file.read().split():
    data.append(int(i))
data.sort()
print data[0], data[1]
