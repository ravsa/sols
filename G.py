import math

for _ in xrange(int(raw_input())):
    l, r = raw_input().split()
    l = int(l, 16)
    r = int(r, 16)
    count = 0
    data = {}
    for i in xrange(0, 17):
        data[i] = int(math.pow(2, i))
    while l <= r:
        num = hex(l)
        hex_num = num[2:]
        hex_num = set(hex_num)
        temp = sum([data[int(i, 16)] for i in hex_num])
        temp = sum([map(lambda x: math.pow(2, int(x, 16)), hex_num)])
        operation = int(num, 16) ^ temp
        if int(hex(l), 16) > operation:
            count += 1
        l += 1
    print count
