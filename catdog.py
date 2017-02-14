for _ in xrange(int(raw_input())):
    C, D, L = map(int, raw_input().split())
    max = (D + C) * 4
    if(D < C and (2 * D) < C):
        min = (D + (C - (2 * D))) * 4
        if (L >= min) and (L <= max) and (L % 4 == 0):
            print "yes"
        else:
            print "no"
    else:
        min = D * 4
        if((L >= min) and (L <= max) and (L % 4 == 0)):
            print "yes"
        else:
            print "no"
