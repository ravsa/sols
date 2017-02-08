problem='https://www.codechef.com/problems/CHFANS'
__author__='Ravindra Singh'


def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

T=int(raw_input())
for i in range(T):
    a,b=map(int,raw_input().split())
    if a>b:
        print abs(abs((a-b))//gcd(a,b))
    else:
        print abs(abs((a-b))//gcd(b,a))
