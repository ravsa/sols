hist = [1, 2, 4]  # , 1, 2, 9]

_max = 0
h, pos = None, None
temph, tempp = None, None
hstack = list()
pstack = list()


def pop():
    global _max, temph, tempp, pos
    temph = hstack.pop()
    tempp = pstack.pop()
    _max = max(_max, temph * (pos - tempp))


for pos in range(len(hist)):
    h = hist[pos]
    if not hstack or h > hstack[-1]:
        hstack.append(h)
        pstack.append(pos)
    elif h < hstack[-1]:
        while hstack and h < hstack[-1]:
            pop()
        hstack.append(h)
        pstack.append(tempp)
while hstack:
    pop()

print _max
