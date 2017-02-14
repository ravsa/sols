notes = [100, 50, 20, 10, 5, 3, 2, 1]


def min_note(value, notes, cache=None):
    if cache is None:
        cache = {}
    if value in cache:
        return cache[value]
    elif value in notes:
        cache[value] = [value]
        return [value]
    elif value == 0:
        return []
    else:
        min_configuration = []
        for coin in notes:
            results = min_note(
                value - coin, notes, cache=cache)
            if results and (not min_configuration or (1 + len(results)) < len(min_configuration)):
                min_configuration = [coin] + results
        cache[value] = min_configuration
    return cache[value]

for _ in xrange(int(raw_input())):
    count = 0
    x = raw_input()
    for value in map(int, raw_input().split()):
        count = count + len(min_note(value, notes))
    print count
