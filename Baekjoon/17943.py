N, Q = map(int, input().split())
domino = [0 for i in range(200001)]

xor = list(map(int, input().split()))

for i in range(1, N):
    domino[i] = domino[i-1] ^ xor[i-1]


for i in range(Q):
    li = list(map(int, input().split()))
    if(li[0] == 0):
        x, y = li[1], li[2]
        ans = domino[x-1] ^ domino[y-1]
        print(ans)
    else:
        x, y, d = li[1], li[2], li[3]
        ans = domino[x-1] ^ domino[y-1] ^ d
        print(ans)



