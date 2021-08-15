import sys
from collections import deque

def bfs(V, n, k):
    queue = deque()
    queue.append(n)

    while queue:
        X = queue.popleft()
        if X == k:
            return V[X]

        for nx in (X+1, X-1, X*2):
            if 0 <= nx < 100001 and V[nx] == 0:
                V[nx] = V[X] + 1
                queue.append(nx)

n, k = map(int, sys.stdin.readline().split())
V = [0] * 100001

print(bfs(V, n, k))
