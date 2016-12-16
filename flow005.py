problem='https://www.codechef.com/problems/FLOW005'


T=int(raw_input())
for i in range(T):
    count=0
    N=int(raw_input())
    for j in [100,50,10,5,2,1]:
        count=count+N//j
        N=N-(N//j*j)
        if not N:break
    print count
