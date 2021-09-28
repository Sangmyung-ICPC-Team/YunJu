import sys

N = int(sys.stdin.readline())
danji = [list(sys.stdin.readline()) for _ in range(N)]

dnum = []
count = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(x, y):
    global count

    danji[x][y] = '0'
    count += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if danji[nx][ny] == '1':
            dfs(nx, ny)

for i in range(N):
    for j in range(N):
        if danji[i][j] == '1':
            count = 0
            dfs(i, j)
            dnum.append(count)

print(len(dnum))

dnum.sort()

for i in dnum:
    print(i)