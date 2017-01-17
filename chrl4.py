import operator


def result(value):
    return (reduce(operator.mul, value)) % 1000000007


def dijkstra(matrix, K):
    queue, visited = [], set()
    start, end = matrix[0], matrix[-1]
    queue.append([start])
    while queue:
        path = queue.pop(0)
        currnet_node = path[-1]
        if currnet_node == end:
            return result(path)
        elif currnet_node not in visited:
            visited.add(currnet_node)
            for nxt_nod in [currnet_node + node for node in xrange(1, K + 1)]:
                if nxt_nod not in visited:
                    queue.append(path + [nxt_nod])
    return None


N, K = map(int, raw_input().split())
matrix = map(int, raw_input().split())
print dijkstra(matrix, K)
