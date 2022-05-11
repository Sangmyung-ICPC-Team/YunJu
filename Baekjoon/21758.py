N = int(input())
honey = list(map(int,input().split()))
li = []
li.append(honey[0])
result = 0

for i in range(1, N):
    li.append(li[i - 1] + honey[i])

for i in range(1, N-1):
    result = max(result, li[-1] - honey[-1] - honey[i] + li[i-1])

for i in range(1, N-1):
    result = max(result, 2 * li[-1] - honey[0] - honey[i] - li[i])

for i in range(1, N-1):
    result = max(result, li[i] - honey[0] + li[-1] - li[i-1] - honey[-1])
    
print(result)