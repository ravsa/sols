while int(raw_input()):
    number = map(int, raw_input().split())
    if not all([count != number[num - 1] for count, num in enumerate(number, 1)]):
        print "ambiguous"
    else:
        print "not ambiguous"
