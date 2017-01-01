import sys
sys.stdin = open("input.txt")


def _max(i, j):
    if i == num:
        return array[i][j]
    if (i, j) in memory:
        return memory[(i, j)]
    ans = array[i][j] + max(_max(i + 1, j), _max(i + 1, j + 1))
    memory[(i, j)] = ans
    return ans

for _ in xrange(int(raw_input())):
    memory = dict()
    array = list()
    for num in xrange(int(raw_input())):
        array.append(map(int, raw_input().split()))
    print _max(0, 0)
