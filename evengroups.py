import sys
sys.stdin = open("input.txt")

N = int(raw_input())
temp = set()
while True:
    try:
        str, A, B = raw_input().split()
        A = int(A)
        B = int(B)
        tadd = temp.add
        if str == "C":
            if not temp:
                tadd(A)
                tadd(B)
            elif A in temp or B in temp:
                tadd(A)
                tadd(B)
            else:
                temp.clear()
                tadd(A)
                tadd(B)
        elif str == "Q":
            if len(temp) & 1 == 0:
                print len(temp) / 2
            else:
                print "0"
    except:
        break
