k, n = map(int, input().split())
arr = []
for i in range(k):
    arr.append(int(input()))
    
start = 0
end = max(arr)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in arr:
        if i >= mid:
            total += i // mid
    if total < n:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)