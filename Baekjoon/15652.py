N, M = map(int, input().split())
dfs_list = []

def dfs(count):
    if len(dfs_list) == M:
        print(*dfs_list)
        return
    
    for i in range(count, N+1):
        dfs_list.append(i)
        dfs(i)
        dfs_list.pop()
    
dfs(1)