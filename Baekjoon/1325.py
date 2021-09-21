import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    i, j = map(int,input().split())
    graph[j].append(i)

ans = 0
li = []
computer = 0

visited = [False] * (n+1)
d = deque()


def bfs(i):
    d = deque()
    d.append(i)

    visited = [False] * (n+1)
    visited[i] = True
    count = 1

    while d:
        targetcom = d.popleft()

        for target in graph[targetcom]:
            if not visited[target]:
                d.append(target)
                visited[target] = True
                count += 1
    return count


for k in range(1, len(graph)):
    if len(graph[k]) > 0:
        computer = bfs(k)

        if ans < computer:
            ans = computer
            li = [k]

        elif ans == computer:
            li.append(k)


for result in li:
    print(result)

