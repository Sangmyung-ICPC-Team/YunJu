N = int(input())
N_list = list(map(int, input().split()))
N_list.sort()
M = int(input())
M_list = list(map(int, input().split()))

for i in range(M):
    low = 0
    high = N - 1
    while low <= high:
        mid = (low + high) // 2
        if N_list[mid] == M_list[i]:
            print(1)
            break
        elif N_list[mid] < M_list[i]:
            low = mid + 1
        else:
            high = mid - 1
        
        if high < low:
            print(0)
            break