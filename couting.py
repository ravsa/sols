arr = [9, 4, 10, 8, 2, 4]
min = min(arr)
max = max(arr)
temp = {x: 0 for x in range(min, max+1)}
count = 1
for x in arr:
    temp[x] += 1
    count += 1
sorted_list = [None] * count
for x in arr:
    pass

