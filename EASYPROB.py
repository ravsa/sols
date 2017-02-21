def powers(element):
    binary = {1: "2(0)", 2: "2"}
    for num, i in enumerate(xrange(2, 15), 2):
        temp = list()
        for index, digit in enumerate(bin(num).replace('0b', '')[::-1]):
            if digit == '1':
                temp.append(binary[pow(2, index)])
        binary[pow(2, i)] = '2(' + '+'.join(temp[::-1]) + ')'
    return binary[element]

input = [137, 1315, 73, 136, 255, 1384, 16385]
for num in input:
    copy_num = num
    solution = list()
    j = 0
    while num > 0:
        if num & 1:
            solution.append(powers(pow(2, j)))
        j += 1
        num >>= 1
    print "%d=%s" % (copy_num, '+'.join(reversed(solution)))
