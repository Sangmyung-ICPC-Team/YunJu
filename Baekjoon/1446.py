import sys

n, d = map(int, sys.stdin.readline().split())
graph = [list(map(int, input().split())) for _ in range(n)]
distance = [i for i in range(d + 1)]

for i in range(d + 1):
    distance[i] = min(distance[i], distance[i-1] + 1)

    for start, end, minway in graph:
        if i == start and end <= d and distance[i] + minway < distance[end]:
            distance[end] = distance[i] + minway

print(distance[d])