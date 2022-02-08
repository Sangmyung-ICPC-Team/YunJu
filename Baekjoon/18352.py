from collections import deque
n, m, k, x = map(int, input().split())
graph = [[] for i in range(n+1)]

dis = [2] * (n+1)
dis[x] = 0
check = False

for i in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)

queue = deque()
queue.append(x)

while(queue):
    city = queue.pop()
    for next in graph[city]:
        if dis[next] == 2:
            dis[next] = dis[city] + 1
            queue.append(next)

for i in range(1, n+1):
    if dis[i] == k:
        print(i)
        check = True
if check == False:
    print(-1)
 
