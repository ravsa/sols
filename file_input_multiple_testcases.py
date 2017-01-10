import sys
filename = raw_input()
sys.stdin = open(filename)
T = int(raw_input())
for _ in xrange(T):
    try:
        N = map(int, raw_input().split())
        print sum(N)
    except:
        print "Invalid Input"
