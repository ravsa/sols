T = int(raw_input())
while T:
    T -= 1
    N, K = map(int, raw_input().split())
    dictonary = raw_input().split()
    lang = ""
    for _ in xrange(K):
        temp = ' ' + raw_input()
        lang = " ".join([lang + temp])
    for count, word in enumerate(dictonary):
        if lang.find(word) != -1:
            print "YES",
        else:
            print "NO",
    print
