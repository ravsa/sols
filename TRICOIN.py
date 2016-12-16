import sys
sys.stdin = open("input.txt")


def increament(data):
    def _increament(data):
        yield data.append(data[-1] + len(data) + 1)
    _increament(data).next()

T = int(raw_input())
data = [1]
while T:
    T -= 1
    N = int(raw_input())
    while N >= data[-1]:
        increament(data)
    low, high = 0, len(data) - 1
    mid = (low + high) / 2
    while True:
        if N == data[mid]:
            print data[mid]
            break
        elif len(data[low:high]) <= 4:
            for i in data[low:high]:
                if N > i:
                    pass
                else:
                    break
            print i
            break

        elif N < data[mid]:
            high = mid
        elif N > data[mid]:
            low = mid
        mid = (low + high) / 2
