def solution(n, times):
    answer = 0

    times.sort()

    def bsort(T, n):
        low = 1 
        high = T[0] * n 

        while(low <= high):
            count = 0
            mid = (low + high) // 2

            for i in T:
                count += mid // i

            if(n <= count):
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result

    answer = bsort(times, n)
    return answer