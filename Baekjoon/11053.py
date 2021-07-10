n = int(input())
li = list(map(int, input().split()))

result = [1] * n

for i in range(n):
    for j in range(i):
        if li[i] > li[j]:
            result[i] = max(result[i], result[j] + 1)

print(max(result))