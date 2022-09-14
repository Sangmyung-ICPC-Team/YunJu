import sys 
input = sys.stdin.readline

M, N = map(int, input().split())
bug = [1 for _ in range(2 * M + 1)]  

for _ in range(N):
    zero, one, two = map(int, input().split())
        
    for i in range(zero, zero + one):
            bug[i] += 1
        
    for i in range(zero + one, zero + one + two):
            bug[i] += 2
            
for i in range(M):
    for j in range(M):
        if j == 0:
            print(bug[M - (i + 1)], end=' ')
        else:
            print(bug[M + j - 1], end=' ')
    print()