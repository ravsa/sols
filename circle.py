import math
for _ in xrange(int(raw_input())):
    x, y, c = map(int, raw_input().split())
    a = pow(x, 2) + pow(y, 2) - c
    print "%.1f" % math.sqrt(a)
