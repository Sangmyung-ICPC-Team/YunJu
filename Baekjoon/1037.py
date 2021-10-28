n = int(input())

nlist = list(map(int, input().split()))

nlist.sort()
answer = nlist[0] * nlist[n - 1]

print(answer)