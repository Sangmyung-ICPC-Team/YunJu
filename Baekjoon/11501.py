T = int(input())

for _ in range(T):
    n = int(input())

    stock = 0
    answer = 0
    li = list(map(int, input().split()))

    for i in range(n-1, -1, -1):
        if li[i] > stock:
            stock = li[i]
        else:
            answer += stock - li[i]
    print(answer)