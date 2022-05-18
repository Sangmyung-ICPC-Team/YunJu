import sys

input = sys.stdin.readline

N, T = map(int, input().split())

time, scor = [0], [0]

for i in range(N):
    t, s = map(int, input().split())
    time.append(t)
    scor.append(s)

dp = [[0 for i in range(T+1)] for j in range(N+1)]
for i in range(1, N+1):
    for j in range(1, T+1):
        if j >= time[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-time[i]] + scor[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][T])