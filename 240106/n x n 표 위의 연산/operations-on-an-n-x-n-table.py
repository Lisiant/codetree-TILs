import sys

input = sys.stdin.readline
dx = [1, 0]
dy = [0, 1]
INF = int(1e9)

n = int(input())
graph = [list(map(str, input().split())) for _ in range(n)]
max_val, min_val = 0, INF


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def is_operator(op):
    return op == "+" or op == "-" or op == "x"


def calc(cur, new, op):
    a, b = map(int, [cur, new])
    if op == "+":
        return a + b

    if op == "-":
        return a - b

    if op == "x":
        return a * b


def solve(x, y, cur, op):
    global max_val, min_val

    if x == n - 1 and y == n - 1:
        max_val, min_val = max(cur, max_val), min(cur, min_val)
        return

    for i in range(2):
        nx, ny = x + dx[i], y + dy[i]

        if not in_range(nx, ny):
            continue

        if is_operator(graph[nx][ny]):
            solve(nx, ny, cur, graph[nx][ny])
        else:
            res = calc(cur, graph[nx][ny], op)
            solve(nx, ny, res, op)


solve(0, 0, graph[0][0], 0)
print(max_val, min_val)