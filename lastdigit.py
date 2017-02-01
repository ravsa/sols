n = int(input())
n = 10**7
i = 0
S = 0
j = 0
while i == 0 or pow(2, i) <= n:
    while j <= n:
        S = S + pow(2, (pow(2, i) + 2 * j))
        j += 1
    i += 1
print(str(int(S))[-1])
