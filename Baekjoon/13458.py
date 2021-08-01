def solution():
    answer = 0

    for i in range(N):
        if arr[i] > 0:
            arr[i] -= result
            answer += 1
 
        if arr[i] > 0:
            answer += int(arr[i]/M)
 
            if arr[i] % M != 0:
                answer += 1
 
    return answer
 
 
N = int(input())
arr = list(map(int, input().split()))
result, M = map(int, input().split())

print(solution())