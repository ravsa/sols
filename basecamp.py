import sys
from collections import defaultdict, deque

sys.stdin = open("input.txt")
rows, column = map(int, raw_input().split())
MATRIX = [list() for _ in xrange(rows)]


def edges(MATRIX):
    edg = list()
    for i in xrange(rows):
        for j in xrange(column):
            temp = MATRIX[i][j]
            if i < rows - 1:
                edg.append((temp, MATRIX[i + 1][j]))
            if j < column - 1:
                edg.append((temp, MATRIX[i][j + 1]))
            if i < rows - 1 and j < column - 1:
                edg.append((temp, MATRIX[i + 1][j + 1]))
            if i < rows - 1 and j > 0:
                edg.append((temp, MATRIX[i + 1][j - 1]))
    return edg


def graph(MATRIX):
    GRAPH = defaultdict(set)
    for current_node, next_node in edges(MATRIX):
        GRAPH[current_node].add(next_node)
        GRAPH[next_node].add(current_node)
    return GRAPH


visitor = ['a', 'b', 'c']
visit_no = 0
visit_pla = list()
target = None
scan = list()
for row in xrange(1, rows + 1):
    line = raw_input().split()
    scan.append(line)
    for col, element in enumerate(line, 1):
        if element == 's':
            element = visitor[visit_no]
            visit_pla.append((visitor[visit_no], row, col))
            visit_no += 1
        if element == 'd':
            target = ('d', row, col)
        MATRIX[row - 1].append((element, row, col))


def bfs(graph, start, end):
    queue = deque()
    queue.append([start])
    visited = set()
    while queue:
        path = queue.popleft()
        vertex = path[-1]
        if vertex == end:
            return path
        elif vertex not in visited:
            for current_neighbour in graph.get(vertex, []):
                queue.append(path+[current_neighbour])
            visited.add(vertex)

for start in visit_pla:
    value = start[0]
    sub = ['s', 'a', 'b', 'c']
    G = graph(MATRIX)
    if value == 'c':
        pass
    data = bfs(G, start, target)
    for i in data:
        if i[0] != 'd':
            scan[i[1] - 1][i[2] - 1] = value
    for temp in scan:
        str = ' '.join(temp)
        for word in sub:
            if word != value:
                str = str.replace(word, '-')
        print str
