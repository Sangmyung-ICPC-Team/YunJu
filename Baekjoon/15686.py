import sys
from itertools import combinations

input= sys.stdin.readline
N, M =map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]

result = 999999
house = []
chicken = []

for i in range(N):
    for j in range(N):
        if map[i][j] == 1:
            house.append((i, j))
        if map[i][j] == 2:
            chicken.append((i, j))

for ch in combinations(chicken, M):

    distance = 0

    for h in house:
        chicken_dis = 999

        for j in range(M):
            chicken_dis = min(chicken_dis, abs(h[0] - ch[j][0]) + abs(h[1] - ch[j][1]))

        distance += chicken_dis

    result = min(result, distance) 

print(result)