N, M = map(int, input().split())
visited = [0 for _ in range(N)]
dfs_list = []

def dfs(count):
    if count == M:
        print(*dfs_list)
        return
    
    for i in range(N):
        if visited[i] == 0:
            dfs_list.append(i+1)

            dfs(count+1)
            visited[i] = 1
            dfs_list.pop()

            for j in range(i+1, N):
                visited[j] = 0

dfs(0)