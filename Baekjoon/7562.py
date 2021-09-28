import sys

dx = [2, 2, 1, 1, -1, -1, -2, -2] 
dy = [1, -1, 2, -2, 2, -2, 1, -1] 

def bfs(): 
    visited = [[-1] * n for __ in range(n)] 
    q = [] 
    q.append(knight)

    visited[knight[0]][knight[1]] = 0 

    while q: 
        nk = q.pop(0) 

        if nk == move: 
            return visited[nk[0]][nk[1]]

        for i in range(8): 
            nx = nk[0] + dx[i] 
            ny = nk[1] + dy[i]
             
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1: 
                visited[nx][ny] = visited[nk[0]][nk[1]] + 1 
                q.append([nx, ny]) 


for _ in range(int(sys.stdin.readline())): 
    n = int(sys.stdin.readline()) 
    knight = list(map(int, sys.stdin.readline().split())) 
    move = list(map(int, sys.stdin.readline().split())) 
    
    print(bfs())
