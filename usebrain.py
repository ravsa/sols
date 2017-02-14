for _ in xrange(7):
    num = int(raw_input())
    count = 0
    for i in xrange(1, num+1):
        if num % i == 0:
            count += 1
    print count
