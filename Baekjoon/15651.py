N, M = map(int, input().split())
dfs_list = []

def dfs(count):
    if count == M:
        print(*dfs_list)
        return

    for i in range(N):
            dfs_list.append(i+1)
            dfs(count+1)
            dfs_list.pop()

dfs(0)