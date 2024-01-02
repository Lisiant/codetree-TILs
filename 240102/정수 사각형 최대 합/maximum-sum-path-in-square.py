import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]* n for _ in range(n)]
res = []

dp[0][0] = graph[0][0]

for i in range(1, n):
    dp[i][0] = dp[i-1][0] + graph[i][0] 
    dp[i][i] = dp[i-1][i-1] + graph[i][i]

for i in range(1, n):
    for j in range(i+1):
        dp[i][j] = max(dp[i-1][j] + graph[i][j], dp[i-1][j-1] + graph[i][j])

for i in range(n):
    temp = sum(graph[n-1]) - graph[n-1][i] + dp[n-1][i]
    res.append(temp)

print(max(res))