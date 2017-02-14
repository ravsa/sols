import sys
sys.stdin = open("input.txt")

for _ in xrange(int(raw_input())):
    string = int(raw_input())
    count = 0
    max = 0
    while string:
        if string & 1:
            count += 1
        string = string << 1
        if max < count:
            max = count
            count = 0
    print count
