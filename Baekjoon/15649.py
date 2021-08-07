n, m = map(int, input().split())

def dfs(result):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    
    for i in range(1, n+1):
        if i in result:
            continue
    
        dfs(result + [i])
dfs([])