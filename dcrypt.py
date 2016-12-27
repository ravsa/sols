import sys
string = input()
try:
    if string.find("||") == -1:
        print (-1)
        sys.exit()
    try:
        C, B = string.split("||")
    except:
        print (-1)
        sys.exit()
    data = input()
    C = C.strip().split("|")
    if len(set(data)) != 10 or len(C) != 10 or len(B) < 2:
        print(-1)
    else:
        selective_sub = [None] * 10
        A = B[-1]
        B = list(B[:-1])
        for char in C:
            if len(char) > 1:
                for c in list(char[:-1]):
                    selective_sub[int(c)] = char[-1]
        while True:
            try:
                selective_sub.remove(None)
            except:
                break
        for i in B:
            selective_sub[int(i)] = int(selective_sub[int(i)]) + 10
        num_pass = list()
        num_pass.append(int(A))
        for i in range(len(selective_sub) - 1):
            num_pass.append(int(selective_sub[i]) - num_pass[i])
        print(''.join([data[_] for _ in num_pass]))
except:
    print (-1)
