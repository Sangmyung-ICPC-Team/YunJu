import sys

T = int(input())
dp = [1, 2, 4]
li = []

for _ in range(T):
    li.append(int(sys.stdin.readline()))

for i in range(3, max(li)):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])
    
for i in li:
    print(dp[i-1])