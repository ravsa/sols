import sys
coins = [1, 2, 3, 5, 10, 50, 100, 1000, 2000]


def find_min_coins_iterative(value):
    min_coin = [sys.maxint] * (value + 1)
    for cents in xrange(value + 1):
        min = cents
        for j in [c for c in coins if c <= cents]:
            if min_coin[cents - j] + 1 < min:
                min = min_coin[cents - j] + 1
        min_coin[cents] = min
    return min_coin[value]


def find_min_coins_recusive(value, cache=None):
    if cache is None:
        cache = dict()
    if value in cache:
        return cache[value]
    elif value in coins:
        cache[value] = 1
        return 1
    else:
        min_coin = value
        coin_lessthan_value = [cn for cn in coins if cn <= value]
        for i in coin_lessthan_value:
            num_coins = 1 + find_min_coins_recusive(value - i, cache)
            if num_coins < min_coin:
                min_coin = num_coins
        cache[value] = min_coin
    return cache[value]
print find_min_coins_recusive(263)
