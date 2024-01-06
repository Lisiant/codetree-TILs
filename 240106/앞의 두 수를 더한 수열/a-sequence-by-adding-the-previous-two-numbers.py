import sys

input = sys.stdin.readline

n = int(input())

memory = [0] * 21


def solve(n):
    if memory[n] != 0:
        return memory[n]

    if n == 0:
        return 0
    if n == 1:
        return 1

    return solve(n - 1) + solve(n - 2)

res = solve(n)
print(res)