from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
check = [-1] * (n+1)

def bfs(node):
    q = deque()
    q.append(node)
    check[node] = 0
    while q:
        node = q.popleft()
        for n in graph[node]:
            if check[n] == -1:
                check[n] = check[node] + 1
                q.append(n)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

bfs(x)

if k not in check:
    print(-1)
else:
    for i in range(n+1):
        if check[i] == k:
            print(i)