for _ in xrange(int(raw_input())):
    N, M = map(int, raw_input().split())
    A = set(map(int, raw_input().split()))
    B = set(map(int, raw_input().split()))
    print len(A.intersection(B))
