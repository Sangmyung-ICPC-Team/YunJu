num = list(map(int, input().split()))

N = num[0] 
M = num[1]
T = [] 

for i in range(N):
    T.append(int(input()))

T.sort()

def bsort(T, num):
    low = 1 
    high = T[0] * num 

    while(low <= high):
        count = 0
        mid = (low + high) // 2

        for i in T:
            count += mid // i

        if(num <= count):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result

print(bsort(T, M))