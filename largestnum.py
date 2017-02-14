import itertools
for _ in xrange(int(raw_input())):
    dig = raw_input()
    data = itertools.permutations(dig, len(dig))
    num = [int(''.join(i)) for i in data]
    mx = max(num)
    while mx % 2 != 0:
        num.remove(mx)
        mx = max(num)
    print mx
