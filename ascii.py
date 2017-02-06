string = input().strip()
for substring in string.split():
    temp = ''
    for sno, sub in enumerate(substring):
        if sno % 2 == 0:
            temp = ''.join([temp, "0" * (ord(sub) - 64)])
        else:
            temp = ''.join([temp, "!" * (ord(sub) - 64)])
    print(temp)
