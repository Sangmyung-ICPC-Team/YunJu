import heapq, sys

input = sys.stdin.readline

N, M = map(int, input().split())
heap = []
score = list(map(int, input().split()))
p_score = list(map(int, input().split()))

for i in range(M):
    heapq.heappush(heap, [-1 * p_score[i], score[i]])

N *= 24

while N > 0 and heap[0][0] != 0:
    hpop = heapq.heappop(heap)
    hplus, hscore = -hpop[0], hpop[1]
    
    spend = (100 - hscore) // hplus

    if N >= spend:
        N -= spend

    else:
        spend = N
        N = 0
    
    hscore = spend * hplus + hscore
    hplus = 100 - hscore

    heapq.heappush(heap, [-1 * p_score, score])