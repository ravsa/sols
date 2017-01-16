problem='https://www.codechef.com/problems/TRISQ'

T=int(raw_input())
for i in range(T):
    B=int(raw_input())
    x=0
    for j in range(1,((B-2)//2)+1):
        x=x+j
    print x
