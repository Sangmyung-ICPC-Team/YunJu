n = int(input())
stairs = [0] * 300

for i in range(n):
  stairs[i] = int(input())

ans = [0] * 300
ans[0] = stairs[0]
ans[1] = stairs[0] + stairs[1]
ans[2] = max(stairs[2] + stairs[0], stairs[2] + stairs[1])

for i in range(3, n):
  ans[i] = max(stairs[i] + ans[i-2], stairs[i] + stairs[i-1] + ans[i-3])

print(ans[n-1])