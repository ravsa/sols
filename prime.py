def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True

pair = [(2, 4), (4, 8), (8, 16), (16, 32), (32, 64), (64, 128), (128, 256), (256, 512),
        (512, 1024), (1024, 2048), (2048, 4096), (4096, 8192), (8192, 16381)]
flag = True
for x, y in pair:
    count = 0
    for num in xrange(x+1, y):
        if is_prime(num):
            count += 1
    print count
