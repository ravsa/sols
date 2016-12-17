import math


def get_distance(A, B):
    x1, y1 = A
    x2, y2 = B
    if x1 == x2:
        return abs(y1 - y2)
    elif y1 == y2:
        return abs(x1 - x2)
    return math.sqrt(pow(abs(x1 - x2), 2) + pow(abs(y1 - y2), 2))
for _ in xrange(int(raw_input())):
    R = int(raw_input())
    A = map(int, raw_input().split())
    B = map(int, raw_input().split())
    C = map(int, raw_input().split())
    c = 0
    if get_distance(A, B) <= R:
        c += 1
    if get_distance(A, C) <= R:
        c += 1
    if get_distance(B, C) <= R:
        c += 1
    if c >= 2:
        print "yes"
    else:
        print "no"
