for _ in xrange(int(raw_input())):
    arr = list()
    for num in xrange(int(raw_input())):
        arr.append(map(int, raw_input().split()))
    for i in xrange(num - 1, -1, -1):
        for j in xrange(i+1):
            arr[i][j] += max(arr[i+1][j], arr[i+1][j+1])
    print arr[0][0]
