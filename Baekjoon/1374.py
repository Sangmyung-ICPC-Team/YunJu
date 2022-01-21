import sys, heapq
input = sys.stdin.readline

N = int(input())
qlist = []
classroom = []

for i in range(N):
    num, s, t = map(int, input().split())
    qlist.append([s, t])
qlist.sort()
heapq.heappush(classroom, qlist[0][1])

for i in range(1, N):
    if qlist[i][0] < classroom[0]:
        heapq.heappush(classroom, qlist[i][1])
    else:
        heapq.heappop(classroom)
        heapq.heappush(classroom, qlist[i][1])
print(len(classroom))