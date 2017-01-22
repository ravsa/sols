L = int(input())
MATRIX = [[None] * L for i in range(L)]


def spiral(N, M):
    if M <= 0 or N <= 0:
        return
    for x in range(M):
        yield 0, x
    for y in range(1, N - 1):
        yield y, M - 1
    if N != 1:
        for x in reversed(range(M)):
            yield N - 1, x
    if M != 1:
        for y in reversed(range(1, N - 1)):
            yield y, 0
    for x, y in spiral(N - 2, M - 2):
        yield x + 1, y + 1

count = 0
powerpoints = 1
cordinates = [(0, 0)]

for i, j in spiral(L, L):
    count += 1
    MATRIX[i][j] = count
    if count % 11 == 0:
        powerpoints += 1
        cordinates.append((i, j))

for i in range(L):
    for j in range(L):
        print("{}".format(MATRIX[i][j]), end='\t')
    print(end='\n')

print("Total Power points : {}".format(powerpoints))
for cor in (cordinates):
    print("(%d,%d)"%cor)
