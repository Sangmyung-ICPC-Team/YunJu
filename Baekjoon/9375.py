T = int(input())
for _ in range(T):
    n = int(input())
    dic = {}
    ans = 1
    for i in range(n):
        name, part = input().split()
        if part in dic:
            dic[part] += 1
        else:
            dic[part] = 1
    for p in dic:
        ans *= dic[p] + 1
    ans -= 1
    print(ans)