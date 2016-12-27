for _ in xrange(int(raw_input())):
    string = raw_input()
    print(min(string.count('a'), string.count('b')))
