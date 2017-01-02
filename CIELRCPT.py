for _ in xrange(int(raw_input())):
    num = int(raw_input())
    count = num / 2048
    num = num % 2048
    while num:
        if num & 1:
            count += 1
        num >>= 1
    print count
