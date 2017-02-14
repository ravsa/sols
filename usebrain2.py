for index, num in enumerate(map(int, raw_input().split())):
    if not index % 2 == 0:
        print num ** 2,
    else:
        print num ** 3,
