R, C = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = [0, 0]
graph = []

for _ in range(R):
    graph.append(list(map(str, input())))

def bfs(x, y):
    q = []
    sheep, wolf = 0, 0

    if graph[y][x] == 'o':
        sheep += 1
    elif graph[y][x] == 'v':
        wolf += 1
    q.append((x, y))
    graph[y][x] = '#'

    while len(q) > 0:
        newx, newy = q.pop()

        for i in range(4):
            nx = newx + dx[i]
            ny = newy + dy[i]

            if 0 <= nx < C and 0 <= ny < R:

                if graph[ny][nx] != '#':

                    if graph[ny][nx] == 'o':
                        sheep += 1
                    elif graph[ny][nx] == 'v':
                        wolf += 1

                    q.append((nx, ny))
                    graph[ny][nx] = '#'
    
    if sheep > wolf:
        answer[0] += sheep
    else:
        answer[1] += wolf

for i in range(R):
    for j in range(C):
        if graph[i][j] != '#':
            bfs(j, i)

print(*answer)