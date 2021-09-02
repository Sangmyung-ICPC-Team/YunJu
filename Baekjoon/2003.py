import sys

input = sys.stdin.readline
 
N, M = map(int, input().split())
A = list(map(int, input().split()))
 
start = 0
end = 0
sum = 0
result = 0
 
while(True):
    if sum >= M:
        sum -= A[end]
        end += 1
    elif start == len(A):
        break
    else:
        sum += A[start]
        start += 1
    
    if sum == M:
        result += 1
 
print(result)