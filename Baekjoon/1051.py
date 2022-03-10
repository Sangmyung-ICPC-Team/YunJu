n, m = map(int, input().split())
li =[]

for _ in range(n):
    li.append(list(map(int, input())))
sq = 1

for i in range(n-1):
    for j in range(m-1):
        k = 1

        while 1:
            if (i+k) == n or (j+k) == m:
                break

            if li[i][j] == li[i+k][j] and li[i][j] == li[i][j+k] and li[i][j] == li[i+k][j+k]:
                sq = max(sq, (k+1) * (k+1))

            k += 1
print(sq)
