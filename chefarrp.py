import operator

T = int(raw_input())
while T:
    T -= 1
    N = int(raw_input())
    array = map(int, raw_input().split())
    count = 0
    for i in xrange(1, N + 1):
        for j in xrange(N + 1 - i):
            if sum(array[j:j + i]) == reduce(operator.mul, array[j:j + i]):
                count += 1
    print count
