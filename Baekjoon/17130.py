import sys
from collections import deque
input=sys.stdin.readline

n, m=map(int, input().split())
board=[]
for _ in range(n):
    board.append(list(input().rstrip()))
for y in range(n):
    for x in range(m):
        if board[y][x]=='R':
            rabit=(y, x, 0)

q=deque([rabit])
visited={}
can=False
move=[[1,0],[1,1],[1,-1]]
ans=0
while q:
    node=q.popleft()
    if node not in visited:
        visited[node]=True
        nx=node[1]; ny=node[0]; nc=node[2]
        ans=max(ans, nc)
        if board[ny][nx]=='O': can=True
        elif board[ny][nx]=='C': nc+=1
        for v in move:
            mx=nx+v[0]; my=ny+v[1]
            if 0<=mx<m and 0<=my<n and board[my][mx]!='#':
                q.append((my, mx, nc))
print(ans if can else -1)