A, B, _max, winner = 0, 0, 0, 1
for _ in xrange(int(raw_input())):
    A, B = map(sum, zip([A, B], map(int, raw_input().split())))
    if (A - B) > _max:
        _max = A - B
        winner = 1
    elif (B - A) > _max:
        _max = B - A
        winner = 2
print winner, _max
