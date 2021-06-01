num = int(input())
time = list(map(int, input().split()))
result = 0

time.sort()

for i in range(num):
    result += time[i] * (num - i)

print(result)
