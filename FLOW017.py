for _ in xrange(int(raw_input())):
    A, B, C = map(int, raw_input().split())
    if A < B:
        print B if B < C else C if A < C else A
    else:
        print A if A < C else C if B < C else B
