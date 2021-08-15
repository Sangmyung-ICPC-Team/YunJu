from collections import deque 
import sys 
sys.setrecursionlimit(100000) 

input = sys.stdin.readline 

def dfs(y, x): 
    dx = [-1, 1, 0, 0] 
    dy = [0, 0, -1, 1] 
    arr[y][x] = 0 
    
    for i in range(4): 
        nx = dx[i] + x
        ny = dy[i] + y 
        if 0 <= nx < m and 0 <= ny < n and arr[ny][nx]: 
            dfs(ny, nx) 

test = int(input()) 
    
for _ in range(test): 
    m, n, k = map(int, input().split()) 
    arr = [[0]*(m) for _ in range(n)] 
    
    for i in range(k): 
        a, b = map(int, input().split()) 
        arr[b][a] = 1 
        
    cnt = 0

    for i in range(n): 
        for j in range(m): 
            if arr[i][j] == 1: 
                cnt += 1 
                dfs(i, j) 
                
    print(cnt)
