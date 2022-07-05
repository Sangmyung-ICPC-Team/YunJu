from collections import deque

lix, liy = 0, 0
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

N = int(input())
house = [list(input().strip()) for _ in range(N)]

li = [[[-1]*4 for _ in range(N)] for _ in range(N)]

q = deque()

def bfs():
    while q:
        x, y, z = q.popleft()
        if x == lix and y == liy:
            print(li[x][y][z])
            return

        nx = x + dx[z]
        ny = y + dy[z]

        while move(nx, ny, z) and house[nx][ny] == '.':
            nx = nx + dx[z]
            ny = ny + dy[z]

        if move(nx, ny, z) and house[nx][ny] == '!':
            li[nx][ny][z] = li[x][y][z]
            q.append((nx, ny, z))
            if z < 2:
                k = 2
            else: 
                k = 0

            for i in range(k, k+2):
                if li[nx][ny][i] == -1:
                    li[nx][ny][i] = li[x][y][z] + 1
                    q.append((nx, ny, i))

def move(x, y, z):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if li[x][y][z] == '*':
        return False
    return True

for i in range(N):
    for j in range(N):
        if house[i][j] == '#':
            if not q:
                for k in range(4):
                    q.append((i, j, k))
                    li[i][j][k] = 0
            else:
                lix, liy = i, j
            house[i][j] = '!'
bfs()