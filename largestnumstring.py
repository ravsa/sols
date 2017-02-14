def mycmp_func(a, b):
    ab, ba = a + b, b + a
    if ab == ba:
        return 0
    if ab < ba:
        return -1
    return 1

for _ in xrange(int(raw_input())):
    N = raw_input()
    A = raw_input().split()
    A.sort(cmp=mycmp_func, reverse=True)
    print ''.join(A)
