def gcd(lst):
    gcd = lst[0]
    for num in lst[1:]:
        while num > 0:
            gcd, num = num, gcd % num
    return gcd

for _ in xrange(int(raw_input())):
    temp = map(int, raw_input().split())
    N, ing = temp[0], temp[1:]
    del temp
    div = gcd(ing)
    print ' '.join([str(num/div) for num in ing])
