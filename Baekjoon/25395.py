import sys

input  = sys.stdin.readline
N, S = map(int, input().split())

car = list(map(int, input().split()))
fuel = list(map(int, input().split()))

S -= 1
ans = [S + 1]

left = car[S] - fuel[S]
right = car[S] + fuel[S]
first_llo = left
first_rlo = right

left_lo = S
right_lo = S

while True:
    for i in range(right_lo + 1, N):
        if car[i] <= right:
            right = max(right, car[i] + fuel[i])
            left = min(left, car[i] - fuel[i])
            ans.append(i+1)
        else:
            right_lo = i - 1
            break
    else:
        right_lo = N

    for i in range(left_lo - 1, -1, -1):
        if car[i] >= left:
            left = min(left, car[i] - fuel[i])
            right = max(right, car[i] + fuel[i])
            ans.append(i+1)
        else:
            left_lo = i+1
            break
    else:
        left_lo = 0

    if left == first_llo and right == first_rlo:
        break

    first_llo = left
    first_rlo = right

ans.sort()

print(*ans)