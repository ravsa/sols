def fact(num):
    if num <= 1:
        return 1
    return num * fact(num - 1)
for _ in xrange(int(raw_input())):
    num = int(raw_input())
    print fact(num)
