import sys
import random


def is_prime(num, efficiency=1):
    if num < 9:
        return [False, False, True, True, False, True, False, True][num]

    if num & 1 == 0:  # if num is even return False
        return False

    s, d = 0, num - 1  # num - 1 can be written into the 2(^s).d form

    while d & 1 == 0:
        s, d = s + 1, d >> 1

    for a in random.sample(xrange(2, min(num - 2, sys.maxint)), efficiency):
        """
            conditions:
                1. a^((2^r).d) % number !=1 and != n-1 ; r=0
                1. a^((2^r).d) % number ==1 and != n-1 ; r=1 to s-1
        """
        x = pow(a, d, num)
        if x != 1 and x != num - 1:
            for _ in xrange(1, s):
                x = pow(x, 2, num)
                if x == 1:
                    return False
                elif x == num - 1:
                    a = 0
                    break
            if a:
                return False
    return True
