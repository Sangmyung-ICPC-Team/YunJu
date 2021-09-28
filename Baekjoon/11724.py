import sys

input = sys.stdin.readline

N, M = map(int, input().split())

visited = [0] * N
line = [[0] * N for _ in range(N)]
result = 0

def bfs(num):
    li = [num]
    while li:
        a = li.pop(0)
        for i in range(N):
            if line[a][i] == 1 and visited[i] == 0:
                li.append(i)
                visited[i] = 1


for i in range(M):
    x, y = map(int, input().split())
    line[x - 1][y - 1] = 1
    line[y - 1][x - 1] = 1

for i in range(len(visited)):
    if visited[i] == 0:
        bfs(i)
        result += 1
        
print(result)