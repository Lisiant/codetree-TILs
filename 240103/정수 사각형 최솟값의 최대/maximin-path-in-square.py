import sys
input = sys.stdin.readline

n = int(input())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [[0] * n for _ in range(n)]
dp[0][0] = graph[0][0]

for i in range(1, n):
    dp[i][0] = min(dp[i-1][0], graph[i][0])
    dp[0][i] = min(dp[0][i-1], graph[0][i])

for i in range(1, n):
    for j in range(1, n):
        max_dp = max(dp[i-1][j], dp[i][j-1])
        dp[i][j] = min(graph[i][j], max_dp)

print(dp[n-1][n-1])

"""
경로에 있는 숫자의 최솟값이 가장 크게 만들기

현재 칸의 숫자 -> 위쪽 칸에서 내려오거나 왼쪽 칸에서 오른쪽으로 이동.
경로에서 고려해야 하는 칸: 현재 칸, 현재 칸의 위쪽 칸, 현재 칸의 왼쪽 칸.

현재가 가장 작은 경우 : 무조건 경로는 현재 칸을 선택. (최솟값)

왼 > 위 > 현재
위 > 왼 > 현재 

그렇지 않으면: 가장 작은 값을 제외한 나머지 칸과 현재 칸의 최솟값을 선택.

현재 > 위 > 왼
현재 > 왼 > 위

왼 > 현재 > 위
위 > 현재 > 왼



예제
3
5 2 3
3 2 1
1 2 4

초기값 d[0][0] = graph[0][0]

5 2 2
3 0 0
1 0 0

d[1][1] -> d[0][1], d[1][0], g[1][1]: 2 3 2 -> 2

5 2 2
3 2 0
1 0 0

d[1][2] -> d[1][1], d[0][2], g[1][2]: 2 2 1 -> 1

5 2 2
3 2 1
1 0 0

d[2][1] -> d[1][1], d[2][0], g[2][1]: 2 1 2 -> 2

5 2 2
3 2 1
1 2 0

d[2][2] -> 2, 1, 4 > 2

5 2 2
3 2 1
1 2 0
"""