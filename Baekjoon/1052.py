n, k = map(int, input().split())
answer = n

def water(n):
    count = 0

    while(True):
        bottle = n // 2
        new = n % 2
        count += new
        n = bottle

        if n == 0:
            break

    return count

while(1):
    if(water(answer) <= k):
        break

    answer += 1

print(answer - n)