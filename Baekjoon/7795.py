def test(li, a):
    s, e = 0, len(li)-1
    res = -1
    while s <= e:
        m = (s + e) // 2
        if li[m] < a:
            res = m
            s = m + 1
        else:
            e = m - 1
    return res
    
    
for _ in range(int(input())):

    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))

    count = 0

    for a in A:
        count += (test(B, a) + 1)
    print(count)