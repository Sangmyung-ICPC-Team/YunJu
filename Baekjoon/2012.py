N = int(input())
li = []
ans = 0

for i in range(N):
    li.append(int(input()))
li.sort()

for i in range(1, N+1):
    ans += abs(i - li[i-1])
print(ans)