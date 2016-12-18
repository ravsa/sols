for _ in xrange(int(raw_input())):
    num = int(raw_input())
    sqrt = 1
    while sqrt * sqrt <= num:
        sqrt += 1
    print sqrt - 1
