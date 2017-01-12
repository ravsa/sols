from collections import defaultdict
from heapq import heappop, heappush


def graph(edges):
    G = defaultdict(list)
    for node, neighbour, cost in edges:
        G[node].append((cost, neighbour))
    return G


def dijkstra(graph, start, end):
    queue, visited = [(0, start, ())], set()
    while queue:
        (cost, current_node, path) = heappop(queue)
        if current_node not in visited:
            visited.add(current_node)
            path = (current_node, path)
            if current_node == end:
                return (cost, path)
            for c, v2 in graph.get(current_node, ()):
                if v2 not in visited:
                    heappush(queue, (cost + c, v2, path))

    return float("inf")

if __name__ == "__main__":
    edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11)
    ]

    print "A -> E:"
    print dijkstra(graph(edges), "A", "E")
    print "F -> G:"
    print dijkstra(graph(edges), "F", "G")
