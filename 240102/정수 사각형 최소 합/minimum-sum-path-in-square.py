import sys
input = sys.stdin.readline

n = int(input())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [[0] * n for _ in range(n)]
dp[0][n-1] = graph[0][n-1]

for i in range(1, n):
    dp[0][n-i-1] = dp[0][n-i] + graph[0][n-i-1]
    dp[i][n-1] = dp[i-1][n-1] + graph[i][n-1]


for i in range(1, n):
    for j in range(1, n):
        
        dp[i][n-j-1] = min(dp[i-1][n - j - 1] + graph[i][n - j - 1], dp[i][n-j] + graph[i][n - j - 1])


print(dp[n-1][0])