import sys

input = sys.stdin.readline
MIISS = lambda: map(int, input().strip().split())
directions = [(0, -1), (1, -1), (-1, -1)]

N, M = MIISS()
arr = list(input().strip() for _ in range(N))
dp = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

def find_a_rabbit_start():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'R':
                return (i, j)


ri, rj = find_a_rabbit_start()
side_doors = []
visited[ri][rj] = True

for j in range(rj + 1, M): 
    for i in range(N):
        if arr[i][j] == '#':
            continue  

        most_carrot_spot = 0
        flag = False 
        for ki, kj in directions:
            ni, nj = i + ki, j + kj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj]: 
                most_carrot_spot = max(most_carrot_spot, dp[ni][nj])
                flag = True

        if flag == False: 
            continue

        visited[i][j] = True 

        if arr[i][j] == 'C':
            dp[i][j] = most_carrot_spot + 1

        elif arr[i][j] == '.':
            dp[i][j] = most_carrot_spot

        elif arr[i][j] == 'O':
            if most_carrot_spot == -1:  
                continue
            dp[i][j] = most_carrot_spot
            side_doors.append(most_carrot_spot)

if side_doors:
    print(max(side_doors))
else:  
    print(-1)