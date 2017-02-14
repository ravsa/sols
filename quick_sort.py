arr = [1, 1, 8, 5, 6, 7, 3, 4, 2]


def sort(left, right, arr):
    if left >= right:
        return
    pivot = arr[(left + right) // 2]
    index = partition(left, right, arr, pivot)
    sort(left, index - 1, arr)
    sort(index, right, arr)


def partition(left, right, arr, pivot):
    while(left <= right):
        while(arr[left] < pivot):
            left += 1
        while(arr[right] > pivot):
            right -= 1
        if (left <= right):
            arr[left], arr[right] = arr[right], arr[left]
            left, right = left + 1, right - 1
    return left

sort(0, len(arr) - 1, arr)
print arr
