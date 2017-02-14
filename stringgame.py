alpha = list()
for _ in xrange(int(raw_input())):
    alpha.append(raw_input())
if sorted(alpha) == alpha:
    print "yes"
else:
    print "no"
