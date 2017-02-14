def multiply(a, b, M):
    ans = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            t = 0
            for k in range(3):
                t += (a[i][k] * b[k][j]) % M
            while t < 0:
                t += M
            ans[i][j] = t % M
    return ans


def power(a, n, M):
    ans = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    t = a
    while n != 0:
        if n % 2 == 1:
            ans = multiply(ans, t, M)
        t = multiply(t, t, M)
        n /= 2
    return ans

C, M = map(int, raw_input().split())

t = [[C, 1, 2 - C], [1, 0, 0], [0, 0, 1]]

T = int(raw_input())
while T:
    x = int(raw_input())
    if x == 1:
        print 1
    elif x == 2:
        print 2
    else:
        y = power(t, x - 2, M)
        ans = 2 * y[0][0] + y[0][1] + y[0][2]
        ans %= M
        print ans
    T -= 1
