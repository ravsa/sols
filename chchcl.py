T = int(raw_input())


def validate(value):
    for _ in value:
        if _ > 1:
            return False
    else:
        return True


for _ in xrange(T):
    n, m = map(int, raw_input().split())
    player = True
    lst = [n, m]
    while not validate(lst):
        _max = max(lst)
        lst.remove(_max)
        a = _max / 2
        b = _max - a
        lst.append(a)
        lst.append(b)
        if player:
            player = False
        else:
            player = True
    if not player:
        print "Yes"
    else:
        print "No"
