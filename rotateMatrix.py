import sys
sys.stdin = open("input.txt")


def rotate(matrix, angle):
    while angle > 0:
        matrix = map(list, zip(*matrix[::-1]))
        angle -= 90
    return matrix


def query(matrix, K, L):
    return matrix[K][L]


def update(matrix, X, Y, Z):
    matrix[X][Y] = Z
    return matrix


N = int(raw_input())
matrix = list()
total_rotation = 0
for _ in xrange(N):
    temp = map(int, raw_input().split())
    matrix.append(list(temp))
initial_matrix = matrix

while True:
    str = raw_input()
    if str.startswith("A"):
        _, S = str.split()
        total_rotation += int(S)
        matrix = rotate(matrix, int(S))
    elif str.startswith("Q"):
        _, K, L = str.split()
        print(query(matrix, int(K) - 1, int(L) - 1))
    elif str.startswith("U"):
        _, X, Y, Z = str.split()
        initial_matrix = update(initial_matrix, int(X) - 1, int(Y) - 1, int(Z))
        matrix = rotate(initial_matrix, total_rotation)
    else:
        break
