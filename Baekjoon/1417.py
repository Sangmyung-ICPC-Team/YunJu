import sys
import heapq

N = int(input())
queue = []
dasom = int(input())

for _ in range(N-1):
    other = int(input())
    heapq.heappush(queue, -other)
count = 0

while queue:
    other = -heapq.heappop(queue)

    if dasom > other:
        break
    
    dasom += 1
    count += 1
    heapq.heappush(queue, -(other-1))

print(count)