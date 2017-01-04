sample = input()
f = open(sample, 'r')
rd = f.readlines()
sum = 0
flag = False
for i in rd[0]:
    if i.isalnum():
        if i.isdigit():
            sum += int(i)
            flag = True
        else:
            flag = False
            break
if flag:
    print (sum+'\n')
else:
    print ("Invalid Input"+'\n')
