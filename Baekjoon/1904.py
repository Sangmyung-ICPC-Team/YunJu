N = int(input())
li = 1000001 * [0, 1, 2]

for i in range(3, N+1):
    li[i] = (li[i-1] +li[i-2]) % 15746

print(li[N])