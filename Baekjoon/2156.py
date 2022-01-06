N = int(input())
li = []
for i in range(N):
    li.append(int(input()))

cup = [0] * N

cup[0] = li[0]

if N > 1:
    cup[1] = li[0] + li[1]
if N > 2:
    cup[2] = max(li[1] + li[2], li[0] + li[2], cup[1])

for i in range(3, N):
    cup[i] = max(cup[i-1], cup[i-3] + li[i-1] + li[i], cup[i-2] + li[i])

print(cup[N-1])