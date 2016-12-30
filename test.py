import random
import sys


sys.stdout = open("input.txt", "w")
T = 10
print T
while T:
    T -= 1
    N = random.randint(2, 9)
    data = [str(random.randint(1, 500)) for _ in xrange(N)]
    print N
    print ' '.join(data)
