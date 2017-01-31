from bisect import bisect
import random
import time
ARRAY = [random.choice(xrange(1000000)) for _ in xrange(1000)]


def normal(ARRAY):
    new = []
    for i in ARRAY:
        new.append(i)
    new.sort()


def b_normal(ARRAY):
    new = []
    for i in ARRAY:
        new.insert(bisect(new, i), i)

start = time.time()
normal(ARRAY)
print "nomral {}".format(time.time() - start)
start = time.time()
b_normal(ARRAY)
print "b_normal {}".format(time.time() - start)
