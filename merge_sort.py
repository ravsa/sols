def combine(array, low, mid, high):
    i, j, temp = low, mid + 1, list()
    while i <= mid and j <= high:
        if array[i] <= array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1
    while i <= mid:
        temp.append(array[i])
        i += 1
    while j <= high:
        temp.append(array[j])
        j += 1
    array[low:high + 1] = temp


def split(array, low, high):
    if low < high:
        mid = (low + high) / 2
        split(array, low, mid)
        split(array, mid + 1, high)
        combine(array, low, mid, high)

array = [2, 5, 1, 6, 0, 1, 6, 21, 4, 32]
split(array, 0, len(array) - 1)
for i in array:
    print i
