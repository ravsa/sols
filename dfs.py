from collections import defaultdict
#  from heapq import heappush, heappop
import queue


class Graph:

    visited = set()
    Queue = list()

    def __init__(self, G, weighted=False):
        if not weighted:
            self._Nodes = defaultdict(set)
            if isinstance(G, dict):
                self._Nodes = G
            elif isinstance(G, list):
                for node in G:
                    self._Nodes[node[0]] = set()
                for node, adjacent in G:
                    self._Nodes[node].add(adjacent)
        else:
            self._Nodes = defaultdict(list)
            for node, adjacent, cost in G:
                self._Nodes[node].append((cost, adjacent))

    def dijkstra(self, source, dest):
        Q = queue.PriorityQueue()
        Q.put((0, [source]))
        while not Q.empty():
            cost, path = Q.get()
            node = path[-1]
            if node == dest:
                return cost, path
            if node not in self.visited:
                self.visited.add(node)
                for child in self._Nodes[node]:
                    _cost, _node = child
                    Q.put((cost + _cost, path + [_node]))

    def push(self, item):
        self.Queue.append(item)

    def pop(self):
        temp = self.Queue[0]
        self.Queue = self.Queue[1:]
        return temp

    def is_empty(self):
        if self.Queue:
            return False
        return True

    def dfs_has_path(self, source, dest):
        if source in self.visited:
            return False
        self.visited.add(source)
        if source == dest:
            return True
        for node in self._Nodes[source]:
            if self.dfs_has_path(node, dest):
                return True
        return False

    def bfs_has_path(self, source, dest):
        self.push(source)
        while not self.is_empty():
            node = self.pop()
            if node == dest:
                return True
            if node not in self.visited:
                self.visited.add(node)
                for child in self._Nodes[node]:
                    self.push(child)
        return False

    def bfs_shortest_path(self, source, dest):
        self.push([source])
        while not self.is_empty():
            path = self.pop()
            node = path[-1]
            if node == dest:
                return path
            if node not in self.visited:
                self.visited.add(node)
                for child in self._Nodes[node]:
                    self.push(path + [child])
        return False

    def bellman_ford(self, source):  # easist algo
        distance = {node: float('inf') for node in self._Nodes.keys()}
        distance[source] = 0
        for i in xrange(len(self._Nodes) - 1):
            for node in self._Nodes:
                for cost, adjacent in self._Nodes[node]:
                    if distance[node] != float('inf') and (
                            distance[node] + cost) < distance[adjacent]:
                        distance[adjacent] = distance[node] + cost
        for node in self._Nodes:
            for cost, adjacent in self._Nodes[node]:
                if distance[node] != float('inf') and (
                        distance[node] + cost) < distance[adjacent]:
                    print "negative cycle found"
        return distance


g = {
    'a': list('bcd'),
    'b': list('ad'),
    'c': list('ad'),
    'd': list('abc'),
    'e': list()
}


l = [
    ('a', 'b', 1),
    ('a', 'c', 2),
    ('a', 'd', 3),
    ('b', 'a', 1),
    ('b', 'd', 5),
    ('c', 'a', 2),
    ('c', 'd', 7),
    ('c', 'g', 8),
    ('c', 'e', 9),
    ('d', 'a', 3),
    ('d', 'b', 5),
    ('d', 'c', 7),
    ('d', 'f', 13),
    ('d', 'e', 14),
    ('e', 'c', 9),
    ('e', 'd', 14),
    ('e', 'g', 17),
    ('f', 'd', 13),
    ('f', 'g', 19),
    ('g', 'f', 19),
    ('g', 'e', 17),
    ('g', 'c', 8),
]
G = Graph(l, weighted=True)
#  print G.dijkstra('a', 'f')
print G.bellman_ford('a')
