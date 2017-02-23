intial_name = set(raw_input().split())
print ' '.join(intial_name)
for _ in xrange(int(raw_input())):
    temp = set(raw_input().split())
    intial_name = intial_name ^ temp
    print ' '.join(intial_name)
