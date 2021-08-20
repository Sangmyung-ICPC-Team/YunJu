n = int(input())

for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    m = ((x2 - x1)**2 + (y2 - y1)**2) **0.5

    if r2 > r1:
        r1, r2 = r2, r1

    if m == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if (r1 + r2 == m) or (r1 - r2 == m):
            print(1)
        elif (r1 + r2 > m) and (r1 - r2 < m):
            print(2)
        else:
            print(0)