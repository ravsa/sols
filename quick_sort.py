def partition(array, left, right):
    mid = (left + right) / 2
    pivot = array[mid]
    array[mid], array[left] = array[left], array[mid]
def quick_sort(array, left, righ):
    if left < right:
        part = partition(array, left, right)
        quick_sort(array, left, part - 1)
        quick_sort(array, part + 1, right)
