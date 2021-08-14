import sys

def bfs(edge, x, y, w, h):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    queue = [[x, y]]

    while queue:
        vertex = queue.pop(0)
        for i in range(8):
            x = vertex[0] + dx[i]
            y = vertex[1] + dy[i]

            if 0 <= x <= h-1 and 0 <= y <= w-1 and edge[x][y]:
                edge[x][y] = 0
                queue.append([x, y])

def answer(edge, w, h):
    tmp = 0
    
    for i in range(h):
        for j in range(w):
            if edge[i][j] == 1:
                tmp+=1
                edge[i][j] = 0

                bfs(edge, i, j, w, h)
    print(tmp)


while(1):
    blist = []
    w, h = map(int, sys.stdin.readline().split())

    for i in range(h):
        blist.append(list(map(int, sys.stdin.readline().split())))

    if w == 0 and h == 0:
        break

    answer(blist, w, h)