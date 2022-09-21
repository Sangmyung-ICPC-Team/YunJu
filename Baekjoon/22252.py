import sys, heapq
input = sys.stdin.readline
Q = int(input())
ans = 0
go = {}
name = set()

for _ in range(Q):
    queue = input().split()

    if queue[0] == '1':
        if queue[1] not in name:
            go[queue[1]] = []
            name.add(queue[1])

        for x in queue[3:]:
            heapq.heappush(go[queue[1]], -int(x))

    else:
        if queue[1] not in name:
            continue
        
        for _ in range(min(int(queue[2]), len(go[queue[1]]))):
            ans += -heapq.heappop(go[queue[1]])

print(ans)
