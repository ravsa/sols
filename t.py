import random
import commands
d = 'abz'
for count, i in enumerate(xrange(100000)):
    str = ''.join([random.choice(list(d))
                   for _ in xrange(100)])
    output1 = commands.getoutput('./string ' + str)
    for i in d:
        if str.count(i) % 2 != 0:
            output2 = "NO"
            break
    else:
        output2 = "YES"
    if output1 == output2:
        print count, "pass"
    else:
        print "fail"
        print str
        break
