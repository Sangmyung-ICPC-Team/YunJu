N, M = map(int, input().split())

arr = [input() for _ in range(N)]

visit = [[-1 for _ in range(M)] for _ in range(N)]
queue = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            queue.append([i, j, 0])
            break
    if len(queue):
        break

move = [(1, 1), (0, 1), (-1, 1)]
result = -1

while queue:
    n_queue = []
    for i, j, cnt in queue:
        for m in move:
            ni, nj = i + m[0], j + m[1]
            if 0 <= ni < N and 0 <= nj < M and cnt > visit[ni][nj] and arr[ni][nj] != '#':
                if arr[ni][nj] == 'O':
                    result = max(result, cnt)
                    n_queue.append([ni, nj, cnt])
                elif arr[ni][nj] == 'C':
                    n_queue.append([ni, nj, cnt + 1])
                else:
                    n_queue.append([ni, nj, cnt])
                visit[ni][nj] = cnt
    queue = n_queue
    
print(result)