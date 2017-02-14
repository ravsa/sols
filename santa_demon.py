import math


def find_distance(A, B):
    x1, y1 = A
    x2, y2 = B
    return math.sqrt((x2 - x1)*2 + (y2 - y1)*2)
A = map(float, raw_input().split())
A, B, C, D = zip(A[::2], A[1::2])
res = [find_distance(A, B), find_distance(
    B, D), find_distance(C, D), find_distance(A, C)]
A = min(res)
res.remove(A)
B = min(res)
res.remove(B)
C = min(res)
res.remove(C)
D = min(res)
if A == B and C == D:
    print "True"
else:
    print "False"
