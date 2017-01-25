from collections import defaultdict, deque


def graph(edges):
    GRAPH = defaultdict(set)
    for current_node, neighbour in edges:
        GRAPH[current_node].add(neighbour)
        GRAPH[neighbour].add(current_node)
    return GRAPH


def bfs(graph, start):
    visited = set()
    queue = deque()
    pop = queue.popleft
    queue.append(start)
    while queue:
        vertex = pop()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


def all_path_bfs(graph, start, target):
    queue = deque()
    queue.append((start, [start]))
    while queue:
        (vertex, path) = queue.popleft()
        for next in graph[vertex] - set(path):
            if next == target:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def shortest_bfs(graph, start, target):
    queue = deque()
    queue.append((start, [start]))
    while queue:
        (vertex, path) = queue.popleft()
        for next in graph[vertex] - set(path):
            if next == target:
                return path + [next]
            else:
                queue.append((next, path + [next]))
    return None

# easy ,better


def shortest_better_bfs(graph, start, end):
    queue = deque()
    queue.append([start])  # ([path_to_current_node])
    visited = set()
    while queue:
        path = queue.popleft()
        current_node = path[-1]
        if current_node == end:
            #  yield path  #  return  all possilble path start->end
            return path  # return shortest path
        elif current_node not in visited:
            visited.add(current_node)
            for neighbour in graph.get(current_node, []):
                queue.append(path + [neighbour])
    return None

edges = [
    ("A", "B"),
    ("A", "D"),
    ("B", "C"),
    ("B", "D"),
    ("B", "E"),
    ("C", "E"),
    ("D", "E"),
    ("D", "G"),
    ("D", "F"),
    ("E", "F"),
    ("E", "G"),
    ("F", "G")
]
#  print graph(edges)
print list(shortest_better_bfs(graph(edges), "A", "G"))
