for _ in xrange(int(raw_input())):
    size = int(raw_input())
    A = map(int, raw_input().split())
    c = 0
    while c < 2:
        for j in xrange(size - 1, c, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
        c += 1
    print A[0] + A[1]
