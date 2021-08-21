import sys
import heapq

n, m = map(int, input().split())

card = list(map(int, input().split()))
queue = []

for i in range(n):
    heapq.heappush(queue, card[i])

for i in range(m):
    x = heapq.heappop(queue)
    y = heapq.heappop(queue)

    heapq.heappush(queue, x+y)
    #heapq.heappush(queue, x+y)

print(sum(queue))
