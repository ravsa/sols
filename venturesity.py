from itertools import combinations
from fractions import gcd


def ndq(a, b, c, d):
    if a + b + c > d:
        if a + b + d > c:
            if a + d + c > b:
                if b + c + d > a:
                    return True
    return False

for _ in xrange(int(raw_input())):
    lst = map(int, raw_input().split())[1:]
    com = combinations(lst, 4)
    A, B = 0, 0
    for _ in com:
        if ndq(*_):
            A += 1
        B += 1
    _gcd = gcd(A, B)
    print "%d/%d " % (A//_gcd, B//_gcd)
